#===========================SKILL CLASS===========================#
#Skills are based on the base skill class

import math
from Colors import colorStat, cyan


class Skill:
    # name = "GenericSkill"
    # type = "generic"    #Buff, Damaging, Defensive
    # costType = "stamina"   
    # cost = 0
    # skillValue = 1    
    # castMessage = "You cast genericSpell!"
    # description = "This is the base skill class; has no effect"
    # cooldown = 0
    # cooldownCap = 0
    # mods = []  #Mods change the way the skill works. ex: "reflect" uses the enemies damage instead
    # holder = None  

    def __init__(self, name, type, costType, cost, skillValue, description, castMessage, cooldown=0, mods = []):
        availableCostTypes = ["mp", "stamina"]
        if costType not in availableCostTypes:
            print("Skill has invalid cost type: [" + str(costType) + "]")
            costType = "mp"
        self.name = str(name)
        self.type = type
        self.costType = costType #stamina, mp, hp
        self.cost = cost
        self.skillValue = skillValue #Damage multi, toughness, Damage (one instance), ect
        self.description = description
        self.castMessage = castMessage
        self.cooldown = 0
        self.cooldownCap = cooldown
        self.mods = mods #Mods change the way the skill works. ex: "reflect" uses the enemies damage instead
        self.holder = None #Character that skill is bound to. use skill.bind(character) to initialize holder

    #Makes the spell do it's effect
    def cast(self, target=None):
        caster = self.holder
        self.cooldown = self.cooldownCap + 1
        if self.type == "attack":
            self.consumeResource()
            if "reflect" in self.mods:
                #skillValue should be a number between 0 and 1. smaller number = more damage delt and less taken
                return target.attack() * abs( 1 - self.skillValue) + caster.attack()
            else:
                return caster.attack() * self.skillValue

    #Returns True if the skill can be used, and returns the message why it cant be used if it cant be used
    def checkUsability(self):
        caster = self.holder
        self.configure()
        if self.costType == "mp":
            if caster.mp < self.cost:
                return self.tooExpensiveMessage()
        elif self.costType == "stamina":
            if caster.stamina < self.cost:
                return self.tooExpensiveMessage()
        if self.cooldown > 0:
            return f"Skill on cooldown for [{cyan(self.cooldown)}] more turns"
        return True #If none of the other requirements dont return a fail message
    
    #Message for not having enough [mana, stamana, ect] to cast spell
    def tooExpensiveMessage(self):
        return "Insufficient [" + colorStat(self.costType, self.costType) + "]"

    #Consumes the resource from the caster [mp, stamina] when spell is cast
    def consumeResource(self):
        caster = self.holder
        if self.costType == "mp":
            caster.mp -= self.cost
        elif self.costType == "stamina":
            caster.stamina -= self.cost
    
    #reduces skill cooldown, called at end of turn
    def tick(self):
        if self.cooldown > 0:
            self.cooldown -= 1
    
    #placeholder for other skill types.
    def configure(self):
        pass

    def bind(self, character):
        self.holder = character
        character.skills[self.name] = self

#This skill converts one resource type to another
class ConvertionSkill(Skill):
    name = "ConvertionSkill"
    type = "conversion"
    costType = "stamina"   #What is being converted
    cost = 0
    convertTo = "mp" #What is the output of the conversion
    convertionRatio = 1 
    castMessage = "You cast genericSpell!"
    description = "This is the base skill class; has no effect"
    def __init__(self, name, costType, convertTo, cost, convertionRatio, description, castMessage, cooldown = 0):
        availableCostTypes = ["mp", "stamina"]
        if costType not in availableCostTypes:
            print("Skill has invalid cost type: [" + str(costType) + "]")
            costType = "mp"
        if convertTo not in availableCostTypes:
            print("Skill has invalid cost type: [" + str(convertTo) + "]")
            convertTo = "stamina"
        self.convertTo = convertTo
        self.convertionRatio = convertionRatio
        super().__init__(name, "conversion", costType, cost, convertionRatio, description, castMessage, cooldown=cooldown)

    #Overrights default cast function
    def cast(self, target=None):
        caster = self.holder
        self.cooldown = self.cooldownCap + 1
        self.consumeResource()
        self.castMessage = "You have recovered [" + colorStat(round(self.cost * self.convertionRatio, 2), self.convertTo) + "] " + self.convertTo
        if self.convertTo == "mp":
            caster.changeMP(self.cost * self.convertionRatio)
        elif self.convertTo == "stamina":
            caster.changeStamina(self.cost * self.convertionRatio)
        return 0
    
    #Sets the cost to a percentage of the resource that the caster is converting to
    def configure(self):
        caster = self.holder
        casterResources = {"mp": caster.maxMP, "stamina": caster.maxStamina}
        self.cost = 1 + casterResources[self.convertTo]/3
        if self.cost > casterResources[self.costType]:
            self.cost = casterResources[self.costType]
    
#This skill type effects the stats of the target
class BuffSkill(Skill):
    # name = "buffskill"
    # type = "buff"
    # costType = "stamina"
    # cost = 0
    # skillValue = 1 #Stat multi
    # duration = 0
    # turnsLeft = 0 #Duration left
    # stats = ["power", "toughness"]
    # castMessage = "You cast BuffSkill!"
    # description = "Buff skill can buff or debuff!"
    # currentTarget = None  #Entity that is being buffed
    def __init__(self, name, costType, cost, stats, skillValue, duration,  description, castMessage, cooldown=0):
        self.stats = stats 
        self.duration = duration
        self.cooldownCap = cooldown if cooldown > self.duration else self.duration
        self.currentTarget = None
        self.turnsLeft = 0
        super().__init__(name, "buff", costType, cost, skillValue, description, castMessage, cooldown=self.cooldownCap)

        
    #Called when the skill is cast
    def cast(self, target):
        caster = self.holder
        self.cooldown = self.cooldownCap + 1
        self.consumeResource()
        self.currentTarget = target
        if "power" in self.stats:
            target.powerMultis[self.name] = self.skillValue
        if "toughness" in self.stats:
            target.toughnessMultis[self.name] = self.skillValue
        self.turnsLeft = self.duration
        return -1
    
    #Cooldowns reduce, time left on buffs reduce
    def tick(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.currentTarget:
            self.turnsLeft -= 1
            if self.turnsLeft <= 0:
                self.deleteBuffs()
        else:
            self.turnsLeft = 0
    
    #Deletes the buffs from the current target
    def deleteBuffs(self):
        self.turnsLeft = 0
        try:
            if "power" in self.stats:
                del self.currentTarget.powerMultis[self.name]
            if "toughness" in self.stats:
                del self.currentTarget.toughnessMultis[self.name]
        except:
            pass #no buffs to delete on target
        self.currentTarget = None

