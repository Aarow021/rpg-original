#===========================COLORS===========================#
#This file holds all of the color related functions

#Generates the ascii value of a color and style["Bold, italic"]
def generateColor(color, style="normal", bg="default"):
    match str(color).lower():
        case "reset":
            color = 0
        case "default":
            color = 39
        case "red":
            color = 31
        case "green":
            color = 32
        case "yellow":
            color = 33
        case "blue":
            color = 34
        case "purple":
            color = 35
        case "cyan":
            color = 36
        case "white":
            color = 37
        case _:
            color = 39
    
    match str(style).lower():
        case "default":
            style = 0
        case "bold":
            style = 1
        case "dim":
            style = 2
        case "italic":
            style = 3
        case "underline":
            style = 4
        case "strike":
            style = 9
        case _:
            style = 0

    match str(bg).lower():
        case "default":
            bg = 49
        case "black":
            bg = 40
        case "red":
            bg = 41
        case "green":
            bg = 42
        case "yellow":
            bg = 43
        case "blue":
            bg = 44
        case "purple":
            bg = 45
        case "cyan":
            bg = 46
        case "white":
            bg = 47
        case _:
            bg = 49
    fullString = "\033[" + str(color)
    if bg != 49:
        fullString += ";" + str(bg)
    if style != 0:
        fullString += ";" + str(style)
    fullString += "m"
    return fullString

#Stylizes a message with a color and optional [Bold, italic]
def style(message, color, style="None"):
    return generateColor(color, style) + str(message) + "\033[0m"

#Only colors a message
def color(message, colorCode):
    return colorCode + str(message) + "\033[0m"

#Returns the message with the color related to that stat
def colorStat(value, stat):
    stat = str(stat).lower()
    if stat == "hp" or stat == "health" or stat == "maxhp":
        return style(value, "red")
    elif stat == "mp" or stat == "mana" or stat == "maxmp":
        return style(value, "blue")
    elif stat == "essence":
        return style(value, "cyan")
    elif stat == "gold":
        return style(value, "yellow")
    elif stat == "power":
        return style(value, "purple")
    elif stat == "toughness":
        return style(value, "green")
    elif stat == "stamina" or stat == "stm":
        return style(value, "yellow")
    return str(value)

#These functions return the message in a specific color
def green(message):
    return style(message, "green")

def yellow(message):
    return style(message, "yellow")

def blue(message):
    return style(message, "blue", "bold")

def cyan(message):
    return style(message, "cyan")

def red(message):
    return style(message, "red")

def purple(message):
    return style(message, "purple")
