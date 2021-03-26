def heap_sorted(array: list):
    def isEven(x: int):
        if x % 2 == 0:
            return True
        else:
            return False

    def findParentIndex(index: int):
        if isEven(index):
            return (index - 2) // 2
        else:
            return (index - 1) // 2

    def heapifyBottom(index: int):
        if index == 0:
            return
        else:
            ParentIndex = findParentIndex(index)
            if array[index] < array[ParentIndex]:
                array[index], array[ParentIndex] = array[ParentIndex], array[index]
                heapifyBottom(ParentIndex)

    def heapifyTop(index: int, lastIndex: int):
        if index == lastIndex:
            return
        else:
            leftChildIndex = (index * 2) + 1
            rightChildIndex = (index * 2) + 2
            if leftChildIndex < lastIndex:
                if array[index] > array[leftChildIndex]:
                    array[index], array[leftChildIndex] = array[leftChildIndex], array[index]
                    heapifyTop(leftChildIndex, lastIndex)
            if rightChildIndex < lastIndex:
                if array[index] > array[rightChildIndex]:
                    array[index], array[rightChildIndex] = array[rightChildIndex], array[index]
                    heapifyTop(rightChildIndex, lastIndex)

    for index in range(len(array)):
        heapifyBottom(index)
    print(array)
    for index in range(len(array)-1, 0, -1):
        print(index)
        array[0], array[index] = array[index], array[0]
        print(array)
        heapifyTop(0, index)
        print(array)
    return array


array = [11, 5, 9, 3, 4, 6, 2, 1, 3, 12, 25]
print(array)
print(heap_sorted(array))
