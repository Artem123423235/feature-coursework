import json
import requests
import logging
from datetime import datetime
from src.utils import get_card_data, get_top_transactions


def generate_json_response(date_input: str) -> str:
    """
    Генерирует JSON-ответ для страницы 'Главная'.

    Args:
        date_input (str): Дата и время в формате 'YYYY-MM-DD HH:MM:SS'.

    Returns:
        str: JSON-ответ.
    """
    logging.info("Generating JSON response for date: %s", date_input)
    dt = datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S')

    response = {
        "greeting": greeting_message(dt),
        "cards": get_card_data(),
        "top_transactions": get_top_transactions(),
        "currency_rates": fetch_currency_rates(),
        "stock_prices": fetch_stock_prices(),
    }

    return json.dumps(response)


def greeting_message(dt: datetime) -> str:
    if 5 <= dt.hour < 12:
        return "Доброе утро"
    elif 12 <= dt.hour < 18:
        return "Добрый день"
    elif 18 <= dt.hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def fetch_currency_rates() -> dict:
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        return response.json()['rates']
    except Exception as e:
        logging.error("Error fetching currency rates: %s", e)
        return {}


def fetch_stock_prices() -> dict:
    # Здесь должен быть реальный API
    return {"AAPL": 150.0, "AMZN": 3200.0, "GOOGL": 2700.0}  # Пример
