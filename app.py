from flask import Flask, request, jsonify
import joblib
import lightgbm as lgb
import pandas as pd
import json

app = Flask(__name__)

# =========================
# Load Models & Artifacts
# =========================

LINEAR_MODEL_PATH = "models/linear_model.pkl"
LGB_MODEL_PATH = "models/lightgbm.txt"
ARTIFACT_PATH = "models/artifact.json"

linear_model = joblib.load(LINEAR_MODEL_PATH)
lgb_model = lgb.Booster(model_file=LGB_MODEL_PATH)

with open(ARTIFACT_PATH) as f:
    artifact = json.load(f)

FEATURES = artifact["features"]
WEIGHTS = artifact["ensemble_weights"]

print("✅ Models loaded successfully")

# =========================
# Routes
# =========================

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict():

    payload = request.get_json()

    if payload is None:
        return jsonify({"error": "Invalid or empty JSON payload"}), 400

    # Convert input to DataFrame
    df = pd.DataFrame([payload])

    # Validate features
    missing_features = set(FEATURES) - set(df.columns)
    if missing_features:
        return jsonify({
            "error": f"Missing features: {list(missing_features)}"
        }), 400

    X = df[FEATURES]

    # -------------------------
    # Model Predictions
    # -------------------------

    pred_linear = float(linear_model.predict(X)[0])
    pred_lgb = float(lgb_model.predict(X)[0])

    # Naive fallback uses lag_1
    pred_naive = float(payload.get("lag_1", pred_linear))

    # -------------------------
    # Weighted Ensemble
    # -------------------------

    final_prediction = (
        WEIGHTS["naive"] * pred_naive +
        WEIGHTS["linear"] * pred_linear +
        WEIGHTS["lgb"] * pred_lgb
    )

    return jsonify({
        "prediction": round(final_prediction, 2),
        "components": {
            "naive": round(pred_naive, 2),
            "linear": round(pred_linear, 2),
            "lgb": round(pred_lgb, 2)
        }
    })


# =========================
# Run Server
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
