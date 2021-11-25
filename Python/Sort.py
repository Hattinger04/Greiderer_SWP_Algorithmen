def insertionsort(arr): 
    for i in range(1, len(arr)): 
        value = arr[i]
        j = i
        while j > 0 and arr[j-1] > value: 
            arr[j] = arr[j - 1]
            j = j - 1 
        arr[j] = value
    return arr

def selectionsort(arr): 
    max = len(arr)
    index = 0
    while index < max: 
        min = index
        for i in range(index + 1, max): 
            if arr[i] < arr[min]:
                min = i
        arr[min], arr[index] = arr[index], arr[min]
        index = index + 1
    return arr

print("Insertionsort")
print(insertionsort([1,2,5,7,1,6,3]))
print()

print("Selectionsort")
print(selectionsort([1,2,5,7,1,6,3]))
print()