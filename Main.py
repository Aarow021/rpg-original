#===========================MAIN CLASS===========================#
#All classes are called in this class

from Player import *
from Monster import *
from Functions import *
from Trait import Trait
from lib import *
from Skill import *
from Colors import *
import time
import random
from math import floor
import os

stage = 1
isGameLoop = True
isDev = False
player = Player(1, 1, 1, 1, 1)
availableCommands = []
encounters = {1: ["battle", "battle", "battle", "shop", "rest"], 2: ["battle", "battle", "battle", "shop", "rest"], 3: ["battle"]}
devCommands = ["Heal", "Skill", "Devcmds", "Shop", "Rest", "Change Stat"]

if os.name == 'nt':
    os.system('') # enables ansi characters in Windows terminal

#Initializes the player
def init():
    global player, isGameLoop, stage
    isGameLoop = True
    stage = 1
    player = None
    spacing(100)
    print(style("At a young age, your village was destroyed by the evil Orc Lord. Now that you are of age to get your first trait, you vow to hunt down the monster and defeat him.", "cyan", "italic"))
    spacing(1)
    #initializes the player (maxHP, power, maxMP, toughness, maxStamina, essence, gold, type)
    player = Player(10, 1, 3, 1, 5, 0, 0, "Player")
    #Skill comes in format: Skill(Name, "Type", "CostType", cost, skillValue, description, CastMessage)
    player.skills["Punch"] = Skill("Punch", "attack", "stamina", 1, 1, "A normal punch", "You throw a punch")
    player.skills["Mana Burst"] = Skill("Mana Burst", "attack", "mp", 2, 1.5, "Shoots a burst of unrefined mana", "You shoot a burst of mana!")

    selectTrait()
    
#Brings player to trait selection
def selectTrait():
    powerTraits = ["Big Muscles", "Herculan Strength"]
    toughnessTraits = ["Thick Skin", "Goliath's Fortitude"]
    mpTraits = ["Mana Affinity", "Mana Core"]
    powerTrait = [trait for trait in player.traits if trait in powerTraits]
    toughnessTrait = [trait for trait in player.traits if trait in toughnessTraits]
    mpTrait = [trait for trait in player.traits if trait in mpTraits]
    
    try:
        powerTrait = powerTraits[powerTraits.index(powerTrait[0]) + 1] if powerTrait else powerTraits[0]
        toughnessTrait = toughnessTraits[toughnessTraits.index(toughnessTrait[0]) + 1] if toughnessTrait else toughnessTraits[0]
        mpTrait = mpTraits[mpTraits.index(mpTrait[0]) + 1] if mpTrait else mpTraits[0]
    except:
        print(red("AN ERROR HAS OCCURED. You have probably reached the end of one of the upgrade lines"))
    print("Choose your trait: \n")
    print(f"({green(1)})" + str(powerTrait))
    print(f"({green(2)})" + str(toughnessTrait))
    print(f"({green(3)})" + str(mpTrait))
    spacing(1)
    validInput = False
    while not validInput:
        selection = input("> ").casefold()
        trait = None
        if selection == powerTrait.casefold() or selection == "1":
            if powerTrait == powerTraits[0]:
                strongPunch = Skill("Strong Punch", "attack", "stamina", 2.5, 1.5, "Punch with lots of effort", "You punch with all your might!")
                trait = Trait("power", powerTrait, 1, 1.35, 1.5, 1, 1.2, [strongPunch], "You have very big muscles")
            elif powerTrait == powerTraits[1]:
                strongPunch = Skill("Herculan Punch", "attack", "stamina", 3, 2, "Punch with the might of hercules", "You punch with Hercules' strength!")
                groundStomp = Skill("Meteor Strike", "attack", "stamina", 6, 3, "Leap high into the air and land a devistating kick onto the opponent's head", "You jump into the air and strike from above!")
                trait = Trait("power", powerTrait, 1, 1.4, 2.5, 1, 1.4, [strongPunch, groundStomp], "Your strength is immense", player.traits["Big Muscles"])
            player.traits[powerTrait] = trait
            trait.init(player)
            validInput = True

        elif selection == toughnessTrait.casefold() or selection == "2":
            if toughnessTrait == toughnessTraits[0]:
                hardenSkin = BuffSkill("Harden Skin", "stamina", 3, ["toughness"], 2, 3, "Hardens your skin, increasing your toughness", "Your skin hardens.")
                trait = Trait("toughness", toughnessTrait, 1.2, 1.5, 1, 1, 1.3, [hardenSkin], "You have very tough skin")

            elif toughnessTrait == toughnessTraits[1]:
                cobaltShell = BuffSkill("Cobalt Shell", "stamina", 5, ["toughness"], 3, 3, "Constructs a shell of cobalt around your body, granting supurb defence", "A shell of cobalt surrounds your body.")
                reflectiveAura = Skill("Reflective Aura", "attack", "stamina", 4, .5, "For a turn, generates an aura that reflects half of the attacker's damage", "You release a reflective aura.", 0, ["reflect"])
                trait = Trait("toughness", toughnessTrait, 1.5, 2, 1.2, 1, 1.6, [cobaltShell, reflectiveAura], "Your fortitude is akin to Goliath", player.traits["Thick Skin"])
            player.traits[toughnessTrait] = trait
            trait.init(player)
            validInput = True
        
        elif selection == mpTrait.casefold() or selection == "3":
            if mpTrait == mpTraits[0]:
                manaRecovery = ConvertionSkill("Mana Recovery", "stamina", "mp", 3, .7, "Recover some mana by using stamina", "You recovered some mana", 1)
                manaBullet = Skill("Mana Bullet", "attack", "mp", 2, 2, "Shoots a bullet of concentrated mana", "You shoot a mana bullet!")
                trait = Trait("mp", mpTrait, 1, 1, 1, 2, 1, [manaRecovery, manaBullet], "You have an affinity for magic")
                del player.skills["Mana Burst"]
            elif mpTrait == mpTraits[1]:
                manaRecovery = ConvertionSkill("Mana Recovery", "stamina", "mp", 4, .95, "Efficiently recover some mana by using stamina", "You recovered some mana", 1)
                magicMissile = Skill("Magic Missile", "attack", "mp", 2, 2.5, "Shoots a missile of concentrated mana", "You shoot a magic missile!")
                enhance = BuffSkill("Enhance", "mp", 7, ["power", "toughness"], 2, 3, "Enhances the user's body with magic, increasing their power and toughness.", "You enhance your body")
                trait = Trait("mp", mpTrait, 1, 1, 1, 3, 1, [manaRecovery, magicMissile, enhance], "You have developed a mana core", player.traits["Mana Affinity"])
            player.traits[mpTrait] = trait
            trait.init(player)
            validInput = True

        if not validInput:
            print("Please select a valid trait")
    player.calculateStats()
    player.hp = player.maxHP
    player.mp = player.maxMP
    player.stamina = player.maxStamina

    
