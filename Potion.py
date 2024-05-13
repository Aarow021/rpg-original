
#Base potion class. Does nothing on it's own, use child classes for effects
from Colors import colorStat


class Potion:
    def __init__(self, name, count=1):
        self.name = name
        self.count = count
        self.holder = None
        
    def use(self):
        if self.count <= 0:
            print(f'You do not have any {self.name}s')
            return -1
        self.holder.potions[self.name].count -= 1
    
    def bind(self, holder):
        self.holder = holder
        if holder.potions[self.name]:
            holder.potions[self.name].gain(self.count)
        else:
            holder.potions[self.name] = self

    def gain(self, amount):
        self.count += amount


#Recovers a resource(mp, hp, stamina) of user
class RecoveryPotion(Potion):
    def __init__(self, name, recoverType, recoverAmount=100, count=1):
        super().__init__(name, count=count)
        availableRecoverTypes = ["hp", "mp", "stamina"]
        if recoverType not in availableRecoverTypes:
            print("Invalid recovery type: " + str(recoverType))
            recoverType = "mp"
        self.recoverType = recoverType #mp, hp, stamina
        self.recoverAmount = recoverAmount #Percentage of max

    def use(self):
        if self.count <= 0:
            print(f'You do not have any {self.name}s')
            return -1
        self.holder.potions[self.name].count -= 1
        holderMaxResources = {"hp": self.holder.maxHP, "mp": self.holder.maxMP, "stamina": self.holder.maxStamina}
        holderCurrentResources = {"hp": self.holder.hp, "mp": self.holder.mp, "stamina": self.holder.stamina}
        holderMax = holderMaxResources[self.recoverType]
        holderCurrent = holderCurrentResources[self.recoverType]

        #Makes sure that recovered is the actual amount recovered. ex: hp = 5, maxHP = 10, recoveredAmount = 7;
        #Instead of recovered = 7, recovered = 5 because only 5 hp was effectively recovered
        recovered = (self.recoverAmount/100) * holderMax
        if holderCurrent + recovered > holderMax:
            recovered = holderMax - holderCurrent

        #Recover resource
        if self.recoverType == "hp":
            self.holder.changeHP(recovered)
        elif self.recoverType == "mp":
            self.holder.changeMP(recovered)
        elif self.recoverType == "stamina":
            self.holder.changeStamina(recovered)
        
        print(f"Recovered [{colorStat(round(recovered, 2), self.recoverType)}] {self.recoverType}")