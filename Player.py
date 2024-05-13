#===========================PLAYER CLASS===========================#
#The player is instanced off of this class
from Functions import *
from Character import *
from Colors import *
import random
class Player(Character):
    
    def __init__(self, maxHP, power, maxMP, toughness, maxStamina):
        super().__init__(maxHP, power, maxMP, toughness, maxStamina, 0, 0, "Player", "")
        self.restCountdown = 3
        self.restCooldown = 2
        self.shopCooldown = 3
        self.monstersKilled = 0
        self.nextTraits = ["Big Muscles", "Thick Skin", "Mana Affinity"]
    
    def statsheet(self):
        self.calculateStats()
        print(r'''
    O
   \|/ 
    |
   / \
              ''')
        printSeperator(30, "═")
        print("Traits: ", end="")
        for trait in self.traits.values():
            print("[" + trait.displayName() + "]", end="")
        print()
        print("HP: " + self.display("hp") + "/" + self.display("maxHP"))
        print("Stamina: " + self.display("stamina") + "/" + self.display("maxStamina"))
        print("MP: " + self.display("mp") + "/" + self.display("maxMP"))
        print("Power: " + self.display("Power"))
        print("Toughness: " + self.display("Toughness"))
        print("Essence: " + self.display("Essence"))
        print("Gold: " + self.display("Gold"))
        printSeperator(30, "═")

    def displaySkills(self):
        printSeperator(30)
        skills = self.skills.values()
        print("Active skills: " + str(*[f"[{green(str(skill.name).capitalize())}({cyan(skill.turnsLeft)})]" for skill in skills if skill.type == "buff" and skill.turnsLeft > 0]))
        count = 0
        for skill in skills:
            skill.configure()
            count += 1
            cost = None
            if skill.costType == "mp":
                cost = blue(round(skill.cost, 2))
            elif skill.costType == "stamina":
                cost = yellow(round(skill.cost, 2))

            print("(" + green(count) +  ")[" + cyan(skill.name.capitalize()) + "] [" + cost + "] " + skill.costType.capitalize() + ":  " + skill.description)
        printSeperator(30)
    
    def changeMP(self, num):
        self.mp += num
        if self.mp > self.maxMP:
            self.mp = self.maxMP
        elif self.mp < 0:
            self.mp = 0
     
    def changeHP(self, num):
        self.hp += num
        if self.hp > self.maxHP:
            self.hp = self.maxHP
        elif self.hp < 0:
            self.hp = 0
    
    def getOrderedSkills(self):
        skillSet = {}
        count = 0
        for skill in self.skills.keys():
            count += 1
            skillSet[str(count)] = skill
        return skillSet
    
