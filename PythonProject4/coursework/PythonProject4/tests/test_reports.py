import pandas as pd
from datetime import datetime
import json
from src.reports import expenses_by_category


def test_expenses_by_category():
    """Тест для функции расходов по категориям"""
    # Преобразуем дату в строку, так как функция ожидает строку
    date_str = "2023-01-01"

    # Создаем пустой DataFrame с нужными колонками
    df = pd.DataFrame(columns=['date', 'category', 'amount'])

    result = expenses_by_category(df, "Супермаркеты", date_str)

    # Проверяем, что результат - строка JSON
    assert isinstance(result, str)

    # Парсим JSON и проверяем структуру
    data = json.loads(result)
    assert isinstance(data, dict)
    assert "category" in data
    assert data["category"] == "Супермаркеты"
    assert "date" in data
    assert data["date"] == date_str
    assert "total_expenses" in data
    assert data["total_expenses"] == 0