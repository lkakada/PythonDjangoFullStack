arr = [4, 7, 2, 9, 0, 1]


def insertionSort(lists):
    for i in range(1, len(lists)):
        curNum = lists[i]
        index = i - 1
        while index >= 0 and curNum < lists[index]:
            print(index)
            lists[index + 1] = lists[index]
            index -= 1
            print(lists)
        lists[index + 1] = curNum
    return lists


print(insertionSort(arr))
