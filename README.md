---

# 🌧️ Rain Prediction Using Machine Learning

This project predicts whether it will **rain tomorrow** using **Machine Learning models** — **Naive Bayes** and **Random Forest** — trained on key weather parameters such as **Humidity**, **Temperature**, **Wind Speed**, and **Pressure**.
The project includes an interactive **Gradio web app** for easy experimentation and visualization.

---

## 🚀 Features

* 🌦️ **Rain Prediction** using **Naive Bayes** and **Random Forest** classifiers
* 🧠 **Pre-trained models** and **scaler** for consistent and reproducible predictions
* 💻 **Interactive Gradio web interface** for real-time prediction
* 📊 **Input Features:** Humidity, Temperature, Wind Speed, and Pressure
* 🔄 Switch between different ML models directly in the UI

---

## 🗂️ File Structure

| File                                          | Description                                         |
| --------------------------------------------- | --------------------------------------------------- |
| **app.py**                                    | Gradio web application for rain prediction          |
| **requirements.txt**                          | Python dependencies                                 |
| **naive_bayes_model.pkl**                     | Trained Naive Bayes model                           |
| **random_forest_model.pkl**                   | Trained Random Forest model                         |
| **scaler.pkl**                                | Feature scaler used during training                 |
| **mazhai.ipynb**                              | Jupyter notebook for model training and experiments |
| **usa_rain_prediction_dataset_2024_2025.csv** | Dataset used for training and evaluation            |

---

## 🧩 Project Workflow

1. **Load Models and Scaler** — Pre-trained models and scaler are loaded at startup.
2. **User Input** — Users provide weather parameters via the Gradio UI.
3. **Data Scaling** — Inputs are scaled using the original scaler.
4. **Prediction** — The selected model predicts if it will rain tomorrow.
5. **Output** — Displays the prediction result (`Rain` / `No Rain`) interactively.

---

## 📈 Dataset

* **Name:** `usa_rain_prediction_dataset_2024_2025.csv`
* **Content:** Contains daily weather data such as humidity, temperature, wind speed, precipitation, cloud cover, pressure, and the rain label (`Rain Tomorrow`).
* **Purpose:** Used for training and validating the rain prediction models.

---

## 🧪 Models Used

* **Naive Bayes Classifier**

  * Simple and fast probabilistic model.
  * Works well with small datasets.

* **Random Forest Classifier**

  * Ensemble-based model offering high accuracy.
  * Handles feature interactions effectively.

---

## 🛠️ Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🌐 Demo

👉 Try the live demo on **Hugging Face Spaces:**
🔗 [Rain Prediction App](https://huggingface.co/spaces/venmugilrajan/Rain_Prediction)

---

## 🪪 License

This project is open-source and available under the **MIT License**.
Feel free to modify and use it for learning or research purposes.

---

