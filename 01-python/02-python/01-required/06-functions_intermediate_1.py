import random
def randInt(max = 100, min = 0):
    rand = random.random() * (max - min) + min
    return int(rand)

# randInt() returns a random integer between 0 to 100
print(randInt())
# randInt(max=50) returns a random integer between 0 to 50
print(randInt(max = 50))
# randInt(min=50) returns a random integer between 50 to 100
print(randInt(min=50))
# randInt(min=50, max=500) returns a random integer between 50 and 500
print(randInt(min=50, max=500))