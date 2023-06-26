import pytest
from src.keyboard import Keyboard

kb = Keyboard('WoodDask 17-84B4', 4700, 78)


def test_init():
    assert str(kb) == 'WoodDask 17-84B4'


def test_change_lang():
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


def test_error_setter_language():
    with pytest.raises(AttributeError):
        kb.language = 'CH'