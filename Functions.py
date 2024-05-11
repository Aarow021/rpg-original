#===========================FUNCTIONS===========================#
#This File holds useful functions used in other parts of the program

import math
import functools
from decimal import *

from Colors import colorStat # type: ignore

#Custom print method
def printf(text, args=None):
    if not args:
        print(text)
    else:
        print(text, **args)

#Prints carriage return n times (for spacing between lines)
def spacing(spaceNum):
    for i in range(spaceNum):
        print()

def cls():
    spacing(100)

#Prints n characters. ex: printSeperator(10, "=") -> ==========
def printSeperator(num, seperator = "-"):
    for i in range(num):
        print(seperator, end="")
    print()

#Waits for user to input anything before continuing
def awaitInput():
    a = input()

#Makes sure user input is an intager within a given range
def readInt(message, maxInt):
    response = -1
    spacing(1)
    while response < 0 or response > maxInt:
        try:
            response = float(input(message))
        except:
            response = -1
        if response < 0 or response > maxInt:
            print("Please enter a number between 0 and " + str(maxInt))
            spacing(1)
    return response

#Prints the values in a dictionary
def printDict(dict):
    for key, value in dict.items():
        print("[Key: " + str(key) + ", Value: " + str(value) +"]", end="")

def printList(list):
    for element in list:
        print(f"[{element}]", end="")
    print()

def listToString(list):
    string = ""
    for element in list:
        string += "[" + str(element) + "] "
    return string

def listToStringColored(list):
    string = ""
    for element in list:
        string += "[" + colorStat(element, element) + "] "
    return string

#Gets the product of all elements in a list of numbers
def getProduct(list):
    if list:
        return functools.reduce(lambda a, b: a*b, list.values())
    else:
        return 1
    
#Makes sure user input meets a given condition. Valid calls are:
    #validateInput("give me a number between 2 and 9: ", "Please enter a number between 2 and 9", "float", lambda x: x if x > 2 and x < 9 else None)
    #validateInput("Tell me hello! : ", "Please tell me hi!", False, lambda x: x if x.casefold() == "hello" or x.casefold() == "hi" else None)
def validateInput(message, numberType, failMessage="Please enter a valid response", condition=lambda x:True):
    try:
        condition(0)
    except:
        print("Condition must be a function")
        return
    response = None
    validInput = False
    while not validInput:
        try:
            if numberType == "int":
                response = int(input(message))
            elif numberType == "float":
                response = float(input(message))
            else:
                response = input(message)
            print()
            if condition(response):
                validInput = True
            else: print(failMessage)
        except:
            print(failMessage)

    return response
        
        
        
        

    


        


    