#Lists currently available commands
def listCommands(commands):
    print("Commands: ", end="")
    for command in commands:
        print("[" + str(command) + "]", end=" ")
    print()


#Generates a monster based on current stage
#CREATEMONSTER---------------------------------------------------------------------------------------------------------
def createMonster(stage):
    chosenMonster = BaseMonster()
    essence = round(random.uniform(.75, 1.5), 2)
    chosenMonster = random.choice([Goblin(), Skeleton()])

    if stage == 1:
        essence = round((player.essence / 100) + random.uniform(.8, 1.4), 2)
        chosenMonster = random.choice([Goblin(), Skeleton()])
    elif stage == 2:
        essence = round((player.essence / 100) + random.uniform(2, 3), 2)
        chosenMonster = random.choice([Orc(), DarkElf()])
    elif stage == 3:
        essence = round((player.essence / 100) + random.uniform(5, 5), 2)
        chosenMonster = OrcLord()

    hp, power, toughness = chosenMonster.maxHP, chosenMonster.power, chosenMonster.toughness
    mana = 1
    stamina = 10
    gold = round(essence * 3 * random.uniform(.75, 1.5), 2)
    monster = Monster(*[round(stat * essence, 2) for stat in [hp, power, mana, toughness, stamina]], essence, gold, style(chosenMonster.type, "cyan"), chosenMonster.image) # type: ignore
    monster.calculateStats()
    monster.hp = monster.maxHP
    return  monster

#Random encounter decided here
#JOURNEY---------------------------------------------------------------------------------------------------------  
def journey():
    global stage, encounters
    spacing(100)
    encounterType = None
    if player.restCountdown <= 0:
        encounterType = "rest"
    else:
        encounterType = random.choice(encounters[stage])
        for i in range(5): #TODO FIX THIS (if shop  on cd and rerolls to rest, skips rest cd)
            if player.restCooldown > 0:
                while encounterType == "rest":
                    encounterType = random.choice(encounters[stage])
            if player.shopCooldown > 0:
                while encounterType == "shop":
                    encounterType = random.choice(encounters[stage])
    if encounterType == "battle":
        player.restCountdown -= 1
        player.restCooldown -= 1
        player.shopCooldown -= 1
        if stage == 3:
            print(style("You enter the cave of the Orc Lord", "green", "italic"))
        battle()
    elif encounterType == "rest":
        player.restCooldown = 2
        player.restCountdown = 5
        rest()
    elif encounterType == "shop":
        player.shopCooldown = 2
        shop()
    

