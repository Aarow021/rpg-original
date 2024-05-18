#===========================MAIN CLASS===========================#
#All classes are called in this class

from Player import *
from Monster import *
from Functions import *
from Shop import Shop
from ShopItem import ShopItem
from Trait import Trait
from lib import *
from Skill import *
from Colors import *
from Potion import *
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
    spacing(100)
    print(style("At a young age, your village was destroyed by the evil Orc Lord. Now that you are of age to get your first trait, you vow to hunt down the monster and defeat him.", "cyan", "italic"))
    spacing(1)
    #initializes the player (maxHP, power, maxMP, toughness, maxStamina, essence, gold)
    player = Player(10, 1, 3, 1, 5)
    #Skill comes in format: Skill(Name, "Type", "CostType", cost, skillValue, description, CastMessage)
    punch = AttackSkill("Punch", "stamina", 1, 1, "A normal punch", "You throw a punch")
    manaBurst = AttackSkill("Mana Burst", "mp", 2, 1.5, "Shoots a burst of unrefined mana", "You shoot a burst of mana!")
    punch.bind(player)
    manaBurst.bind(player)
    starterPotions = [RecoveryPotion("Health Potion", "hp", 50, 0), RecoveryPotion("Mana Potion", "mp", 100, 0), RecoveryPotion("Stamina Potion", "stamina", 100, 0)]
    for potion in starterPotions:
        player.potions[potion.name] = potion
        potion.bind(player)

    selectTrait()
    
