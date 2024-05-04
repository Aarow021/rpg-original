#===========================MONSTER CLASS===========================#
#Monster entities are instanced off of this class

from Functions import spacing, printSeperator, awaitInput
from Character import *
from Colors import *
class Monster(Character):
    type = "Monster"


    def listHP(self):
        print("<" + self.type + "> has [" + self.display("hp") + "] HP left")
        spacing(1)

    def statSheet(self):
        print(self.image)
        printSeperator(27, "-")
        print("Type: <" + self.type + ">")
        print("HP: " + self.display("hp") + "/" + self.display("maxhp"))
        print("Power: " + self.display("power"))
        printSeperator(27, "-")
        awaitInput()
    
    #returns the damage delt to the monster. Different calculation than default character
    def defend(self, dmg):
        self.calculateStats()
        return round(dmg / (1 + (self.toughness-1)/20), 2)
    
    #Calculates the attribute stats after all of the multis
    def calculateStats(self):
        self.power = round(self.basePower * getProduct(self.powerMultis), 2)
        # self.toughness = round(self.baseToughness * getProduct(self.toughnessMultis), 2)
        self.toughness = 1
        self.maxMP = round(self.baseMaxMP * getProduct(self.mpMultis), 2)
        self.maxHP = round(self.baseMaxHP * getProduct(self.hpMultis), 2)
        self.maxStamina = round(self.baseMaxStamina * getProduct(self.staminaMultis) + getProduct(self.staminaMultis) * (math.log(3 + self.essence)/math.log(3)), 2)