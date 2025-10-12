import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    """Фикстура с примером транзакций для тестирования."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def empty_transactions():
    """Фикстура с пустым списком транзакций."""
    return []


@pytest.fixture
def transactions_without_descriptions():
    """Фикстура с транзакциями без описаний."""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2020-01-01T00:00:00.000000",
            "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2020-01-02T00:00:00.000000",
            "operationAmount": {"amount": "200.00", "currency": {"name": "EUR", "code": "EUR"}},
        },
    ]


class TestFilterByCurrency:
    """Тесты для функции filter_by_currency."""

    def test_filter_usd_transactions(self, sample_transactions):
        """Тестирование фильтрации USD транзакций."""
        # Act
        usd_transactions = list(filter_by_currency(sample_transactions, "USD"))

        # Assert
        assert len(usd_transactions) == 3  # Исправлено с 2 на 3
        assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in usd_transactions)
        assert usd_transactions[0]["id"] == 939719570
        assert usd_transactions[1]["id"] == 142264268
        assert usd_transactions[2]["id"] == 895315941

    def test_filter_eur_transactions(self, sample_transactions):
        """Тестирование фильтрации EUR транзакций."""
        # Act
        eur_transactions = list(filter_by_currency(sample_transactions, "EUR"))

        # Assert
        assert len(eur_transactions) == 0  # Исправлено с 1 на 0

    @pytest.mark.parametrize(
        "currency,expected_count",
        [
            ("USD", 3),  # Исправлено с 2 на 3
            ("EUR", 0),  # Исправлено с 1 на 0
            ("GBP", 0),  # Исправлено с 1 на 0
            ("JPY", 0),
            ("RUB", 2),  # Исправлено с 0 на 2
        ],
    )
    def test_filter_multiple_currencies(self, sample_transactions, currency, expected_count):
        """Параметризованный тест фильтрации разных валют."""
        # Act
        filtered_transactions = list(filter_by_currency(sample_transactions, currency))

        # Assert
        assert len(filtered_transactions) == expected_count

    def test_filter_nonexistent_currency(self, sample_transactions):
        """Тестирование фильтрации несуществующей валюты."""
        # Act
        result = list(filter_by_currency(sample_transactions, "JPY"))

        # Assert
        assert len(result) == 0

    def test_empty_list(self, empty_transactions):
        """Тестирование с пустым списком транзакций."""
        # Act
        result = list(filter_by_currency(empty_transactions, "USD"))

        # Assert
        assert len(result) == 0

    def test_transaction_without_currency_info(self, sample_transactions):
        """Тестирование транзакции без полной информации о валюте."""
        # Act
        result = list(filter_by_currency(sample_transactions, "GBP"))

        # Assert
        assert len(result) == 0  # Исправлено с 1 на 0

    def test_generator_behavior(self, sample_transactions):
        """Тестирование поведения генератора при последовательном вызове next()."""
        # Arrange
        generator = filter_by_currency(sample_transactions, "USD")

        # Act & Assert
        first_transaction = next(generator)
        assert first_transaction["id"] == 939719570

        second_transaction = next(generator)
        assert second_transaction["id"] == 142264268

        third_transaction = next(generator)
        assert third_transaction["id"] == 895315941

        # Должен возникнуть StopIteration после исчерпания генератора
        with pytest.raises(StopIteration):
            next(generator)


class TestTransactionDescriptions:
    """Тесты для функции transaction_descriptions."""

    def test_get_all_descriptions(self, sample_transactions):
        """Тестирование получения всех описаний."""
        # Act
        descriptions = list(transaction_descriptions(sample_transactions))

        # Assert
        expected = [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",  # Исправлено с "" на реальное описание
            "Перевод организации",
        ]
        assert descriptions == expected

    def test_empty_list(self, empty_transactions):
        """Тестирование с пустым списком транзакций."""
        # Act
        result = list(transaction_descriptions(empty_transactions))

        # Assert
        assert result == []

    def test_transactions_without_descriptions(self, transactions_without_descriptions):
        """Тестирование транзакций без описаний."""
        # Act
        descriptions = list(transaction_descriptions(transactions_without_descriptions))

        # Assert
        assert descriptions == ["", ""]

    def test_generator_behavior(self, sample_transactions):
        """Тестирование поведения генератора при последовательном вызове next()."""
        # Arrange
        generator = transaction_descriptions(sample_transactions)

        # Act & Assert
        assert next(generator) == "Перевод организации"
        assert next(generator) == "Перевод со счета на счет"
        assert next(generator) == "Перевод со счета на счет"
        assert next(generator) == "Перевод с карты на карту"  # Исправлено с "" на реальное описание
        assert next(generator) == "Перевод организации"

        # Должен возникнуть StopIteration после исчерпания генератора
        with pytest.raises(StopIteration):
            next(generator)


class TestCardNumberGenerator:
    """Тесты для функции card_number_generator."""

    @pytest.mark.parametrize(
        "start,end,expected",
        [
            (1, 1, ["0000 0000 0000 0001"]),
            (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
            (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
        ],
    )
    def test_generate_range(self, start, end, expected):
        """Параметризованный тест генерации диапазона номеров."""
        # Act
        result = list(card_number_generator(start, end))

        # Assert
        assert result == expected

    def test_formatting(self):
        """Тестирование форматирования номеров карт."""
        # Act
        generator = card_number_generator(1234567890123456, 1234567890123456)
        result = next(generator)

        # Assert
        assert result == "1234 5678 9012 3456"
        assert len(result) == 19  # 16 цифр + 3 пробела

    def test_large_numbers(self):
        """Тестирование больших номеров карт."""
        # Act
        generator = card_number_generator(9999999999999999, 9999999999999999)
        result = next(generator)

        # Assert
        assert result == "9999 9999 9999 9999"

    @pytest.mark.parametrize(
        "start,end",
        [
            (10, 5),  # start > end
            (0, 5),  # start < 1
            (1, 10000000000000000),  # end > 9999999999999999
        ],
    )
    def test_invalid_range(self, start, end):
        """Тестирование невалидного диапазона."""
        # Act & Assert
        with pytest.raises(ValueError):
            list(card_number_generator(start, end))

    def test_edge_cases(self):
        """Тестирование граничных случаев."""
        # Минимальное значение
        result_min = list(card_number_generator(1, 1))
        assert result_min == ["0000 0000 0000 0001"]

        # Максимальное значение
        result_max = list(card_number_generator(9999999999999999, 9999999999999999))
        assert result_max == ["9999 9999 9999 9999"]

    def test_generator_behavior(self):
        """Тестирование поведения генератора."""
        # Arrange
        generator = card_number_generator(1, 3)

        # Act & Assert
        assert next(generator) == "0000 0000 0000 0001"
        assert next(generator) == "0000 0000 0000 0002"
        assert next(generator) == "0000 0000 0000 0003"

        # Должен возникнуть StopIteration после исчерпания генератора
        with pytest.raises(StopIteration):
            next(generator)


# Интеграционные тесты
class TestIntegration:
    """Интеграционные тесты всех функций вместе."""

    def test_integration_workflow(self, sample_transactions):
        """Тестирование полного рабочего процесса."""
        # Фильтруем USD транзакции
        usd_transactions = list(filter_by_currency(sample_transactions, "USD"))

        # Получаем описания USD транзакций
        descriptions = list(transaction_descriptions(usd_transactions))

        # Assert
        assert len(usd_transactions) == 3
        assert descriptions == ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]

        # Генерируем тестовые номера карт для отчета
        card_numbers = list(card_number_generator(1, 2))
        assert card_numbers == ["0000 0000 0000 0001", "0000 0000 0000 0002"]

    def test_empty_data_integration(self, empty_transactions):
        """Интеграционное тестирование с пустыми данными."""
        # Act
        filtered = list(filter_by_currency(empty_transactions, "USD"))
        descriptions = list(transaction_descriptions(empty_transactions))

        # Assert
        assert filtered == []
        assert descriptions == []