#Main fight sequence - Full battle takes place here
#BATTLE---------------------------------------------------------------------------------------------------------
def battle():
    global stage, player, availableCommands, isGameLoop
    monster = createMonster(stage)
    print("You have encountered a <" + monster.type + ">.")
    spacing(2)
    while monster.hp > 0 and player.hp > 0:
        dmg = 0
        dmgTaken = player.defend(monster.attack())
        nextTurn = False #Determines if enemy attacks
        attackType = None
        availableCommands = ["(" + green(1) + ")Skills", "(" + green(2) + ")Inspect", "(" + green(3) + ")Potion", "(" + green(4) + ")Recover", "(" + green(5) + ")Flee"]
        printSeperator(75)
        print("HP: [" + player.display("hp") + "]  MP: [" + player.display("mp") + "]  STM: [" + player.display("stamina") + "]")
        listCommands(availableCommands)
        action = input("> ").casefold()
        spacing(50)
        alwaysAvailableCommands(action)
        if action == "skills" or action == "1":
            player.displaySkills()
            action = input("> ").casefold()
            skillKeys = [*[skill for skill in player.skills], *[skill for skill in player.getOrderedSkills()]]
            if action in skillKeys:
                skill = None
                if action in player.getOrderedSkills().keys():
                    skill = player.skills[player.getOrderedSkills()[action]]
                else:
                    skill = player.skills[action]           
                if skill.checkUsability(player) == True:
                    attackType = skill.costType
                    if skill.type == "attack":
                        if "reflect" in skill.mods:
                            dmg = skill.cast(player, monster)
                            dmgTaken = player.defend(monster.attack() * skill.skillValue)
                        else:
                            dmg = monster.defend(skill.cast(player))
                            dmgTaken = player.defend(monster.attack())
                        nextTurn = True

                    elif skill.type == "buff":
                        skill.cast(player, player)
                    elif skill.type == "conversion":
                        skill.cast(player)
                        nextTurn = True
                    print(skill.castMessage)
                else:
                   print(skill.checkUsability(player)) #Returns error message
            else:
                print("Invalid skill")
        elif action == "inspect" or action == "2":
            monster.statSheet()
        elif action == "potion" or action == "3":
            selectPotion()
        elif action == "recover" or action == "4":
            stmRecovery = player.maxStamina / 3
            print("You catch your breath and regain [" + yellow(round(stmRecovery, 2)) + "] stamina")
            player.changeStamina(stmRecovery)
            dmg = 0
            dmgTaken = player.defend(monster.attack())
            nextTurn = True
        elif action == "flee" or action == "5":
            roll = random.random()
            if roll > .3:
                print("You failed to run away")
                dmg = 0
                dmgTaken = player.defend(monster.attack())
                nextTurn = True
            else:
                print("You successfully escape!")
                player.resetSkillCooldowns()
                awaitInput()
                return
        if nextTurn:
            fight(monster, dmg, dmgTaken, attackType)

        spacing(2)

        #Player death
        if player.hp <= 0:
            spacing(2)
            print(style("You have been slain.", "red", "bold"))
            print("Monsters killed: [" + style(player.monstersKilled, "purple", "bold") + "]")
            player.statsheet()
            isGameLoop = False
            return
        #Monster death
        if monster.hp <= 0:
            spacing(2)
            print("The <" + monster.type + "> has been slain.")
            print("You have absorbed [" + cyan(monster.essence) + "] essence from the <" + monster.type + ">.")
            print("The <" + monster.type + "> dropped [" + yellow(monster.gold) + "] gold!")
            player.essence += monster.essence
            player.gold += monster.gold
            player.changeStamina(player.maxStamina / 4)
            player.changeHP(player.maxHP / 10)
            player.monstersKilled += 1
            player.resetSkillCooldowns()

            #Stage up
            if stage == 1 and player.essence >= 10:
                awaitInput()
                spacing(50)
                print(style("You feel the essence inside of you pulse", "cyan", "bold"))
                spacing(1)
                selectTrait()
                lore("stage2")
                stage += 1
            elif stage == 2 and player.essence >= 30:
                awaitInput()
                spacing(50)
                print(style("The cave of the Orc Lord is in sight", "green", "italic"))
                spacing(1)
                stage += 1
                # awaitInput()
            elif stage == 3:
                print(style("You have defeated the Orc Lord, avenging your village", "purple", "bold"))
                player.statsheet()
                isGameLoop = False
            awaitInput()
            return
        

