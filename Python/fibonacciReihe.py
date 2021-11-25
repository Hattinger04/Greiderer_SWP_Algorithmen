def fibonacciReihe(zahl, zahl2, target):
    if target == 1: 
        return zahl + zahl2
    return fibonacciReihe(zahl + zahl2, zahl, target-1)

print(fibonacciReihe(0, 1, 20)) 

def fibonacciReiheRecursive(target):
    if target == 0: 
        return 0
    if target == 1: 
        return 1
    return fibonacciReiheRecursive(target-2)+ fibonacciReiheRecursive(target-1)

print(fibonacciReiheRecursive(20)) 