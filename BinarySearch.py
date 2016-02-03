def binarySearch(targetelement, elements ):
    low = 0
    high = len(elements)
    position = 0
    numberofcomparisons = 0
    found = False
    while low <= high:
        mid = (low + high)//2
        numberofcomparisons += 1
        if targetelement == elements[mid]:
            position = mid
            found = True
            break
        numberofcomparisons += 1
        if targetelement < elements[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if not found:
        position = -1
    return (position, numberofcomparisons)

listmin = 11
listmax = 70
array = list(range(listmin, listmax))
print("Current list in use is: ", array)
print("Length of current list is: ", len(array))

for element in array:
    print(binarySearch(element, array))