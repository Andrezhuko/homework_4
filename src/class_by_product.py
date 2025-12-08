from src.base_product import BaseProduct
from src.product_mixin import Mixin_product

class Product(Mixin_product, BaseProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if other.__class__ is not self.__class__:
            raise TypeError()
        else:
            return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, kwargs):
        return cls(
            kwargs["name"], kwargs["description"], kwargs["price"], kwargs["quantity"]
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")

        else:
            self.__price = new_price

