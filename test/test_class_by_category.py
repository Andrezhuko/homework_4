from src.class_by_category import Category


def test_Category(product_object):
    product1 = product_object
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1],
    )
    assert category1.name == "Смартфоны"
    assert (
        category1.description == "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category1.return_product == [product1]
    assert category1.products == "Iphone 15, 210000.0 руб. Остаток: 8шт.\n"


def test_add_product(product_object, category_one):
    assert len(category_one.return_product) == 1
    category_one.add_product(product_object)
    assert len(category_one.return_product) == 2

def test_middle_price(category_one, category_two):
    cat1 = category_one
    cat2 = category_two
    assert cat1.middle_price() == 180000
    assert cat2.middle_price() == 0
