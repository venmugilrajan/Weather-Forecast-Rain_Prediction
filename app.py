import gradio as gr
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# --- Load saved models and the scaler ---
try:
    nb_model = joblib.load("naive_bayes_model.pkl")
    rf_model = joblib.load("random_forest_model.pkl")
    scaler = joblib.load("scaler.pkl")
except FileNotFoundError:
    print("Error: Model or scaler files not found. Make sure the .pkl files are in the same directory.")
    exit()

# --- Prediction Function ---
def predict_weather(model_choice, humidity, temperature, wind_speed, pressure):
    input_data = pd.DataFrame(
        [[humidity, temperature, wind_speed, pressure]],
        columns=['Humidity', 'Temperature', 'Wind Speed', 'Pressure']
    )
    input_data_scaled = scaler.transform(input_data)
    if model_choice == "Naive Bayes":
        model = nb_model
    else:
        model = rf_model
    prediction = model.predict(input_data_scaled)[0]
    return f"🌧️ Rain Tomorrow: {'Yes' if prediction == 1 else 'No'} (Model: {model_choice})"

# --- Gradio Interface ---
iface = gr.Interface(
    fn=predict_weather,
    inputs=[
        gr.Radio(["Naive Bayes", "Random Forest"], label="Choose Model"),
        gr.Number(label="Humidity"),
        gr.Number(label="Temperature"),
        gr.Number(label="Wind Speed"),
        gr.Number(label="Pressure"),
    ],
    outputs="text",
    title="Rain Prediction using ML Models",
    description="Predict whether it will rain tomorrow using Naive Bayes or Random Forest.",
    theme="soft"
)

# --- Launch App ---
if __name__ == "__main__":
    iface.launch()
