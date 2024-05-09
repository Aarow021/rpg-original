#===========================PLAYER CLASS===========================#
#The player is instanced off of this class
from Functions import *
from Character import *
from Colors import *
import random
class Player(Character):
    type = "Player"
    restCountdown = 3
    restCooldown = 2
    shopCooldown = 3
    monstersKilled = 0

    
    def statsheet(self):
        self.calculateStats()
        print('''
    O
   \|/ 
    |
   / \\
              ''')
        printSeperator(30, "═")
        print("Traits: ", end="")
        for trait in self.traits.values():
            print("[" + trait.displayName() + "]", end="")
        print()
        print("HP: " + self.display("hp") + "/" + self.display("maxHP"))
        print("Stamina: " + self.display("stamina") + "/" + self.display("stamina"))
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
            skill.configure(self)
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
    
