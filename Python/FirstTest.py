# Binary Search iterative:
def binarySearchIterative(arr, target):

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

# Binary Search rekursive:
def binarySearchRecusive(arr, target, left, right):

    middle = round((left + right) / 2)
    if arr[middle] == target:
        return True
    if left > right:
        return False

    elif target > arr[middle]:
        return binarySearchRecusive(arr, target, middle + 1, right)
    else:
        return binarySearchRecusive(arr, target, left, middle - 1)

# Fakultät rekursiv
def fakRecursive(base):
    if base <= 1:
        return 1
    return base * fakRecursive(base - 1)

# Fakultät endrekursiv
def fakEndRecursive(product, base):
    if base <= 1:
        return product
    return fakEndRecursive(product * base, base - 1)

# Hochfunktion rekursiv
def powRecursive(basis, exponent):
    if exponent == 0:
        return 1
    return basis * powRecursive(basis, exponent-1)

# Hochfunktion endrekursiv
def powEndRecursive(product, basis, exponent):
    if exponent == 0:
        return product
    return powEndRecursive(product * basis, basis, exponent - 1)

print("Suche")
print(binarySearchIterative([1,2,3,4,5,6,7,8,9], 5))
print(binarySearchRecusive([1,2,3,4,5, 6,7,8,9], 5, 0, 9))
print()

print("Fakultät")
print(fakRecursive(31) / (fakRecursive(2) * fakRecursive(29)))
print(fakEndRecursive(1, 5))
print()

print("Hochfunktion")
print(powRecursive(2, 5))
print(powEndRecursive(1, 2, 5))

