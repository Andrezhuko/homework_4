from src.class_by_category import Category


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
    assert category1.products == "Iphone 15, 210000.0 руб. Остаток: 8шт.\n"


def test_add_product(Product_object, category_one):
    assert len(category_one.return_product) == 1
    category_one.add_product(Product_object)
    assert len(category_one.return_product) == 2