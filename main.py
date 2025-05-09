from PL_match_data import load_real_data
from Train_Model import train_model
from Predict_New_Match import predict_match
from sklearn.preprocessing import LabelEncoder

def main():
    # Load real data from a CSV file
    df = load_real_data("E0.csv")  # Make sure this CSV file exists
    
    # Encode team names and results
    label_encoder = LabelEncoder()
    df['HomeTeam_enc'] = label_encoder.fit_transform(df['HomeTeam'])
    df['AwayTeam_enc'] = label_encoder.transform(df['AwayTeam'])
    df['FTR_enc'] = label_encoder.fit_transform(df['FTR'])  # FTR: Full Time Result (H/D/A)

    # Train model
    model = train_model(df)

    # Predict a new match
    home_team = "Arsenal"
    away_team = "Chelsea"
    result = predict_match(model, home_team, away_team, label_encoder)

    print(f"Prediction for {home_team} vs {away_team}: {result}")

if __name__ == "__main__":
    main()
