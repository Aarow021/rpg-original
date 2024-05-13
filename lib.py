#===========================LIB===========================#
#Holds monster specific info (Goblin, Skeleton, ect)
#Ascii dot art assets (goblin, orc, skeleton, crown) are from https://emojicombos.com/

from Colors import *
#Monster base values
class BaseMonster:
    maxHP = 100
    power = 1
    toughness = 1
    type = "MonsterTemplate"
    image = ""

class Goblin(BaseMonster):
    maxHP = 5
    power = .70
    toughness = 1
    type = "Goblin"
    image = green('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠢⣤⣀⡀⠀⠀⠀⢿⣧⣄⡉⠻⢿⣿⣿⡿⠟⢉⣠⣼⡿⠀⠀⠀⠀⣀⣤⠔⠀
⠀⠀⠈⢻⣿⣶⠀⣷⠀⠉⠛⠿⠶⡴⢿⡿⢦⠶⠿⠛⠉⠀⣾⠀⣶⣿⡟⠁⠀⠀
⠀⠀⠀⠀⠻⣿⡆⠘⡇⠘⠷⠠⠦⠀⣾⣷⠀⠴⠄⠾⠃⢸⠃⢰⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠋⢠⣾⣥⣴⣶⣶⣆⠘⣿⣿⠃⣰⣶⣶⣦⣬⣷⡄⠙⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢋⠛⠻⠿⣿⠟⢹⣆⠸⠇⣰⡏⠻⣿⠿⠟⠛⡙⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢧⡀⠠⠄⠀⠈⠛⠀⠀⠛⠁⠀⠠⠄⢀⡼⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⡀⠃⠀⣿⡆⢰⣿⠀⠘⢀⣴⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⡀⠘⠇⠸⠃⢀⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣷⣄⣠⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

class Skeleton(BaseMonster):
    maxHP = 3
    power = 1
    toughness = .8
    type = "Skeleton"
    image = '''
  ⠀⠀⣀⠤⠔⠒⠒⠒⠒⠒⠒⠒⠦⢄⠀⠀⠀⠀⠀
⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄⠀⠀
⢀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀
⢸⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠈⡇
⢸⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⡇
⠘⡆⢸⠀⢀⣀⣤⣄⡀⠀⠀⠀⢀⣤⣤⣄⡀⠀⡇⠀⠀
⠀⠘⣾⠀⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⠀⡇⠀⠀
⠀⠀⣿⠀⠙⢿⣿⠿⠃⢠⢠⡀⠙⠿⣿⠿⠃⠀⡇⠀⠀
⠀⠀⠘⣄⡀⠀⠀⠀⢠⣿⢸⣿⠀⠀⠀⠀⠀⣠⠇⠀⠀
⠀⠀⠀⠀⡏⢷⡄⠀⠘⠟⠈⠿⠁⠀⢠⡞⡹⠁⠀⠀⠀
⠀⠀⠀⠀⢹⠸⠘⢢⢠⠤⠤⡤⡄⢰⢡⠁⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠀⠣⣹⢸⠒⠒⡗⡇⣩⠌⢀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢧⡀⠀⠉⠉⠉⠉⠁⠀⣀⠜⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠓⠢⠤⠤⠤⠔⠊⠁⠀⠀⠀⠀⠀⠀'''

class Orc(BaseMonster):
    maxHP = 5
    power = .8
    toughness = 1.5
    type = "Orc"
    image = green('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣧⣄⣉⣉⣠⣼⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣤⣤⣈⠙⠳⢄⣉⣋⡡⠞⠋⣁⣤⣤⣧⠀⠀⠀⠀⠀⠀⠀
⠀⢲⣶⣤⣄⡀⢀⣿⣄⠙⠿⣿⣦⣤⡿⢿⣤⣴⣿⠿⠋⣠⣿⠀⢀⣠⣤⣶⡖⠀
⠀⠀⠙⣿⠛⠇⢸⣿⣿⡟⠀⡄⢉⠉⢀⡀⠉⡉⢠⠀⢻⣿⣿⡇⠸⠛⣿⠋⠀⠀
⠀⠀⠀⠘⣷⠀⢸⡏⠻⣿⣤⣤⠂⣠⣿⣿⣄⠑⣤⣤⣿⠟⢹⡇⠀⣾⠃⠀⠀⠀
⠀⠀⠀⠀⠘⠀⢸⣿⡀⢀⠙⠻⢦⣌⣉⣉⣡⡴⠟⠋⡀⢀⣿⡇⠀⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣧⠈⠛⠂⠀⠉⠛⠛⠉⠀⠐⠛⠁⣼⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣏⠀⣤⡶⠖⠛⠋⠉⠉⠙⠛⠲⢶⣤⠀⣹⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣶⣿⣿⣿⣿⣿⣿⣶⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠛⠛⠉⠉⠉⠁⠀⠀⠀''')

class DarkElf(BaseMonster):
    maxHP = 4
    power = 1
    toughness = 1
    type = "Dark Elf"
    image = '''
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣾⣿⣿⣿⣿⣿⣿⣶⣦⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠰⣿⣅⣀ ⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⠍⠋⠀⠀⠨⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀ ⡀⣰⣶ 
 ⠀⠘⠻⣯⡓⢦⣤⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡿⠊⠀⠀⢀⣾⣖⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀ ⣀⡤⢟⣫⡞ ⠀
 ⠀⠀⠀⠉⢻⣶⢌⠙⠓⠶⣿⣿⣿⣿⣿⣿⣿⣿⡋⠀⠀⠀⠘⢿⣿⣿⠗⠀⠀⠀⢙⣿⣿⣿⣿⣿⣿⣿⣿⠶⠖⠊⣁⢴⣿⠏ ⠀⠀
 ⠀⠀⠀⠀ ⠻⣷⠑⠢⡀⣿⣿⣿⣿⣿⣿⡿⠻⣿⣶⣄⢀⠀⡀⠻⢡⠀⠀⣠⣴⣿⠿⠻⣿⣿⣿⣿⣿⣿⣄⡠⠞⢳⡿⠋ ⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⣻⡇⡮⠈⣿⣿⣿⣿⣿⣿⣶⣿⣾⣿⣿⣷⡄⣷⢀⣿⣀⣼⣿⣿⣿⣷⣾⣾⣿⣿⣿⣿⣿⣯⠍⢶⡿ ⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⣿⣤⠁⣿⣿⣿⣿⡿⢿⣷⡉⢿⡿⢻⣿⣿⣿⢾⣿⣿⣿⢿⣯⡿⢁⣿⣿⢻⣿⣿⣿⣿⡇⡀⣿⠇⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠋⢻⣿⣿⣿⣿⣿⡗⠘⢿⣿⣿⣿⣿⣿⣿⠋⠀⠻⣿⣿⣿⣿⣿⣿⣿⠏⠈⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⢇⠀⠈⠙⢿⡿⡟⠁⠀⠀⠀⠀⠈⠛⠿⣿⢿⡟⠁⠀⣴⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣣⡀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠀⢀⢜⣽⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣇⠑⠀⠀⠀⠀⠀⠈⠳⣲⡷⠀⠀⠀⠀⠀⢠⠊⢸⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⣀⣠⣤⣭⣢⣄⡀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠉⠀⠀⠈⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠷⣤⣀⠀⠀⠀⠀⠀⠀⠠⠊⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠱⡨⠉⠷⣖⣀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀'''

class OrcLord(BaseMonster):
    maxHP = 10
    power = 1
    toughness = 2
    type = "Orc Lord"
    image = yellow('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢿⡿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠙⣷⣾⠋⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡀⠀⠀⠀⢀⣠⣤⣌⡙⢷⣽⣧⡾⢋⣠⣤⣄⡀⠀⠀⠀⢀⠀⠀⠀⠀
⠀⠀⠀⣀⣿⢄⡤⣰⡿⠛⠉⠙⠻⣾⣿⣿⣿⠟⠋⠉⠛⢿⣆⢤⡰⡿⣀⠀⠀⠀
⠀⣠⣤⣝⣷⣼⣷⣿⠁⠀⠀⢠⡶⢿⣿⣿⡷⢶⡄⠀⠀⠈⣿⣾⣧⣾⣫⣤⣄⠀
⣼⡟⠉⣽⣿⣿⣿⡿⠛⣷⠀⠸⣧⣴⣿⣿⣶⣼⠇⠀⣾⠛⢿⣿⣿⣿⣯⠉⢻⣧
⣿⡀⠀⢿⣄⡘⢿⡇⣰⠟⢀⣴⠶⣦⣻⣿⣴⠶⣦⡀⠻⣆⢸⡿⢃⣠⡿⠀⠀⣿
⢹⣇⠀⠀⠉⠻⠞⣿⡛⠀⢿⡁⠀⠀⣿⣿⠁⠀⢈⡿⠀⢛⣿⠳⠟⠉⠀⠀⣸⡏
⠀⠻⣦⡀⠀⠀⢀⣿⣷⣄⠈⠙⢛⣽⣿⣿⣿⡛⠛⠁⣠⣾⣿⡀⠀⠀⢀⣴⠟⠀
⠀⠀⢹⣿⣶⣶⣾⣿⡿⠿⠿⠾⠿⠿⠿⠿⠿⠿⠷⠿⠿⢿⣿⣷⣶⣶⣿⡟⠀⠀
⠀⠀⠈⢩⣵⣶⣶⡇⣶⡌⢻⣿⣿⣏⠰⡷⢸⣿⣿⣿⢡⣶⢘⣶⣶⣾⡭⠁⠀⠀
⠀⠀⠀⠈⣛⣩⣭⣥⣤⣤⣭⣥⠤⠴⠤⠤⠴⠤⢬⣭⣤⣤⣬⣭⣍⣛⡃⠀⠀⠀''') + green('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣤⣤⣈⠙⠳⢄⣉⣋⡡⠞⠋⣁⣤⣤⣧⠀⠀⠀⠀⠀⠀⠀
⠀⢲⣶⣤⣄⡀⢀⣿⣄⠙⠿⣿⣦⣤⡿⢿⣤⣴⣿⠿⠋⣠⣿⠀⢀⣠⣤⣶⡖⠀
⠀⠀⠙⣿⠛⠇⢸⣿⣿⡟⠀''') + red("⡄") + green('''⢉⠉⢀⡀⠉⡉''') + red("⢠") + green(''' ⢻⣿⣿⡇⠸⠛⣿⠋⠀⠀
⠀⠀⠀⠘⣷⠀⢸⡏⠻⣿⣤⣤⠂⣠⣿⣿⣄⠑⣤⣤⣿⠟⢹⡇⠀⣾⠃⠀⠀⠀
⠀⠀⠀⠀⠘⠀⢸⣿⡀⢀⠙⠻⢦⣌⣉⣉⣡⡴⠟⠋⡀⢀⣿⡇⠀⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣧⠈⠛⠂⠀⠉⠛⠛⠉⠀⠐⠛⠁⣼⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣏⠀⣤⡶⠖⠛⠋⠉⠉⠙⠛⠲⢶⣤⠀⣹⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣶⣿⣿⣿⣿⣿⣿⣶⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠛⠛⠉⠉⠉⠁⠀⠀⠀''')