class Product:

    REASON = ('defective', 'like_new', 'opened')

    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def calcTax(self, tax):
        return self.price*(1 + tax)

    def returnItem(self, reason):
        if reason == self.REASON[0]:
            self.status = "defective"
            self.price = 0
        elif reason == self.REASON[1]:
            self.status = "for sale"
        elif reason == self.REASON[2]:
            self.status = "used"
            self.price = self.price - self.price * 0.20
        return self

    def display_info(self):
        print("Price: ", self.price)
        print("Item name: ", self.item_name)
        print("Weight: ",  self.weight)
        print("Brand: ", self.brand)
        print("Status: ", self.status, "\n")
        return self


product1 = Product(1300, "Dell Desktop", "5.6lb", "Dell")
product1.sell().display_info()
product1.returnItem("opened").display_info()

product2 = Product(1500, "MacBook Pro", "4.6lb", "Apple")
product2.sell().display_info()
product2.returnItem("defective").display_info()
