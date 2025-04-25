import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "params, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 736541084301358743", "Введён неверный формат карты\\аккаунта"),
        ("Счет 7365410843013587430t", "Введён неверный формат карты\\аккаунта"),
        ("", "Введён неверный формат карты\\аккаунта"),
    ],
)
def test_mask_account_card(params: str, expected: str) -> None:
    """Функция тестирования маскировки карт/счетов"""

    assert mask_account_card(params) == expected


@pytest.mark.parametrize(
    "params, expected",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2025-01-31", "31.01.2025"), ("", "Нет данных")],
)
def test_get_date(params: str, expected: str) -> None:
    """Функция тестирования форматирования даты"""

    assert get_date(params) == expected
