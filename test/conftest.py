import pytest
from src.class_by_product import Product

@pytest.fixture
def Product_object():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)