import pytest
from src.item import Item
from src.phone import Phone

item1 = Item('Смартфон', 1000, 3)
item2 = Item('Ноутбук', 2500, 2)
item3 = Item('Микроволновка', 8000, 6)
phone1 = Phone("Чайник", 1400, 8, 3)
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


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name():
    assert len(item2.name) <= 10
    assert len(item3.name) >= 10


def test_str():
    assert str(item3) == "Микроволновка"
    assert str(item2) == "Ноутбук"
    assert str(item1) == "Смартфон"


def test_repr():
    assert repr(item3) == "Item('Микроволновка', 8000, 6)"


def test_add():
    assert item1 + phone1 == 11
    assert item2 + phone1 == 10