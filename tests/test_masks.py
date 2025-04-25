from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account() -> None:
    assert get_mask_account(12345678901234567890) == "**7890"
    assert get_mask_account(1234) == "Введён неверный формат данных"
    assert get_mask_account("") == "Нет данных"


def test_get_mask_card_number() -> None:
    assert get_mask_card_number(1234567890123451) == "1234 56** **** 3451"
    assert get_mask_account(1234) == "Введён неверный формат данных"
    assert get_mask_account("") == "Нет данных"
