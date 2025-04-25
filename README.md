# Виджет для банка

## Содержание
- [Описание](#описание)
- [Технологии](#Технологии)
- [Установка](#Установка)
- [Использование](#Использование)
- [Документация](#Документация)

## Описание
Проект создавался с целью редактирования банковских данных
для виджета банка. На данный момент можно маскировать номер
карты/счёта, форматировать дату, а также сортировать список операций.

## Технологии
* [Python](https://www.python.org/)

## Установка  
1. Клонируйте репозиторий
```commandline
git clone https://github.com/Mr-iOS/Bank_widget.git
```
2. Установите зависимости:
```commandline
pip install -r requirements.txt
```

## Использование
Файл __[masks.py](src/masks.py)__ отвечает за наложение масок
на номер карт / аккаунтов.
```commandline
get_mask_card_number(test_card_number)
get_mask_account(test_account_number)
```
Пример использования:
```commandline
print(get_mask_card_number(1234567890123451)) --> "1234 56** **** 3451"
print(get_mask_account(12345678901234567890)) --> "**7890"
```
Файл __[widget.py](src/widget.py)__ отвечает за наложение масок на
вводные формата "карта/счёт номер_карты/номер_счёта", а также
за форматирование даты.
```commandline
mask_account_card(account_name)
get_date(date)
```
Пример использования:
```commandline
print(mask_account_card("Maestro 1596837868705199")) --> "Maestro 1596 83** **** 5199"
print(mask_account_card("Счет 64686473678894779589")) --> "Счет **9589"
print(get_date("2024-03-11T02:26:18.671407")) --> "11.03.2024"
```
Файл __[processing.py](src/processing.py)__ отвечает за сортировку операций
по дате и по выполнению.
```commandline
filter_by_state(list_of_operations, state) # state is optional, by default = "EXECUTED"
sort_by_date(list_of_operations, is_reverse) # is_reverse is optional, by default = True
```
Пример использования:
```commandline
test_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(test_list))
    print(filter_by_state(test_list, "CANCELED"))
    print(sort_by_date(test_list))
    print(sort_by_date(test_list, False))
    
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]  
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
[{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```
## Документация
Дополнительную информацию о структуре проекта и API можно найти
в [документации](README.md).
