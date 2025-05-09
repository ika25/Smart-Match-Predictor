import pandas as pd
from fetch_premier_league_api import fetch_league_matches
from Train_Model import train_model
from Predict_New_Match import predict_match
from Preprocess_Data import preprocess_data

def main():
    API_KEY = 'beccff234225471281fc3cfa3bf50ca1'  # Replace with your actual API key
    seasons = [2019, 2020, 2021, 2022, 2023]
    league_names = {
        'PL': 'Premier League',
        'PD': 'La Liga',
        'BL1': 'Bundesliga',
        'SA': 'Serie A',
        'FL1': 'Ligue 1'
    }

    print("Available Leagues:")
    for code, name in league_names.items():
        print(f"  {code}: {name}")

    selected_league = input("\nEnter the league code you want to use: ").strip().upper()
    if selected_league not in league_names:
        print("❌ Invalid league code. Exiting.")
        return

    print(f"Fetching data for {league_names[selected_league]}...")
    df = fetch_league_matches(API_KEY, selected_league, seasons)
    if df.empty:
        print("❌ No data found for this league.")
        return

    print(f"✅ Loaded {len(df)} matches from {league_names[selected_league]}.")

    # Show available teams
    teams = sorted(set(df['HomeTeam']).union(set(df['AwayTeam'])))
    print("\nAvailable teams in this league:")
    for team in teams:
        print(f" - {team}")

    # User inputs for home and away teams
    home_team = input("\nEnter the home team: ").strip()
    away_team = input("Enter the away team: ").strip()

    if home_team not in teams or away_team not in teams:
        print("❌ One or both teams are not valid for this league.")
        return

    # Preprocess and predict
    df, team_encoder, result_encoder = preprocess_data(df)
    model, _, _ = train_model(df)

    result = predict_match(model, home_team, away_team, team_encoder, result_encoder)
    print(f"\n🔮 Prediction for {home_team} vs {away_team}: {result}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ An error occurred: {e}")