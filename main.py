import pandas as pd
from fetch_premier_league_api import fetch_multiple_seasons
from Train_Model import train_model
from Predict_New_Match import predict_match
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

def main():
    API_KEY = 'beccff234225471281fc3cfa3bf50ca1'  # Replace with your actual API key
    seasons = [2020, 2021, 2022, 2023]

    # Load Premier League data for multiple seasons
    df = fetch_multiple_seasons(API_KEY, seasons)
    print("Multi-season data loaded successfully.")
    print(df.head())

    # --- Team Encoder ---
    team_encoder = LabelEncoder()
    teams = pd.concat([df['HomeTeam'], df['AwayTeam']]).unique()
    team_encoder.fit(teams)

    df['HomeTeam_enc'] = team_encoder.transform(df['HomeTeam'])
    df['AwayTeam_enc'] = team_encoder.transform(df['AwayTeam'])

    # --- Result Encoder ---
    result_encoder = LabelEncoder()
    df['FTR_enc'] = result_encoder.fit_transform(df['FTR'])

    # Train model and evaluate
    model, X_test, y_test = train_model(df)
    print("Model trained successfully.")

    y_pred = model.predict(X_test)
    y_test_labels = result_encoder.inverse_transform(y_test)
    y_pred_labels = result_encoder.inverse_transform(y_pred)

    print("\n--- Model Evaluation ---")
    print(classification_report(y_test_labels, y_pred_labels))
    print("Accuracy:", accuracy_score(y_test_labels, y_pred_labels))

    # Optional prediction for one match
    home_team = "Liverpool FC"
    away_team = "Chelsea FC"
    result = predict_match(model, home_team, away_team, team_encoder, result_encoder)
    print(f"\nPrediction for {home_team} vs {away_team}: {result}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")