from typing import Any, Dict, Iterator


def filter_by_currency(transactions: list[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Функция принимает на вход список словарей, представляющих транзакции, возвращать итератор, который поочередно
    выдает транзакции, где валюта операции соответствует заданной"""
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions: list[dict]) -> str:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        description = transaction.get("description", "")
        yield description


def card_number_generator(start: int, end: int) -> str:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    if start < 1 or end > 9999999999999999 or start > end:
        raise ValueError("Некорректный диапазон номеров карт")

    for num in range(start, end + 1):
        formatted_num = str(num).zfill(16)
        card_number = " ".join([formatted_num[i : i + 4] for i in range(0, 16, 4)])
        yield card_number
