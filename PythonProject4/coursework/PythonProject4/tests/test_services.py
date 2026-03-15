import requests
from unittest.mock import patch
from src.services import get_currency_rates, profitable_cashback_categories, invest_savings


@patch("src.services.requests.get")
def test_get_currency_rates_success(mock_get):
    mock_get.return_value.json.return_value = {
        "base": "USD",
        "rates": {"USD": 1.0, "EUR": 0.9},
    }
    mock_get.return_value.status_code = 200

    rates = get_currency_rates()

    assert "rates" in rates
    assert "USD" in rates["rates"]
    assert rates["base"] == "USD"


@patch("src.services.requests.get")
def test_get_currency_rates_failure(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("API Error")

    rates = get_currency_rates()
    assert rates == {}


# Удален тест get_stock_prices, т.к. такой функции нет
# def test_get_stock_prices():
#     prices = get_stock_prices()
#     assert isinstance(prices, dict)

def test_profitable_cashback_categories():
    """Тест для profitable_cashback_categories"""
    transactions = [
        {"date": "2023-01-01", "amount": 1000, "category": "Еда"},
        {"date": "2023-01-02", "amount": 2000, "category": "Транспорт"}
    ]

    result = profitable_cashback_categories(2023, 1, transactions)
    assert isinstance(result, str)
    import json
    data = json.loads(result)
    assert isinstance(data, dict)


def test_invest_savings():
    """Тест для invest_savings"""
    transactions = [
        {"date": "2023-01-01", "amount": 123.45, "category": "Еда"},
        {"date": "2023-01-02", "amount": 678.90, "category": "Транспорт"}
    ]

    result = invest_savings(1, transactions, 10.0)
    assert isinstance(result, str)
    import json
    data = json.loads(result)
    assert isinstance(data, dict)
