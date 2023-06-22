import pytest
from src.item import Item
from src.phone import Phone

phone1 = Phone("iPhone-1", 30000, 3, 8)
phone2 = Phone("iPhone-2", 70000, 8, 29)


def test_phone_init():
    assert phone1.name == "iPhone-1"
    assert phone1.price == 30000
    assert phone1.quantity == 3
    assert phone1.number_of_sim == 8
    assert phone2.name == "iPhone-2"
    assert phone2.price == 70000
    assert phone2.quantity == 8
    assert phone2.number_of_sim == 29