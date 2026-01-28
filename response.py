import requests

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

r = requests.post("http://127.0.0.1:5000/predict", json=payload)
print(r.json())
