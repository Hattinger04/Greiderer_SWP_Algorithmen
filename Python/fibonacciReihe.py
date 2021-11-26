def fibonaccireiheiterative(target):
    last = 1
    current = 0
    for i in range(0, target): 
        current, last = current + last, current
    return current

def fibonaccireiherecursive(target):
    if target == 0 or target == 1: 
        return target
    return fibonaccireiherecursive(target-2)+ fibonaccireiherecursive(target-1)

def fibonaccireiheendrekursion(zahl, zahl2, target):
    if target == 1:
        return zahl + zahl2
    return fibonaccireiheendrekursion(zahl + zahl2, zahl, target-1)



print(fibonaccireiheiterative(20)) 
print(fibonaccireiherecursive(20)) 
print(fibonaccireiheendrekursion(0, 1, 20)) 
