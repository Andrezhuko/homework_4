from src.class_by_category import Category


def test_Product(Product_object):
    product = Product_object
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.info_by_price == 180000.0
    assert product.quantity == 5
    product.info_by_price = 52
    assert product.info_by_price == 52

def test_Category(Product_object):
    product1 = Product_object
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1],
    )
    assert category1.name == "Смартфоны"
    assert (category1.description == "Смартфоны, как средство не только коммуникации, "
                                     "но и получения дополнительных функций для удобства жизни")
    assert category1.return_product == [product1]
    category1.add_product = [product1]
    assert category1.return_product == [[product1].append(product1)]
