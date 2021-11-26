def fibonacciReiheIterative(target):
    last = 1
    current = 0
    for i in range(0, target): 
        current, last = current + last, current
    return current

def fibonacciReiheRecursive(target):
    if target == 0 or target == 1: 
        return target
    return fibonacciReiheRecursive(target-2)+ fibonacciReiheRecursive(target-1)

def fibonacciReiheEndrekursion(zahl, zahl2, target):
    if target == 1: 
        return zahl + zahl2
    return fibonacciReiheEndrekursion(zahl + zahl2, zahl, target-1)



print(fibonacciReiheIterative(20)) 
print(fibonacciReiheRecursive(20)) 
print(fibonacciReiheEndrekursion(0, 1, 20)) 
