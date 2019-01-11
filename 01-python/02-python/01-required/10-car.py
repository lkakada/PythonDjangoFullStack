class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = lambda: 0.15 if self.price > 10000 else 0.12

        self.display_all()

    def display_all(self):
        print(f"Price: {self.price}")
        print(f"Speed: {self.speed}")
        print(f"Fuel: {self.fuel}")
        print(f"Mileage: {self.mileage}")
        print(f"Tax: {self.tax()}\n")
        return self


bmw = Car(9000, '35mph', 'full', '15mpg')
lexus = Car(2000, '35mph', 'empty', '15mpg')
audi = Car(5000, '35mph', 'full', '15mpg')
ford = Car(2000, '35mph', 'kind of full', '15mpg')
gmc = Car(70000, '35mph', 'full', '15mpg')
madaz = Car(2000, '35mph', 'empty', '15mpg')
