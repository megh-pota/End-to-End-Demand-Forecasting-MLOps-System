# 🧠 End-to-End Demand Forecasting & MLOps System --- Technical Documentation

This document explains the internal design, coding logic, and
engineering decisions behind the DemandForge system.

------------------------------------------------------------------------

## 📂 Contents

1.  Notebook Pipeline Architecture\
2.  Phase-by-Phase Code Logic\
3.  Feature Engineering Design\
4.  Leakage Prevention Strategy\
5.  Model Training & Evaluation\
6.  Hyperparameter Tuning\
7.  Ensemble Logic\
8.  Monitoring Logic\
9.  Flask API (app.py)\
10. Response Layer (response.py)\
11. API Tests (test_app.py)\
12. CI Pipeline

------------------------------------------------------------------------

## 🧪 1. Notebook Pipeline Architecture

Raw Data → Cleaning → Time Validation → Missing Date Handling → Feature
Engineering → Train/Validation Split → Baseline Models → Advanced Models
→ Ensemble → Monitoring Simulation

------------------------------------------------------------------------

## 🔍 2. Phase-by-Phase Code Logic

### Phase 1 --- Data Loading & Cleaning

-   Load CSV data
-   Convert date columns to datetime
-   Remove negative quantities
-   Aggregate demand per date

### Phase 2 --- Time Validation

-   Create continuous date range
-   Detect missing dates
-   Reindex to fill gaps

### Phase 3 --- Feature Engineering

-   Calendar features: dayofweek, week, month
-   Cyclical encoding: sin/cos transforms
-   Lag features: lag_1, lag_7, lag_14, lag_28
-   Rolling statistics: mean and std
-   Momentum features

------------------------------------------------------------------------

## 🛡️ 4. Leakage Prevention Strategy

-   Use shift before rolling features
-   Strict time-based split
-   No future information leakage

------------------------------------------------------------------------

## 🤖 5. Model Training & Evaluation

Models used: - Naive baseline - Linear Regression - LightGBM

Metrics: - MAE - RMSE - MAPE

------------------------------------------------------------------------

## 🎯 6. Hyperparameter Tuning

Optuna optimization on: - learning_rate - num_leaves -
feature_fraction - bagging_fraction

------------------------------------------------------------------------

## 🧩 7. Ensemble Logic

Weighted average of model predictions for robustness.

------------------------------------------------------------------------

## 📊 8. Monitoring Logic

-   Drift detection using KS test
-   Rolling MAE monitoring
-   Alert threshold triggers retraining

------------------------------------------------------------------------

## 🌐 9. Flask API --- app.py

-   Loads trained models
-   Validates input schema
-   Generates predictions
-   Serves endpoints /health and /predict

------------------------------------------------------------------------

## 📦 10. Response Layer --- response.py

-   Centralized response formatting
-   Consistent JSON schema
-   Error handling helpers

------------------------------------------------------------------------

## 🧪 11. API Tests --- test_app.py

-   Validates health endpoint
-   Validates prediction endpoint
-   Prevents regression

------------------------------------------------------------------------

## ⚙️ 12. CI Pipeline

-   GitHub Actions
-   Automated testing
-   Dependency installation
