import json
from src.views import generate_json_response


def test_generate_json_response():
    response = generate_json_response("2023-10-01 10:30:00")
    data = json.loads(response)

    assert isinstance(data, dict)
    assert "greeting" in data
    assert "cards" in data
    assert "top_transactions" in data
