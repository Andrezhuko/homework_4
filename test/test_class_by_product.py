import pytest

from src.class_by_product import Product


def test_Product(product_object, product_dict):
    product = product_object
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8
    product.price = 52
    assert product.price == 52
    product.price = 0
    assert product.price == 52
    product_two = Product.new_product(product_dict)
    assert product_two.name == "Samsung Galaxy S23 Ultra"
    assert product_two.description == "256GB, Серый цвет, 200MP камера"
    assert product_two.price == 180000.0
    assert product_two.quantity == 5


def test_by_function_add(product_object, product_object_two):
    product = product_object
    product2 = product_object_two
    assert product + product2 == 2114000.0

def test_by_zero_quantity(product_object_two):
    with pytest.raises(ValueError):
        product = Product("Iphone 15", "512GB, Gray space", 210000.0, 0)