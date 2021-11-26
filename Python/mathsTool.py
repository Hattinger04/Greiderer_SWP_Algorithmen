class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
            if arr[i] < arr[min]:
                minimal = i
        arr[minimal], arr[index] = arr[index], arr[minimal]
        index = index + 1
    return arr


def fibonaccireihe():
    target = int(input("Bitte geben sie ihre Zahl ein, von der sie die Fibonacci Reihe berechnen möchten: ")) # still have to write smth about that (try / catch)
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
    print("Calc")


def menue(): 
    print(bcolors.OKGREEN + nameString)
    print()
    print(optionsString)
    print("1: Calculator")
    print("2: Sort a list")
    print("3: Search value from a list")

    while(True):
        if not checkvalue(input(">> ")): 
            return 

def checkvalue(userinput):
    if(userinput == '1'): 
        menuecalculator()
    elif(userinput == '2'): 
        menuesortlist()
    elif(userinput == '3'): 
        menuesearchlist()
    elif(str(userinput).startswith("exit") or str(userinput).startswith("quit")): 
        return False
    return True

def menuecalculator(): 
    print(bcolors.OKBLUE + calculatorString)
    print("1: Rechner ")
    print("2: Kombinatorik")
    print("3: Fibonacci")
    while(True):
         if not checkcalculation(input("# ")): 
             print(bcolors.OKGREEN + "Menue: ")
             return 


def menuesortlist(): 
    print(bcolors.OKBLUE + sortString)
    print()


def menuesearchlist(): 
    print(bcolors.OKBLUE + searchString)
    print()

def menuekombinatorik(): 
    print(bcolors.OKCYAN + kombinatorikString)
    print()
    print(optionsString)
    print("1: ")
    print("2: ")
    print("3: ")
    print("4: ")
    print("5: ")
    print("6: ")

    while(True):
         if not checkkombinatorik(input("# ")): 
             print(bcolors.OKBLUE + "Calculatormenue: ")
             return 



def checkcalculation(userinput):
    if(userinput == '1'): 
        calculator()
    elif(userinput == '2'): 
        menuekombinatorik()
    elif(userinput == '3'): 
        fibonaccireihe()
    elif(str(userinput).startswith("exit") or str(userinput).startswith("quit")): 
        return False
    return True
    
def checkkombinatorik(userinput): 
    print(int(userinput))




menue()
