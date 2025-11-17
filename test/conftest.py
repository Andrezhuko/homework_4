import pytest

from src.class_by_category import Category
from src.class_by_product import Product


@pytest.fixture
def product_object():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

@pytest.fixture
def product_object_two():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

@pytest.fixture
def product_dict():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}

@pytest.fixture
def category_one():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        ],
    )
