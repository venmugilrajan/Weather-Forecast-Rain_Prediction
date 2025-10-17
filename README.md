# 🌧️Rain Prediction Using Machine Learning
This project predicts whether it will rain tomorrow using machine learning models (Naive Bayes and Random Forest) trained on weather data features such as humidity, temperature, wind speed, and pressure. The web app is powered by Gradio for an interactive experience.

Features
Predicts next-day rain using Naive Bayes and Random Forest classifiers.

Interactive web interface via Gradio.

Input features: Humidity, Temperature, Wind Speed, Pressure.

Includes pre-trained models and scaler for reproducibility.

File Structure
File	Purpose
app.py	Gradio web application for prediction
requirements.txt	Python dependencies list
naive_bayes_model.pkl	Saved Naive Bayes model
random_forest_model.pkl	Saved Random Forest model
scaler.pkl	Saved feature scaler
mazhai.ipynb	Training and experiments notebook
usa_rain_prediction_dataset_2024_2025.csv	Dataset
Project Workflow
Load trained models and scaler.

Accept user inputs for weather features in the UI.

Scale input data using the original scaler.

Predict rain outcome with selected model.

Dataset
Uses usa_rain_prediction_dataset_2024_2025.csv featuring weather metrics and target labels for rain prediction.

License
This repository is open source and licensed under MIT.
