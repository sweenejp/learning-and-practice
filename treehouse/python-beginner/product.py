class Product:
    _price = 0.0
    tax_rate = 0.12

    def __init__(self, base_price):
        self._price = base_price

    @property
    def price(self):
        return self._price + (self._price * self.tax_rate)

    @price.setter
    def price(self, new_price):
        self._price = new_price


cheese = Product(2.50)
cost_of_cheese = cheese.price
print(cost_of_cheese)

cheese.price = 3.00
print(cheese.price)
print(cheese.tax_rate)

