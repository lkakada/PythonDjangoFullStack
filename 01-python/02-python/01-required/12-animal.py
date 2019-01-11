class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print("The animal's health is :", self.health)
        return self

a1 = Animal('Bella', 20)
a1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name, health = 150):
        super().__init__(name, health)
    
    def pet(self):
        self.health -= 5
        return self
a2 = Dog('Lucky')
a2.walk().walk().walk().run().run().pet().displayHealth()
# a2.fly()

class Dragon(Animal):
    def __init__(self, name, health = 170):
        super().__init__(name, health)

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon")
        return self
a3 = Dragon('Lola')
a3.walk().run().fly().displayHealth()
# a3.pet()
