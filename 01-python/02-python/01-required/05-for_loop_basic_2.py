# 1. Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big".
# Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].


def makeItBig(list):
    for i in range(len(list) - 1):
        if list[i] > 0:
            list[i] = "big"
    return list


print(makeItBig([-1, 3, 5, -5]))

# 2. Count Positives - Given an array of numbers, create a function to replace last value with
# number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3]
# and returns it.  (Note that zero is not considered to be a positive number).


def countPositives(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
    list[len(list) - 1] = count
    return list


print(countPositives([-1, 1, 1, 1]))

# 3. SumTotal - Create a function that takes an array as an argument and returns the sum of all the values
# in the array.  For example sumTotal([1,2,3,4]) should return 10


def sumTotal(list):
    sum = 0
    for i in list:
        sum += i
    return sum


print(sumTotal([1, 2, 3, 4]))

# 4.Average - Create a function that takes an array as an argument and returns the average of all
# the values in the array.  For example average([1,2,3,4]) should return 2.5


def average(list):
    avg = 0
    sum = sumTotal(list)
    avg = float(sum) / len(list)
    return round(avg, 2)


print(average([1, 2, 3, 4]))

# 5. Length - Create a function that takes an array as an argument and returns the length of the array.
# For example length([1,2,3,4]) should return 4


def lengthList(list):
    length = 0
    while length < len(list):
        length += 1
    return length


print(lengthList([1, 2, 3, 4]))

# 6. Minimum - Create a function that takes an array as an argument and returns the minimum value
# in the array.  If the passed array is empty, have the function return false.
# For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.


def minimum(list):
    if len(list) > 0:
        min = list[0]
        for i in range(len(list)):
            if min > list[i]:
                min = list[i]
        return min
    else:
        return False


print(minimum([1, 2, 3, 4]))
print(minimum([-1, -2, -3]))
print(minimum([]))

# 7. Maximum - Create a function that takes an array as an argument and returns the maximum value
# in the array.  If the passed array is empty, have the function return false.
# For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.


def maximum(list):
    if len(list) > 0:
        max = list[0]
        for i in range(len(list)):
            if max < list[i]:
                max = list[i]
        return max
    else:
        return False


print(maximum([1, 2, 3, 4]))
print(maximum([-1, -2, -3]))
print(maximum([]))

# 8. UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary
# that has the sumTotal, average, minimum, maximum and length of the array.


def ultimateAnalyze(list):
    collection = {}
    max = maximum(list)
    min = minimum(list)
    length = lengthList(list)
    sum = sumTotal(list)
    avg = average(list)
    collection = {
        "Sum": sum,
        "Average": avg,
        "Minimum": min,
        "Maximum": max,
        "Length": length
    }
    return collection


print(ultimateAnalyze([3, 2, 5, 8, 1, 9, 4]))

# 9. ReverseList - Create a function that takes an array as an argument and return an array in a reversed
# order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4])
# should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.


def reverseList(list):
    for i in range(len(list)/2):
        list[i], list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]
    return list


print(reverseList([1, 2, 3, 4]))
