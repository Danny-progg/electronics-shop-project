import pytest
from src.item import Item

item1 = Item("Смартфон", 1000, 3)
item2 = Item("Ноутбук", 2500, 2)
Item.pay_rate = 0.8


def test_item_init():
    assert item1.name == "Смартфон"
    assert item2.name == "Ноутбук"
    assert item1.price == 1000
    assert item2.price == 2500
    assert item1.quantity == 3
    assert item2.quantity == 2


def test_calculate_total_price():
    assert item1.calculate_total_price() == 3000
    assert item2.calculate_total_price() == 5000


def test_apply_discount():
    assert item1.apply_discount() is None
    assert item2.apply_discount() is None

