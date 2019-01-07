# 1. Countdown - Create a function that accepts a number as an input.  Return a new list that counts 
# down by one, from the number (as lists 'zero'th element) down to 0 (as the last element).  
# For example countDown(5) should return [5,4,3,2,1,0].
def countDown(num):
    arr = []
    for i in range(0, num + 1):
        arr.append(num - i)
    print(arr)
countDown(6)

# 2. Print and Return - Your function will receive a list with two numbers. Print the first value, 
# and return the second.
def printReturn(list):
    print(list[0])
    return list[1]
x = printReturn([3,2])
print(x)

# 3. First Plus Length - Given a list, return the sum of the first value in the list, plus the list's length.
def firstPlusLength(list):
    sum = 0
    if type(list[0]) is int:
        sum = 0 + len(list)
    else:
        sum = len(list[0]) + len(list)
    return sum
print(firstPlusLength(["banana", 3, 2, 3]))
print(firstPlusLength([1, 3, 2, 3]))

# 4. Values Greater than Second - Write a function that accepts a list, and returns a new list with 
# the list values that are greater than its 2nd value.  Print how many values this is.  
# If the list is only one element long, have the function return False
def valueGreaterThanSecond(list):
    arr = []
    if len(list) > 1:
        for i in list:
            if i > list[1]:
                arr.append(i)
        return arr
    else:
        return False

x = valueGreaterThanSecond([4,3,6,1,4])
y = valueGreaterThanSecond([4])
print(x)
print(y)

# 5. This Length, That Value - Write a function called lengthAndValue which accepts two parameters, 
# size, and value. This function should take two numbers and return a list of length size containing 
# only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].
def lengthAndValue(size, value):
    arr = []
    inc = 0
    while inc < size:
        arr.append(value)
        inc += 1
    return arr
print(lengthAndValue(4,7))
print(lengthAndValue(10,7))