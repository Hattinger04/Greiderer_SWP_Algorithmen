import os
from enum import Enum

# TODO: Bei back/quit Menue anzeigen!

# Classes

class ConsoleColors:
    OKGREEN = '\033[92m'
    OKCYAN = '\033[96m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    OPTIONS = '\u001b[37m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Status(Enum): 
    No = 0
    Yes = 1
    WrongInput = 2
    Exit = 3
    
# Big strings and global members

variablen = {}
zwischenvariable = ""
willSafe = False

calculatorString = """
  ______     ___       __        ______  __    __   __          ___   .___________.  ______   .______      
 /      |   /   \     |  |      /      ||  |  |  | |  |        /   \  |           | /  __  \  |   _  \     
|  ,----'  /  ^  \    |  |     |  ,----'|  |  |  | |  |       /  ^  \ `---|  |----`|  |  |  | |  |_)  |    
|  |      /  /_\  \   |  |     |  |     |  |  |  | |  |      /  /_\  \    |  |     |  |  |  | |      /     
|  `----./  _____  \  |  `----.|  `----.|  `--'  | |  `----./  _____  \   |  |     |  `--'  | |  |\  \----.
 \______/__/     \__\ |_______| \______| \______/  |_______/__/     \__\  |__|      \______/  | _| `._____|
                                                                                                           """


searchString = """
     _______. _______     ___      .______        ______  __    __  
    /       ||   ____|   /   \     |   _  \      /      ||  |  |  | 
   |   (----`|  |__     /  ^  \    |  |_)  |    |  ,----'|  |__|  | 
    \   \    |   __|   /  /_\  \   |      /     |  |     |   __   | 
.----)   |   |  |____ /  _____  \  |  |\  \----.|  `----.|  |  |  | 
|_______/    |_______/__/     \__\ | _| `._____| \______||__|  |__| 
                                                                    """


sortString = """
     _______.  ______   .______     .___________.
    /       | /  __  \  |   _  \    |           |
   |   (----`|  |  |  | |  |_)  |   `---|  |----`
    \   \    |  |  |  | |      /        |  |     
.----)   |   |  `--'  | |  |\  \----.   |  |     
|_______/     \______/  | _| `._____|   |__|     
                                                 """

nameString = """
.___  ___.      ___   .___________. __    __  .___________.  ______     ______    __      
|   \/   |     /   \  |           ||  |  |  | |           | /  __  \   /  __  \  |  |     
|  \  /  |    /  ^  \ `---|  |----`|  |__|  | `---|  |----`|  |  |  | |  |  |  | |  |     
|  |\/|  |   /  /_\  \    |  |     |   __   |     |  |     |  |  |  | |  |  |  | |  |     
|  |  |  |  /  _____  \   |  |     |  |  |  |     |  |     |  `--'  | |  `--'  | |  `----.
|__|  |__| /__/     \__\  |__|     |__|  |__|     |__|      \______/   \______/  |_______|
                                                                                          """

kombinatorikString = """ 
 __  ___   ______   .___  ___. .______    __  .__   __.      ___   .___________.  ______   .______       __   __  ___ 
|  |/  /  /  __  \  |   \/   | |   _  \  |  | |  \ |  |     /   \  |           | /  __  \  |   _  \     |  | |  |/  / 
|  '  /  |  |  |  | |  \  /  | |  |_)  | |  | |   \|  |    /  ^  \ `---|  |----`|  |  |  | |  |_)  |    |  | |  '  /  
|    <   |  |  |  | |  |\/|  | |   _  <  |  | |  . `  |   /  /_\  \    |  |     |  |  |  | |      /     |  | |    <   
|  .  \  |  `--'  | |  |  |  | |  |_)  | |  | |  |\   |  /  _____  \   |  |     |  `--'  | |  |\  \----.|  | |  .  \  
|__|\__\  \______/  |__|  |__| |______/  |__| |__| \__| /__/     \__\  |__|      \______/  | _| `._____||__| |__|\__\ 
                                                                                                                      """

optionsString = "Options: "

# Help Menues

def menuehelp(): 
    print()
    print(ConsoleColors.WARNING + "HELP: ")
    print()
    print(ConsoleColors.OKBLUE)

def calculatorhelp(): 
    print()
    print(ConsoleColors.WARNING + "HELP: ")
    print()
    print(ConsoleColors.OKGREEN)

def calculationhelp(): 
    print()
    print(ConsoleColors.WARNING + "HELP: ")
    print()
    print(ConsoleColors.OKGREEN)

# Options Menues

def menueoptions(): 
    print()
    print(ConsoleColors.OPTIONS + optionsString)
    print("1: Calculator")
    print("2: Sort a list")
    print("3: Search value from a list")
    print(ConsoleColors.OKBLUE)

def calcoptions(): 
    print()
    print(ConsoleColors.OPTIONS + optionsString)
    print("1: Calc ")
    print("2: Kombinatorik")
    print("3: Fibonacci")
    print(ConsoleColors.OKGREEN)

# Functions

def binarysearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = round((left + right) / 2)
        if arr[middle] == target:
            return True
        elif target > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return False

def selectionsort(arr): 
    maximal = len(arr)
    index = 0
    while index < maximal: 
        minimal = index
        for i in range(index + 1, maximal):
            if arr[i] < arr[minimal]:
                minimal = i
        arr[minimal], arr[index] = arr[index], arr[minimal]
        index = index + 1
    return arr

def fibonaccireihe(target):
    last = 1
    current = 0
    for i in range(0, target): 
        current, last = current + last, current
    return current

def hochfunktion(product, basis, exponent):
    if exponent == 0:
        return product
    return hochfunktion(product * basis, basis, exponent - 1)

def fakultaet(product, base):
    if base <= 1:
        return product
    return fakultaet(product * base, base - 1)

def calculator(): 
    while True: 
        stringrechnung = input("Geben sie bitte nun ihre Rechnung an oder schreiben sie " \
        + ConsoleColors.WARNING + "help/-h " + ConsoleColors.OKGREEN + "für eine Hilfestellung:\n## ") 
        if stringrechnung.startswith("exit") or stringrechnung.startswith("back") or stringrechnung.startswith("quit"): 
            return
        if stringrechnung.startswith("help") or (stringrechnung.startswith("-h") and len(stringrechnung) <= 3): 
            print(calculationhelp())
            continue
        try: 
            stringrechnung = searchVariable(stringrechnung)
            stringrechnung = searchSafe(stringrechnung, "->")
            stringrechnung = searchFaku(stringrechnung, "!")
            ergebnis = str(eval(stringrechnung))
            print(ConsoleColors.WARNING + "Ihr Ergebnis lautet: " + ConsoleColors.BOLD + ConsoleColors.UNDERLINE + ergebnis + ConsoleColors.ENDC + ConsoleColors.OKGREEN)
            makeSafe(ergebnis, "->")
        except: 
            print(ConsoleColors.FAIL + "Konnte nicht berechnet werden, versuche es erneut!" + ConsoleColors.OKGREEN)

def console(command):  
    os.system(command)

# Main Menue + Checks

def menue(): 
    print(ConsoleColors.OKBLUE + nameString)
    print()
    print(optionsString)
    print("1: Calculator")
    print("2: Sort a list")
    print("3: Search value from a list")

    while(True):
        if not checkvalue(input(">> ")): 
            return 

def checkvalue(userinput):
    if((userinput.startswith('1') and len(userinput) <= 2)  or userinput.startswith("calc")): 
        menuecalculator()
    elif((userinput.startswith('2') and len(userinput) <= 2) or userinput.startswith("sort")): 
        menuesortlist()
    elif((userinput.startswith('3') and len(userinput) <= 2) or userinput.startswith("search") or userinput.startswith("suchen")): 
        menuesearchlist()
    elif(userinput.startswith("help")): 
        menuehelp()
    elif(userinput.startswith("option")): 
        menueoptions()
    elif(userinput == "clear" or userinput == "cls"): 
        console(userinput)
    elif(str(userinput).startswith("back") or str(userinput).startswith("quit")): 
        return False
    elif(str(userinput).startswith("exit")): 
        exit()
    return True

# Menue + Checks Calculator

def menuecalculator(): 
    print(ConsoleColors.OKGREEN + calculatorString)
    print(optionsString)
    print("1: Calc ")
    print("2: Kombinatorik")
    print("3: Fibonacci")
 
    while True:
        if not checkcalculation(input("#> ")): 
             print(ConsoleColors.OKBLUE + "Menue: ")
             return 

def checkcalculation(userinput):
    if((userinput.startswith('1') and len(userinput) <= 2) or userinput.startswith("calc") or userinput.startswith("rechner")): 
        calculator()
    elif((userinput.startswith('2') and len(userinput) <= 2) or userinput.startswith("kombi")): 
        checkkombinatorik()
    elif((userinput.startswith('3') and len(userinput) <= 2) or userinput.startswith("fibonacci")): 
        target = int(input("Bitte geben sie ihre Zahl ein, von der sie die Fibonacci Reihe berechnen möchten: "))    # still have to write smth about that (try / catch)
        print("Ihr Ergebnis lautet: " + str(fibonaccireihe(target)))
    elif(userinput == "clear" or userinput == "cls"): 
        console(userinput)
    elif(userinput.startswith("option")): 
        calcoptions()
    elif(userinput.startswith("help")): 
        calculatorhelp()
    elif(str(userinput).startswith("back") or str(userinput).startswith("quit")): 
        return False
    elif(str(userinput).startswith("exit")): 
        exit()

    return True

def checkkombinatorik(): 
    print("Fragen zu Berechnung der Formel: ")
    frage1 = input("Ist es eine ?(0) oder eine ?(1)? ")
    state1 = kombinatorikabfrage(frage1)
    while(state1 == Status.WrongInput): 
            print("Sie haben eiune falsche Eingaebe getätigt, bitte versuchen sie es erneut: ")
            frage1 = input("Ist es eine ?(0) oder eine ?(1)? ")
            state1 = kombinatorikabfrage(frage1)

    if state1 == Status.Yes: 
        frage2 = input("Ist es eine ?(0) oder eine ?(1)? ")
        state2 = kombinatorikabfrage(frage2)
        while(state2 == Status.WrongInput): 
            print("Sie haben eiune falsche Eingaebe getätigt, bitte versuchen sie es erneut: ")
            frage2 = input("Ist es eine ?(0) oder eine ?(1)? ")
            state2 = kombinatorikabfrage(frage2)
        if state2 == Status.Yes: 
            frage3 = input("Ist es eine ?(0) oder eine ?(1)? ")
            state3 = kombinatorikabfrage(frage3)
        else: 
            frage3 = input("Ist es eine ?(0) oder eine ?(1)? ")
            state3 = kombinatorikabfrage(frage3)

    else: 
        frage2 = input("Ist es eine ?(0) oder eine ?(1)? ")
        state2 = kombinatorikabfrage(frage2)
        while(state2 == Status.WrongInput): 
            print("Sie haben eiune falsche Eingaebe getätigt, bitte versuchen sie es erneut: ")
            frage2 = input("Ist es eine ?(0) oder eine ?(1)? ")
            state2 = kombinatorikabfrage(frage2)
            if state2 == Status.Yes: 
                frage3 = input("Ist es eine ?(0) oder eine ?(1)? ")
                state3 = kombinatorikabfrage(frage3)
            else: 
                frage3 = input("Ist es eine ?(0) oder eine ?(1)? ")
                state3 = kombinatorikabfrage(frage3)

def kombinatorikabfrage(userinput):
    if((userinput.startswith('1') and len(userinput) <= 2)): 
        return Status.Yes
    elif(userinput.startswith('0')): 
        return Status.No
    elif(userinput.startswith == "exit"): 
        return Status.Exit
    else: 
        return Status.WrongInput

# Sort Menue

def menuesortlist(): 
    print(ConsoleColors.OKGREEN + sortString)
    trennung = input("Geben sie bitte die gewünschte Trennungsmethode ein, welche die einzelnen Werte der Liste trennen sollen: ")

    arrUser = input("Geben sie nun bitte ihre Liste an (TRENNUNG beachten): ")
    arr = []
    try: 
        arr = arrUser.split(trennung)
        print(ConsoleColors.WARNING + ConsoleColors.BOLD + selectionsort(arr) + ConsoleColors.ENDC + ConsoleColors.OKBLUE)
    except:
        print(ConsoleColors.FAIL + "Erstellung der Liste nicht erfolgreich!" + ConsoleColors.OKBLUE)
        return True

# Search Menue

def menuesearchlist(): 
    print(ConsoleColors.OKGREEN + searchString)
    print()
    print(optionsString)
    print("1: Nicht sortierte Reihe")
    print("2: Sortierte Reihe")
    while(True):
        if not checksearchlist(input("#> ")): 
            print(ConsoleColors.OKBLUE + "Menue: ")
            return 

def checksearchlist(userinput): 
    if((userinput.startswith('1') and len(userinput) <= 2) or (userinput.startswith('2') and len(userinput) <= 2)):
        target = 0
        trennung = input("Geben sie bitte die gewünschte Trennungsmethode ein, welche die einzelnen Werte der Liste trennen sollen: ")
        try: 
            target = int(input("Geben sie bitte den gesuchten Wert an: "))
        except: 
            print(ConsoleColors.FAIL + "Eingabe des Suchwertes nicht erfolgreich!" + ConsoleColors.OKGREEN) 
            return True
        arrUser = input("Geben sie nun bitte ihre Liste an (TRENNUNG beachten): ")
        try: 
            arr = arrUser.split(trennung)
            arr = list(map(int, arr))
        except:
            print(ConsoleColors.FAIL + "Erstellung der Liste nicht erfolgreich!" + ConsoleColors.OKGREEN) 
            return True
        if userinput.startswith('1') and len(userinput) <= 2: 
            arr = selectionsort(arr) 
            
        erfolg = binarysearch(arr, target)
        if erfolg: 
            print(ConsoleColors.WARNING + ConsoleColors.UNDERLINE + ConsoleColors.BOLD + "Der Wert existiert in der Liste!" + ConsoleColors.ENDC + ConsoleColors.OKGREEN)
            return True
        print(ConsoleColors.WARNING + "Der Wert existiert NICHT in der Liste!" + ConsoleColors.OKGREEN)
    elif(userinput == "clear" or userinput == "cls"): 
        console(userinput)
    elif(userinput.startswith("help")): 
        calculatorhelp()
    elif(str(userinput).startswith("exit")):
        exit()
    elif(str(userinput).startswith("back") or str(userinput).startswith("quit")): 
        return False

    return True

# Prim Menue (nicht eingebaut)

def menueprim(): 
    pass

# Search String Functions

def searchFaku(stringrechnung, zeichen): 
    while stringrechnung.find(zeichen) != -1:          
        try: 
            faku = stringrechnung.rpartition(zeichen)[0]
            zaehler = 1
            value = 0
            for i in reversed(faku): 
                if i.isnumeric(): 
                    value = value + (int(i) * zaehler)
                    zaehler = zaehler * 10
                else: 
                    break
            stringrechnung = stringrechnung.replace(str(value) + stringrechnung.rpartition(zeichen)[1], str(fakultaet(1, value)))
        except ValueError: 
            print(ConsoleColors.FAIL + "Werte für Fakultät falsch eingegeben, versuche es erneut!" + ConsoleColors.OKGREEN)
    return stringrechnung

def searchVariable(stringrechnung):
    stringrechnung = stringrechnung.replace(" ", "") 
    for i in variablen: 
        if i in stringrechnung: 
            stringrechnung = stringrechnung.replace(i, variablen[i])
    return stringrechnung

def searchSafe(stringrechnung, zeichen):
    global willSafe, zwischenvariable
    stringrechnung = stringrechnung.replace(" ", "")
    if stringrechnung.find(zeichen) != -1: 
            try: 
                willSafe = True
                zwischenvariable = stringrechnung.rpartition(zeichen)[2]
                if not zwischenvariable: 
                    return 
                stringrechnung = stringrechnung.replace(stringrechnung.rpartition(zeichen)[1] + zwischenvariable, "")
            except ValueError: 
                print(ConsoleColors.FAIL + "Werte für Speicherung der Variable falsch eingegeben, versuche es erneut!" + ConsoleColors.OKGREEN)
    return stringrechnung

def makeSafe(ergebnis, zeichen): 
    global willSafe, zwischenvariable
    if willSafe:
        try:
            variablen[zwischenvariable] = ergebnis
            willSafe = False
        except: 
            print(ConsoleColors.FAIL + "Speicherung der Variable hat nicht funktioniert, versuche es erneut!" + ConsoleColors.OKGREEN)
    return

console("clear")
menue()

