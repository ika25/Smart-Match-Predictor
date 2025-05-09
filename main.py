import pandas as pd
from fetch_premier_league_api import fetch_multiple_seasons
from Train_Model import train_model
from Predict_New_Match import predict_match
from Preprocess_Data import preprocess_data
from sklearn.metrics import classification_report, accuracy_score

def main():
    API_KEY = 'beccff234225471281fc3cfa3bf50ca1'  # Replace with your actual API key
    seasons = [2020, 2021, 2022, 2023, 2024, 2025]  # Example seasons

    # Load data
    df = fetch_multiple_seasons(API_KEY, seasons)
    print(f"Loaded {len(df)} matches from {len(seasons)} seasons.")
    print(df.head())

    # Preprocess
    df, team_encoder, result_encoder = preprocess_data(df)

    # Train and evaluate
    model, X_test, y_test = train_model(df)
    print("Model trained successfully.")

    y_pred = model.predict(X_test)
    y_test_labels = result_encoder.inverse_transform(y_test)
    y_pred_labels = result_encoder.inverse_transform(y_pred)

    print("\n--- Model Evaluation ---")
    print(classification_report(y_test_labels, y_pred_labels))
    print("Accuracy:", accuracy_score(y_test_labels, y_pred_labels))

    # Optional prediction
    home_team = "Liverpool FC"
    away_team = "Chelsea FC"
    result = predict_match(model, home_team, away_team, team_encoder, result_encoder)
    print(f"\nPrediction for {home_team} vs {away_team}: {result}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")