#Brings player to trait selection
def selectTrait():
    # powerTraits = ["Big Muscles", "Herculan Strength"]
    # toughnessTraits = ["Thick Skin", "Goliath's Fortitude"]
    # mpTraits = ["Mana Affinity", "Mana Core"]

    availableTraits = {}
    for i in range(len(player.nextTraits)):
        availableTraits[str(i+1)] = player.nextTraits[i] #availableTraits[1] = "Big Muscles"

    print("Choose your trait: \n")
    for i in range(len(availableTraits)):
        print(f"({green(i + 1)})" + str(availableTraits[str(i+1)]))
    print(f"\n({red(len(availableTraits) + 1)})None (This will handicap you and make the game harder. Good luck)")

    spacing(1)
    validInput = False
    while not validInput:
        selection = input("> ").casefold()
        if selection in availableTraits:
            selection = availableTraits[selection]
            trait = None

            if selection == "Big Muscles":
                strongPunch = AttackSkill("Strong Punch", "stamina", 2.5, 1.5, "Punch with lots of effort", "You punch with all your might!")
                trait = Trait("power", "Big Muscles", 1, 1.3, 1.3, 1, 1.2, [strongPunch], "You have very big muscles", nextTraits=["Herculan Strength"])
            elif selection == "Herculan Strength":
                strongPunch = AttackSkill("Herculan Punch", "stamina", 3, 1.75, "Punch with the might of hercules", "You punch with Hercules' strength!")
                groundStomp = AttackSkill("Meteor Strike", "stamina", 6, 2.5, "Leap high into the air and land a devistating kick onto the opponent's head", "You jump into the air and strike from above!")
                trait = Trait("power", "Herculan Strength", 1, 1.5, 2, 1, 1.4, [strongPunch, groundStomp], "Your strength is immense", overWrites="Big Muscles")


            elif selection == "Thick Skin":
                hardenSkin = BuffSkill("Harden Skin", "stamina", 3, ["toughness"], 2, 3, "Hardens your skin, increasing your toughness", "Your skin hardens.")
                trait = Trait("toughness", "Thick Skin", 1.2, 1.5, 1, 1, 1.3, [hardenSkin], "You have very tough skin", nextTraits=["Goliath's Fortitude"])

            elif selection == "Goliath's Fortitude":
                cobaltShell = BuffSkill("Cobalt Shell", "stamina", 5, ["toughness"], 3, 3, "Constructs a shell of cobalt around your body, granting supurb defence", "A shell of cobalt surrounds your body.")
                reflectiveAura = ReflectSkill("Reflective Aura", "stamina", 4, 50, "For a turn, generates an aura that reflects half of the attacker's damage", "You release a reflective aura.", 0)
                trait = Trait("toughness", "Goliath's Fortitude", 1.5, 2, 1.2, 1, 1.6, [cobaltShell, reflectiveAura], "Your fortitude is akin to Goliath", overWrites="Thick Skin")


            elif selection == "Mana Affinity":
                manaRecovery = ConvertionSkill("Mana Recovery", "stamina", "mp", 3, .7, "Recover some mana by using stamina", "You recovered some mana", 1)
                manaBullet = AttackSkill("Mana Bullet", "mp", 2, 2, "Shoots a bullet of concentrated mana", "You shoot a mana bullet!")
                trait = Trait("mp", "Mana Affinity", 1, 1, 1, 2, 1, [manaRecovery, manaBullet], "You have an affinity for magic", nextTraits=["Mana Core"])
                del player.skills["Mana Burst"]
            elif selection == "Mana Core":
                manaRecovery = ConvertionSkill("Mana Recovery", "stamina", "mp", 4, .95, "Efficiently recover some mana by using stamina", "You recovered some mana", 1)
                magicMissile = AttackSkill("Magic Missile", "mp", 2, 2.5, "Shoots a missile of concentrated mana", "You shoot a magic missile!")
                enhance = BuffSkill("Enhance", "mp", 7, ["power", "toughness"], 2, 3, "Enhances the user's body with magic, increasing their power and toughness.", "You enhance your body")
                trait = Trait("mp", "Mana Core", 1, 1, 1, 3, 1, [manaRecovery, magicMissile, enhance], "You have developed a mana core", overWrites="Mana Affinity")
            
            player.traits[selection] = trait
            trait.bind(player)
            validInput = True

        elif selection == "none" or selection == "4":
            validInput = True #No trait

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
                if skill.checkUsability() == True:
                    attackType = skill.costType
                    if skill.type == "attack":
                            dmg = monster.defend(skill.cast())
                            dmgTaken = player.defend(monster.attack())
                            nextTurn = True
                    elif skill.type == "reflect":
                            dmg = skill.cast(monster)
                            dmgTaken = player.defend(monster.attack() * (1 - skill.skillValue))
                            nextTurn = True
                    elif skill.type == "buff":
                        skill.cast(player)
                    elif skill.type == "conversion":
                        skill.cast(player)
                        nextTurn = True
                    print(skill.castMessage)
                else:
                   print(skill.checkUsability()) #Returns error message
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
    counter = 0
    print("What potion would you like to use?")

    potionList = {}
    for potion in player.potions.values():
        counter += 1
        potionList[counter] = potion
        print(f"({green(counter)}){potion.name}s: [{potion.count}]")
    print(f"({red(counter + 1)})Back")

    choice = readInt("> ", counter + 1)
    if choice in potionList:
        potion = potionList[choice]
        potion.use()
    else:
        return
    # if choice == 1:
    #     if player.potions["hp"] <= 0:
    #         print("You don't have any health potions!")
    #         return
    #     healed = round(player.maxHP / 2, 2)
    #     player.changeHP(healed)
    #     player.potions["hp"] -= 1
    #     print("you drink a health potion and regain [" + red(healed) + "] health!")


        
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
    healthCost = round(10*stage + (player.gold/4 + 1), 2)
    manaCost = round(5*stage + (player.gold/5 + 1), 2)
    staminaCost = round(3*stage + (player.gold/6 + 1), 2)
    shop = Shop()
    shop.addItem(ShopItem(RecoveryPotion("Health Potion", player, 50), healthCost, "hp", f"{red('Health')} Potion","A potion that heals you for half of your health"))
    shop.addItem(ShopItem(RecoveryPotion("Mana Potion", player, 50), manaCost, "mp", f"{blue('Mana')} Potion", description="A potion that recovers all of your mana"))
    shop.addItem(ShopItem(RecoveryPotion("Stamina Potion", player, 50), staminaCost, "stamina", f"{yellow('Stamina')} Potion", description="A potion that recovers all of your stamina"))
    spacing(100)
    print("You come apon a travelling merchant. He offers you some potions.")
    spacing(1)
    print("Gold: [" + player.display("gold") + "]")
    print("What would you like to buy? (\"exit\" to leave)")
    itemList = {}
    count = 0
    for item in shop.items.values():
        count += 1
        itemList[count] = item.name
        print(f"({green(count)})[{item.displayName}] Gold: [{yellow(item.cost)}]. {item.description}")
    print(f"({green(len(itemList) + 1)})[{red('Leave')}]")
    spacing(1)
    
    while True:
        choice = readInt("> ", len(itemList) + 1)
        spacing(1)
        if choice in itemList:
            choice = itemList[choice]
            shop.buyItem(player, choice)
        elif choice == len(itemList) + 1:
            print("The merchant waves you goodbye")
            awaitInput()
            return
        else:
            print("Please enter a valid response.")
        print("Gold: [" + player.display("gold") + "]")


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
        AttackSkill(name, costType, cost, value, desc, message).bind(player)
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
    elif selection == "change stat" or selection == "stat":
        availableStats = ["hp", "mp", "stamina", "toughness", "power", "gold", "essence"]
        def isAStat(stat):
            stat = str(stat).casefold()
            for availableStat in availableStats:
                if stat == availableStat:
                    return True
            return False #If input not in available stats
        print("Available Stats: " + listToStringColored(availableStats) + "\nWhat stat do you want to change?")
        stat = validateInput("", "string", "Please enter a valid stat", isAStat)
        print("\nWhat do you want to set the stat to?")
        value = validateInput("", "float", "Please enter a number greater than or equal to 0", lambda x: True if x >= 0 else None)
        player.changeStat(stat, value)
    elif selection == "test":
        player.gold = 100

#prints out lore based on events - Will be used more after the AP submission
def lore(key):
    if key == "stage2":
        spacing(50)
        print(style("You have reached the deep forest.", "green", "italic"))
    
def askRestart():
    validInput = False
    spacing(3)
    print(f"Do you want to restart? ([{green('Yes')}] or [{red('No')}])")
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
        spacing(4)
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
            instaKill = AttackSkill("InstaKill", "stamina", 0, 9999, "Instantly kills the enemy", "You instantly kill the enemy.")
            instaKill.bind(player)
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
randVal = random.choice(range(100))
if randVal == 0:
    for i in range(100):
        awaitInput()
    print(style("Wow, you really pressed enter 100 times! Well this is an easter egg I suppose. Take it! 🥚", "purple", "italic"))
    for i in range(10):
        awaitInput()