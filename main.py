import pandas as pd
from PL_match_data import load_real_data
from Train_Model import train_model
from Predict_New_Match import predict_match
from sklearn.preprocessing import LabelEncoder

def main():
    df = load_real_data("C:/Users/krich/Desktop/Smart Match Predictor/Smart-Match-Predictor/PL-Data_CSV/data.csv")
    print("Data loaded successfully.")
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

    # Train model
    model = train_model(df)
    print("Model trained successfully.")

    # Predict a new match
    home_team = "Southampton"
    away_team = "Man City"
    result = predict_match(model, home_team, away_team, team_encoder, result_encoder)

    print(f"Prediction for {home_team} vs {away_team}: {result}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
