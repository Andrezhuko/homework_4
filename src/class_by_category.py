from src.class_by_product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    @property
    def products(self):
        new_str = ""
        for product in self.__products:
            new_str += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity}шт.\n"
            )
        return new_str

    def add_product(self, product_object):
        if isinstance(product_object, Product):
            Category.product_count += 1
            self.__products.append(product_object)

    @property
    def return_product(self):
        return self.__products
