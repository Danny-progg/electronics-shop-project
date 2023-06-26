import os
from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
                Создание экземпляра класса item.

                :param name: Название товара.
                :param price: Цена за единицу товара.
                :param quantity: Количество товара в магазине.
                """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Создает экземпляры класса на основе таблицы хранящейся в items.csv
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/items.csv', encoding='utf-8') as csv_file:
            csv_reader = DictReader(csv_file)
            cls.all = []
            for (row) in csv_reader:
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        Преобразовывает строки-числа в числа
        """
        if "." in number:
            return int(float(number))
        else:
            return int(number)

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity





