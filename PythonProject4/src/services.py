import json
import logging

import requests


def get_currency_rates() -> dict:
    """
    Получает текущие курсы валют.

    Returns:
        dict: Словарь с курсами валют.
    """
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as exc:
        logging.error("Error fetching currency rates: %s", exc)
        return {}


def profitable_cashback_categories(year: int, month: int, transactions: list) -> str:
    """
    Рассчитывает выгодные категории повышенного кешбэка.

    Args:
        year (int): Год расчета.
        month (int): Месяц расчета.
        transactions (list): Список транзакций.

    Returns:
        str: JSON-ответ с результатом.
    """
    result = {}
    return json.dumps(result)


def invest_savings(month: int, transactions: list, rounding_limit: float) -> str:
    """
    Рассчитывает сбережения на основе транзакций.

    Args:
        month (int): Месяц расчета.
        transactions (list): Список транзакций.
        rounding_limit (float): Лимит округления.

    Returns:
        str: JSON-ответ с результатом.
    """
    result = {}
    return json.dumps(result)