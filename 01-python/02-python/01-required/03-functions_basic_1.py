def a():
    return 5


print(a())
# Output: 5


def b():
    return 5


print(b()+b())
# Output: 10


def c():
    return 5
    return 10


print(c())
# Ouput: 5


def d():
    return 5
    print(10)


print(d())
# Output: 5


def f():
    print(5)


x = f()
print(x)
# Output: 5, none


def g(b, c):
    print(b+c)
# print(g(1,2) + g(2,3))
# Output: 3, 5, unsupport operand type


def h(b, c):
    return str(b)+str(c)


print(h(2, 5))
# Output: 25


def j():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7


print(j())
# Output: 100, 10


def k(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(k(2, 3))
print(k(5, 3))
print(k(2, 3) + k(5, 3))
# Output:7, 14, 21


def l(b, c):
    return b+c
    return 10


print(l(3, 5))
# Output:8

b = 500
print(b)


def m():
    b = 300
    print(b)


print(b)
m()
print(b)
# Output: 500, 500, 300, 500

b = 500
print(b)


def n():
    b = 300
    print(b)
    return b


print(b)
n()
print(b)
# Output: 500, 500, 300, 500

b = 500
print(b)


def o():
    b = 300
    print(b)
    return b


print(b)
b = o()
print(b)
# Output: 500, 500, 300, 300


def p():
    print(1)
    q()
    print(2)


def q():
    print(3)


p()
# Output: 1, 3, 2


def s():
    print(1)
    x = r()
    print(x)
    return 10


def r():
    print(3)
    return 5


y = s()
print(y)
# Output: 1, 3, 5, 10
