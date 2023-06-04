import pytest
from src.item import Item

item1 = Item("Смартфон", 9876, 20)
item2 = Item("Ноутбук", 20000, 7)


assert item1.price == 9876
assert item2.quantity == 7
assert item1.calculate_total_price() == 197520
assert item2.apply_discount() == 20000