#The actual damaging of player and monster occurs here
#FIGHT---------------------------------------------------------------------------------------------------------
def fight(monster, dmg, dmgTaken, attackType):
    global player

    spacing(1)
    if dmg > 0:
        print("You damage the <" + monster.type + "> for [" + red(dmg) + "] damage!")
        monster.changeHP(-dmg)
        

    print("The <" + monster.type + "> attacks you for [" + red(dmgTaken) + "] damage!")
    player.changeHP(-dmgTaken)

    monster.listHP()
    player.changeMP(.5) if attackType != "mp" else None
    player.changeStamina(player.maxStamina / 10) if attackType != "stamina" else None
    for skill in player.skills.values():
        skill.tick()
    # awaitInput()

        
#Player selects a potion to drink - if they have any
def selectPotion():
    hpKeyWords = ["1", "hp", "health", "health potion", "health pot"]
    mpKeyWords = ["2", "mp", "mana", "mana potion", "mana pot"]

    print("Health Potions: [" + red(player.potions["hp"]) + "]")
    print("Mana Potions: [" + blue(player.potions["mp"]) + "]")
    print("What potion would you like to use?")
    choice = input("> ").casefold()
    if choice in hpKeyWords:
        if player.potions["hp"] <= 0:
            print("You don't have any health potions!")
            return
        healed = round(player.maxHP / 2, 2)
        player.changeHP(healed)
        player.potions["hp"] -= 1
        print("you drink a health potion and regain [" + red(healed) + "] health!")
    elif choice in mpKeyWords:
        if player.potions["mp"] <= 0:
            print("You don't have any mana potions!")
            return
        recovered = round(player.maxMP, 2)
        player.changeMP(recovered)
        player.potions["mp"] -= 1
        print("you drink a mana potion and regain [" + blue(recovered) + "] mana!")
        
#Player regains stamina, health, and mana
#REST----------------------------------------------------------------------------------------------------------
def rest():
    global player
    originalHP = player.hp
    healed = player.maxHP - player.hp
    if originalHP + healed > player.maxHP:
        healed = originalHP - player.maxHP
    mpRecovered = player.maxMP - player.mp
    stmRecovered = player.maxStamina - player.stamina
    player.changeHP(healed)
    player.changeMP(mpRecovered)
    player.changeStamina(stmRecovered)
    print(f"You found a nice spot to take a rest. You regained [{red(round(healed, 2))}] HP, [{blue(round(mpRecovered, 2))}]MP, and [{yellow(round(stmRecovered, 2))}] Stamina")
    awaitInput()

#Player can buy potions here
def shop():
    shopping = True
    hpKeyWords = ["1", "hp", "health", "health potion", "health pot"]
    mpKeyWords = ["2", "mp", "mana", "mana potion", "mana pot"]
    healthCost = round(10*stage + (player.gold/5 + 1), 2) # type: ignore
    manaCost = round(10*stage + (player.gold/5 + 1), 2) # type: ignore
    spacing(100)
    print("You come apon a travelling merchant. He offers you some potions.")
    spacing(1)
    print("Gold: [" + player.display("gold") + "]")
    print("What would you like to buy? (\"exit\" to leave)")
    print(f"({green(1)})[" + red("Health") + " Potion]: " + yellow(healthCost) + " Gold")
    print(f"({green(2)})[" + blue("Mana") + " Potion]: " + yellow(manaCost) + " Gold")
    spacing(1)
    
    while shopping:
        choice = input("> ").casefold()
        spacing(1)
        if choice in hpKeyWords:
            if player.gold >= healthCost:
                print("You buy a [health potion]")
                print("The merchant smiles and waves you goodbye")
                player.potions["hp"] += 1
                shopping = False
            else:
                print("You dont have enough gold to buy this")
            
        elif choice in mpKeyWords:
            if player.gold >= manaCost:
                print("You buy a [mana potion]")
                print("The merchant smiles and waves you goodbye")
                player.potions["hp"] += 1
                shopping = False
            else:
                print("You dont have enough gold to buy this")
        elif choice == "exit":
            print("The merchant waves you goodbye")
            awaitInput()
            return
        else:
            print("Please enter a valid response. (\"exit\" to leave)")
    awaitInput()

