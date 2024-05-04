#===========================TRAIT CLASS===========================#
#This is the class for Traits

from Colors import *

class Trait:
    upgradeTree = "attack"
    name = "Base Trait"
    desc = "This is a basic trait"
    hpMulti = 1
    toughnessMulti = 1
    powerMulti = 1
    mpMulti = 1
    staminaMulti = 1
    skills = []
    #What trait this one overwrites (replaces)
    overWrites = None
    def __init__(self, upgradeTree, name, hpMulti, toughnessMulti, powerMulti, mpMulti, staminaMulti, skills, desc, overWrites=None):
        self.upgradeTree = upgradeTree
        self.name = name
        self.desc = desc
        self.hpMulti = hpMulti
        self.toughnessMulti = toughnessMulti
        self.powerMulti = powerMulti
        self.mpMulti = mpMulti
        self.staminaMulti = staminaMulti
        self.skills = skills
        self.overWrites = overWrites

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
            target.skills[skill.name] = skill
    
    #Removes all the effects the trait has on its holder and deletes itself
    def removeTrait(self, player):
        for skill in self.skills:
            del player.skills[skill.name]
        del player.hpMultis[self.name]
        del player.toughnessMultis[self.name]
        del player.powerMultis[self.name]
        del player.mpMultis[self.name]
        del player.traits[self.name]
    
    #Replaces another trait of the target with itself
    def replaceTrait(self, player):
        if self.overWrites:
            removedTrait = player.traits[self.overWrites.name]
            removedTrait.removeTrait(player)

    #Called once at the creation of the trait
    def init(self, target):
        self.applyStats(target)
        self.replaceTrait(target)
        self.setSkills(target)

    #returns colored name
    def displayName(self):
        if self.upgradeTree == "power":
            return style(self.name, "purple", "bold")
        elif self.upgradeTree == "toughness":
            return style(self.name, "green", "bold")
        elif self.upgradeTree == "mp":
            return style(self.name, "blue", "bold")