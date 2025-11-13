class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, kwargs):
        return cls(kwargs["name"], kwargs["description"], kwargs["price"], kwargs["quantity"])

    @property
    def info_by_price(self):
        return self.__price

    @info_by_price.setter
    def info_by_price(self, new_price: int):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")

        else:
            self.__price = new_price

print(Product.new_product({"name":"Iphone 15","description": "512GB, Gray space","price": 210000.0,"quantity": 8}))
