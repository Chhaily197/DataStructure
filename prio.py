#Priority Queue implementation in Python

#Function to heapify the tree
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    #Swap and continue heapifying if root is not larget
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

#Function to insert and element inot the tree
def insert(arr, newNumber):
    size = len(arr)
    if size == 0:
        arr.append(newNumber)
    else:
        arr.append(newNumber)
        for i in range((size // 2) -1, -1, -1):
            heapify(arr, size, i)

#Function to delete an element from the tree
def deleteNode(arr, num):
    size = len(arr)
    i = 0
    for i in range(0, size):
        if num == arr[i]:
            break
    arr[i], arr[size - 1] = arr[size - 1], arr[i]
    arr.remove(size, 1)

    for i in range((len(arr) // 2) -1, -1, -1):
        heapify(arr, len(arr), i)

arr = []
insert(arr, 3)
insert(arr, 5)
insert(arr, 7)
insert(arr, 9)
insert(arr, 13)


print("Max-Heap array: " + str(arr))