#commands that is always able to be called
def alwaysAvailableCommands(input):
    if input == "stats":
        player.statsheet()
    if isDev:
        selectDevCommand(input)

#Dev commands
def selectDevCommand(selection):
    if selection == "heal":
        print("Healed")
        player.hp = player.maxHP
    elif selection == "skill":
        #Skill comes in format: Skill(Name, "Type", "CostType", cost, skillValue, description, CastMessage)
        print("Welcome to the skill maker!")
        name = input("Please enter your skill name: ")
        costType = input("Please enter the cost type of skill (mp, stamina): ")
        cost = readInt("Enter the cost of your skill: ", float("inf"))
        value = readInt("Enter the damage multiplier of your skill: ", float("inf"))
        desc = input("Please enter your skill's description: ")
        message = input("Please enter your skill's cast Message: ")
        player.skills[name] = Skill(name, "attack", costType, cost, value, desc, message)
    elif selection == "devcmds":
        listCommands(devCommands)
    elif selection == "shop":
        shop()
    elif selection == "rest":
        rest()
    elif selection == "essence":
        try:
            essence = int(input("How much essence do you want?"))
            player.essence += essence
        except:
            print("Invalid input")
    elif selection == "change stat":
        availableStats = ["hp", "mp", "stamina", "toughness", "power", "gold", "essence"]
        def isAStat(stat):
            stat = str(stat).casefold()
            for availableStat in availableStats:
                if stat == availableStat:
                    return True
            return False #If input not in available stats
        print("Available Stats: " + listToString(availableStats) + "\nWhat stat do you want to change?")
        stat = validateInput("", "string", "Please enter a valid stat", isAStat)
        print("\nWhat do you want to set the stat to?")
        value = validateInput("", "float", "Please enter a number greater than or equal to 0", lambda x: True if x >= 0 else None)
        player.changeStat(stat, value)
    elif selection == "test":
        print("Nothing in test for now")

#prints out lore based on events - Will be used more after the AP submission
def lore(key):
    if key == "stage2":
        spacing(50)
        print(style("You have reached the deep forest.", "green", "italic"))
    
def askRestart():
    validInput = False
    spacing(3)
    print(f"Do you want to restart? ([{green("Yes")}] or [{red("No")}])")
    while validInput == False:
        choice = input().casefold()
        spacing(1)
        if choice == "yes" or choice == "y":
            return True
        elif choice == "no" or choice == "n":
            return False
        else:
            print("Please enter a valid answer.")

#The main game controller (Main Menu)
def gameLoop():
    global isDev, availableCommands, player, devCommands, isGameLoop
    init()
    spacing(100)
    while isGameLoop:
        spacing(10)
        availableCommands = [f"({green(1)})Journey", f"({green(2)})Stats"]
        listCommands(availableCommands)
        selection = input("Please select an option: ").casefold()
        spacing(2)
        if selection == "stats" or selection == "2":
            player.statsheet()
        elif selection == "commands" or selection == "3":
            listCommands(availableCommands)
        elif selection == "journey" or selection == "1":
            journey()
        
        if selection == "dev" and not isDev:
            isDev = True
            print("Dev mode activated")
            listCommands(devCommands)
            player.skills["InstaKill"] = Skill("InstaKill", "attack", "stamina", 0, 9999, "Instantly kills the enemy", "You instantly kill the enemy.")
            # player.skills["Gimme Gimme Gimme Stamina"] = Skill("Gimme Gimme Gimme Stamina", "attack", "stamina", -9999999999999999, 0, "Gimme the stamina!", "Alright, here you go.")
            # player.skills["Gimme Gimme Gimme Mana"] = Skill("Gimme Gimme Gimme Mana", "attack", "mp", -9999999999999999, 0, "Gimme the mana!", "Alright, here you go.") 
        if isDev:
            selectDevCommand(selection)
    
        

#|~---------------------------------Main----------------------------------~|#
gameLoop()
while askRestart():
    isGameLoop = True
    stage = 1
    gameLoop()

spacing(2)
print("Goodbye")
for i in range(100):
    awaitInput()
print(style("Wow, you really pressed enter 100 times! Well this is an easter egg I suppose. Take it! 🥚", "purple", "italic"))
for i in range(10):
    awaitInput()