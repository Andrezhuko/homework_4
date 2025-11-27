def test_Lawngrass(grass_one, grass_two):
    grass1 = grass_one
    grass2 = grass_two

    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"

    assert grass2.name == "Газонная трава 2"
    assert grass2.description == "Выносливая трава"
    assert grass2.price == 450.0
    assert grass2.quantity == 15
    assert grass2.country == "США"
    assert grass2.germination_period == "5 дней"
    assert grass2.color == "Темно-зеленый"
