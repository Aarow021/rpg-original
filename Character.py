#===========================CHARACTER CLASS===========================
import random
from Colors import *
from Functions import *

#Base class for entities such as Player and Monsters
class Character:
    def __init__(self, maxHP, power, maxMP, toughness, maxStamina, essence=0, gold=0, type="Default", image = ""):
        self.baseMaxHP, self.maxHP, self.hp = maxHP, maxHP, maxHP
        self.power, self.basePower = power, power
        self.maxMP, self.baseMaxMP, self.mp = maxMP, maxMP, maxMP
        self.toughness, self.baseToughness = toughness, toughness
        self.essence = essence
        self.gold = gold
        self.maxStamina, self.stamina, self.baseMaxStamina = maxStamina, maxStamina, maxStamina
        self.type = type
        self.image = image
        self.skills = {}
        self.hpMultis = {}
        self.mpMultis = {}
        self.powerMultis = {}
        self.toughnessMultis = {}
        self.staminaMultis = {}
        self.traits = {}
        self.potions = {}

        
    #Calibrates stats with its multipliers
    #Use before doing anything with power/toughness
    def calculateStats(self):
        self.power = round(self.basePower * (1 + self.essence/10) * getProduct(self.powerMultis), 2)
        self.toughness = round(self.baseToughness * (1 + self.essence/10) * getProduct(self.toughnessMultis), 2)
        self.maxMP = round(self.baseMaxMP * getProduct(self.mpMultis) + getProduct(self.mpMultis) * (math.log(1 + self.essence)/math.log(7)), 2)
        self.maxHP = round(self.baseMaxHP * getProduct(self.hpMultis), 2)
        self.maxStamina = round(self.baseMaxStamina * getProduct(self.staminaMultis) + getProduct(self.staminaMultis) * (math.log(5 + self.essence)/math.log(5)), 2)

    #Returns calculated attack
    def attack(self):
        self.calculateStats()
        return round(self.power * random.uniform(.8, 1.2), 2)
    
    #Returns calculated damage taken
    def defend(self, dmg):
        self.calculateStats()
        return round(dmg / (math.log(1 + self.toughness) / math.log(2)), 2)
    
    #Changes the hp of the creature
    def changeHP(self, num):
        self.hp += num
        if self.hp > self.maxHP:
            self.hp = self.maxHP
        elif self.hp < 0:
            self.hp = 0
    
    #Changes the stamina of the character
    def changeStamina(self, num):
        self.stamina += num
        if self.stamina > self.maxStamina:
            self.stamina = self.maxStamina
        elif self.stamina < 0:
            self.stamina = 0
    
    #Returns the string form of the stat to be displayed. Used for color, formatting. For example, calling display("Message about mana", "mp") will return a blue version of the message
    def display(self, stat):
        stat = str(stat).lower()
        if stat == "hp":
            return style(round(self.hp, 2), "red")
        elif stat == "maxhp":
            return style(round(self.maxHP, 2), "red")
        elif stat == "mp":
            return style(round(self.mp, 2), "blue")
        elif stat == "maxmp":
            return style(round(self.maxMP, 2), "blue")
        elif stat == "essence":
            return style(round(self.essence, 2), "cyan")
        elif stat == "gold":
            return style(round(self.gold, 2), "yellow")
        elif stat == "power":
            return style(round(self.power, 2), "purple")
        elif stat == "toughness":
            return style(round(self.toughness, 2), "green")
        elif stat == "stamina":
            return style(round(self.stamina, 2), "yellow")
        elif stat == "maxstamina":
            return style(round(self.maxStamina, 2), "yellow")
        return

    #Resets all the skill cooldowns and resets buffs on creature
    def resetSkillCooldowns(self):
        for skill in self.skills.values():
            skill.cooldown = 0
            if skill.type == "buff":
                skill.deleteBuffs()

    #Changes a given stat of the character
    def changeStat(self, stat, value):
        stat = str(stat).casefold()
        match stat:
            case "hp":
                self.baseMaxHP = value
                self.hp = value
            case "mp":
                self.baseMaxMP = value
                self.mp = value
            case "stamina":
                self.baseMaxStamina = value
                self.stamina = value
            case "power":
                self.basePower = value
            case "toughness":
                self.baseToughness = value
            case "gold":
                self.gold = value
            case "essence":
                self.essence = value