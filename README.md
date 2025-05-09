# ⚽ Premier League Match Predictor (AI Agent Project)

## 🧠 Overview
This project is a fully functional **AI agent** that predicts the outcome of English Premier League matches. It pulls **live data** using an API, **trains a machine learning model**, and returns predictions with **confidence scores** and performance evaluation.

## 🚀 Features
- ✅ Pulls live match data from **football-data.org** across **multiple seasons**
- 🧠 Trains a **Random Forest** classifier to predict outcomes (Win, Draw, Loss)
- 📊 Evaluates model with **classification report** and **accuracy**
- 🔮 Predicts individual match outcomes with **confidence visualization**
- 🧼 Clean, modular Python code (separated into data fetching, preprocessing, training, and predicting)

## 🧰 Tech Stack
- **Python 3.10+**
- `pandas`, `scikit-learn`, `matplotlib`
- **Football-Data.org API**
- (Optional: Streamlit or Flask for web UI)

## 🧠 AI Agent Architecture

| Component   | Role                                              |
|-------------|---------------------------------------------------|
| Perception  | Pulls data from the Premier League via API       |
| Reasoning   | Uses machine learning (Random Forest)            |
| Action      | Predicts match outcomes and explains confidence  |
| Learning    | Improves with multi-season data                  |

## 📈 Example Prediction
```
Prediction for Liverpool FC vs Chelsea FC: H
Confidence:
- Home Win (H): 71%
- Draw (D): 19%
- Away Win (A): 10%
```

## 📁 Project Structure
```
├── main.py                     # Main script to run the AI agent
├── fetch_premier_league_api.py  # API connection and data collection
├── Train_Model.py             # Model training logic
├── Predict_New_Match.py       # Single match prediction + confidence plot
├── Preprocess_Data.py         # Label encoding for teams and results
```

## 💡 Future Additions (Ideas)
- Add team **form metrics** or **player injuries**
- Compare multiple ML models (e.g., XGBoost)
- Deploy as a **Streamlit app** for user input
- Add **automated retraining** on new data