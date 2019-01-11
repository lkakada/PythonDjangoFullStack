arr = [10, 6, 30, 1, 9, 27, 1]


def selection_sort(lists):
    for i in range(len(lists)):
        min_index = i
        for j in range(i, len(lists)):
            if lists[min_index] > lists[j]:
                min_index = j
        lists[i], lists[min_index] = lists[min_index], lists[i]
    return lists


print(selection_sort(arr))
