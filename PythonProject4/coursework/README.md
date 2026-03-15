Финансовый Аналитик - Python-проект для анализа финансовых операций
Проект предоставляет инструменты для анализа финансовых данных, работы с курсами валют, генерации отчетов и расчета кешбэка.

📁 Структура проекта
PythonProject4/
├── src/                    # Исходный код приложения
│   ├── __init__.py
│   ├── services.py        # Сервисы для работы с API и расчетов
│   ├── reports.py         # Функции для генерации отчетов
│   ├── utils.py           # Вспомогательные утилиты
│   └── views.py           # Веб-интерфейс (если есть)
├── tests/                 # Тесты
│   ├── test_services.py
│   ├── test_reports.py
│   ├── test_utils.py
│   └── test_views.py
├── .venv/                 # Виртуальное окружение
├── requirements.txt       # Зависимости проекта
├── pyproject.toml        # Конфигурация проекта
└── README.md             # Документация
🚀 Быстрый старт
Установка зависимостей
# Создание виртуального окружения
python -m venv .venv

# Активация на Windows
.venv\Scripts\activate

# Активация на MacOS/Linux
source .venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
Запуск тестов
pytest
Запуск приложения
# Если есть веб-интерфейс
python -m src.views

# Или импортируйте модули в своем коде
📊 Основные функции
1. 📈 Курсы валют (services.py)
Получение текущих курсов валют с внешнего API
Обработка ошибок соединения
Кэширование данных
from src.services import get_currency_rates

rates = get_currency_rates()
print(rates)  # {'base': 'USD', 'rates': {'USD': 1.0, 'EUR': 0.9, ...}}
2. 💰 Расчет кешбэка (services.py)
Определение выгодных категорий для повышенного кешбэка
Анализ транзакций по месяцам
Рекомендации по оптимизации расходов
from src.services import profitable_cashback_categories

transactions = [
    {"date": "2023-01-01", "amount": 1000, "category": "Супермаркеты"},
    {"date": "2023-01-02", "amount": 2000, "category": "Транспорт"}
]
result = profitable_cashback_categories(2023, 1, transactions)
3. 🏦 Инвестиционные сбережения (services.py)
Расчет доступных для инвестирования средств
Округление транзакций до заданного лимита
Формирование инвестиционного портфеля
from src.services import invest_savings

transactions = [
    {"date": "2023-01-01", "amount": 123.45, "category": "Еда"},
    {"date": "2023-01-02", "amount": 678.90, "category": "Транспорт"}
]
result = invest_savings(1, transactions, 10.0)
4. 📋 Отчеты по категориям (reports.py)
Детализация расходов по категориям
Фильтрация по датам
Экспорт в JSON-формат
from src.reports import expenses_by_category
import pandas as pd

# Создание DataFrame с транзакциями
df = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-01'],
    'category': ['Супермаркеты', 'Супермаркеты'],
    'amount': [1000, 2000]
})

report = expenses_by_category(df, "Супермаркеты", "2023-01-01")
5. 🛠️ Утилиты (utils.py)
Вспомогательные функции для обработки данных
Форматирование чисел и дат
Валидация входных данных
6. 🌐 Веб-интерфейс (views.py)
REST API для доступа к функциям
Документация API
Примеры запросов
🧪 Тестирование
Проект покрыт тестами для обеспечения надежности:

✅ Тесты сервисов: Проверка работы с API и расчетов
✅ Тесты отчетов: Проверка генерации отчетов
✅ Тесты утилит: Проверка вспомогательных функций
✅ Тесты интерфейса: Проверка веб-интерфейса (если есть)
Запуск всех тестов:

pytest -v
Запуск конкретного модуля тестов:

pytest tests/test_services.py -v
📦 Зависимости
Основные зависимости проекта:

pandas - обработка табличных данных
requests - HTTP-запросы к API
pytest - фреймворк для тестирования
flask/fastapi - веб-фреймворк (если есть веб-интерфейс)
Полный список в requirements.txt

🔧 Конфигурация
Настройки проекта в pyproject.toml:

Версия Python
Зависимости для разработки
Настройки pytest
Настройки линтеров
🐛 Отладка и логирование
Приложение использует стандартный модуль logging для логирования ошибок и важных событий. Уровень логирования можно настроить через переменные окружения.

📝 Пример использования
import pandas as pd
from src.services import get_currency_rates, profitable_cashback_categories
from src.reports import expenses_by_category

# Получение курсов валют
rates = get_currency_rates()
print(f"Курс EUR: {rates.get('rates', {}).get('EUR', 'N/A')}")

# Анализ транзакций
transactions = [
    {"date": "2023-01-01", "amount": 1500, "category": "Рестораны"},
    {"date": "2023-01-02", "amount": 3000, "category": "Транспорт"},
    {"date": "2023-01-03", "amount": 500, "category": "Супермаркеты"}
]

cashback_analysis = profitable_cashback_categories(2023, 1, transactions)
print(f"Рекомендации по кешбэку: {cashback_analysis}")

# Генерация отчета
df = pd.DataFrame(transactions)
report = expenses_by_category(df, "Рестораны", "2023-01-01")
print(f"Отчет по расходам: {report}")
