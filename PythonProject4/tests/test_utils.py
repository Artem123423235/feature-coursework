import pytest
from src.utils import parse_date, get_card_data, get_top_transactions

def test_parse_date():
    date_string = "2023-10-01 10:30:00"
    parsed_date = parse_date(date_string)
    assert parsed_date.year == 2023

def test_get_card_data():
    cards = get_card_data()
    assert len(cards) == 2

def test_get_top_transactions():
    transactions = get_top_transactions()
    assert len(transactions) == 5
