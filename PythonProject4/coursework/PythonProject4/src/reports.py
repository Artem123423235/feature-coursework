import json
import pandas as pd


def expenses_by_category(df: pd.DataFrame, category: str, date: str) -> str:
    """
    Подсчитывает расходы по категориям.

    Args:
        df (pd.DataFrame): Входной DataFrame с транзакциями.
        category (str): Запрашиваемая категория.
        date (str): Дата расчета.

    Returns:
        str: JSON-ответ с результатами.
    """
    # Проверяем, пустой ли DataFrame
    if df.empty:
        result = {
            "category": category,
            "date": date,
            "total_expenses": 0,
            "transactions": []
        }
    else:
        # Фильтруем данные по категории и дате
        # Предположим, что DataFrame имеет колонки: 'category', 'date', 'amount'
        filtered_df = df[(df['category'] == category) & (df['date'] == date)]

        if filtered_df.empty:
            result = {
                "category": category,
                "date": date,
                "total_expenses": 0,
                "transactions": []
            }
        else:
            total = filtered_df['amount'].sum()
            transactions = filtered_df.to_dict('records')
            result = {
                "category": category,
                "date": date,
                "total_expenses": float(total),
                "transactions": transactions
            }

    return json.dumps(result)


def expenses_by_day_of_week(df: pd.DataFrame, date: str = None) -> str:
    """
    Подсчитывает расходы по дням недели.

    Args:
        df (pd.DataFrame): Входной DataFrame с транзакциями.
        date (str): Дата расчета.

    Returns:
        str: JSON-ответ с результатами.
    """
    # Логика формирования отчета
    # ...
    return json.dumps(result)
