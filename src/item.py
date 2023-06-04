class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = '[<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
                Создание экземпляра класса item.

                :param name: Название товара.
                :param price: Цена за единицу товара.
                :param quantity: Количество товара в магазине.
                """
        self.name = name
        self.price = price
        self.quantity = quantity



    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        calc_price = self.price * self.quantity
        return calc_price

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        price = self.pay_rate * self.price
        return price

