from src.item import Item


class MixinLanguage:
    __slots__ = ['__language']

    def __init__(self) -> None:
        self.__language: str = "EN"

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLanguage):
    __slots__ = ['name', 'price', 'quantity']

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

