import sys
import os
import json

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from app import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_predict_endpoint():
    client = app.test_client()

    payload = {
        "dayofweek": 2,
        "week": 25,
        "month": 6,
        "is_weekend": 0,
        "dow_sin": 0.43,
        "dow_cos": -0.22,
        "lag_1": 73,
        "lag_7": 69,
        "lag_14": 68,
        "lag_28": 68,
        "roll_mean_7": 77.1,
        "roll_mean_14": 78.7,
        "roll_mean_28": 85.1,
        "roll_std_7": 64.5,
        "roll_std_14": 81.9,
        "roll_std_28": 112.2,
        "momentum_7": 0
    }

    response = client.post(
        "/predict",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 200
    assert "prediction" in response.json
