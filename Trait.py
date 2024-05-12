#===========================TRAIT CLASS===========================#
#This is the class for Traits

from Colors import *

class Trait:  
    overWrites = None
    def __init__(self, upgradeTree, name, hpMulti, toughnessMulti, powerMulti, mpMulti, staminaMulti, skills, desc, overWrites=None, nextTraits=[]):
        self.upgradeTree = upgradeTree #Type of trait. ex: Power, Toughness, Mana
        self.name = name
        self.desc = desc
        self.hpMulti = hpMulti
        self.toughnessMulti = toughnessMulti
        self.powerMulti = powerMulti
        self.mpMulti = mpMulti
        self.staminaMulti = staminaMulti
        self.skills = skills
        self.overWrites = overWrites #What trait this one overwrites (replaces)
        self.holder = None #What character holds this trait. Initialized in bind()
        self.nextTraits = nextTraits #Next traits in the path; Traits that this unlocks. Ex: mana affinity -> mana core

    #Applies the stat bonuses to the holder of the trait
    def applyStats(self, target):
        target.hpMultis[self.name] = self.hpMulti
        target.toughnessMultis[self.name] = self.toughnessMulti
        target.powerMultis[self.name] = self.powerMulti
        target.mpMultis[self.name] = self.mpMulti
        target.staminaMultis[self.name] = self.staminaMulti
    
    #Applies the trait's skills to the target
    def setSkills(self, target):
        for skill in self.skills:
            skill.bind(target)
    
    #Removes all the effects the trait has on its holder and deletes itself
    def removeTrait(self, player):
        for skill in self.skills:
            del player.skills[skill.name]
        del player.hpMultis[self.name]
        del player.toughnessMultis[self.name]
        del player.powerMultis[self.name]
        del player.mpMultis[self.name]
        for nextTrait in self.nextTraits:
            try:
                del player.nextTraits[player.nextTraits.index(nextTrait)]
            except:
                print("Attempted to remove nextTrait that character does not have")

        del player.traits[self.name]
    
    #Replaces another trait of the target with itself
    def replaceTrait(self, player):
        if self.overWrites and self.overWrites in player.traits:
            try:
                removedTrait = player.traits[self.overWrites]
                removedTrait.removeTrait(player)
            except:
                pass #Player does not have trait that is getting removed

    #Called once at the creation of the trait
    def bind(self, target):
        self.holder = target
        self.applyStats(target)
        self.replaceTrait(target)
        self.setSkills(target)
        if self.name in target.nextTraits:
            del target.nextTraits[target.nextTraits.index(self.name)]
        for trait in self.nextTraits:
            target.nextTraits.append(trait)

    #returns colored name
    def displayName(self):
        if self.upgradeTree == "power":
            return style(self.name, "purple", "bold")
        elif self.upgradeTree == "toughness":
            return style(self.name, "green", "bold")
        elif self.upgradeTree == "mp":
            return style(self.name, "blue", "bold")