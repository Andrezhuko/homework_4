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

    @classmethod
    def add_product(cls, product_object):
        cls.__products.update(product_object)
        Category.product_count += len(product_object)
        Category.category_count += 1

    @property
    def print_user_list_product(self):
        new_str = ""
        for product in self.__products:
            new_str += f"{product.name}, {product.price}. {product.quantity}."

    @property
    def return_product(self):
        return self.__products