import json
from datetime import datetime


def parse_date(date_string: str) -> datetime:
    """
    Парсит входящую строку даты в объект datetime.

    Args:
        date_string (str): Строка с датой в формате 'YYYY-MM-DD HH:MM:SS'.

    Returns:
        datetime: Объект datetime.
    """
    return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')


def get_card_data() -> list:
    """
    Возвращает данные о картах.

    Returns:
        list: Список словарей с данными карт.
    """
    return [
        {"last_four_digits": "1234", "total": 15000, "cashback": 150},
        {"last_four_digits": "5678", "total": 20000, "cashback": 200},
    ]


def get_top_transactions() -> list:
    """
    Возвращает данные о топовых транзакциях.

    Returns:
        list: Список словарей с данными транзакций.
    """
    return [
        {"transaction": "Ресторан", "amount": 5000},
        {"transaction": "Супермаркет", "amount": 3000},
        {"transaction": "Такси", "amount": 1500},
        {"transaction": "Кино", "amount": 1200},
        {"transaction": "Аптека", "amount": 800},
    ]
