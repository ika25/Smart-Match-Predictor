import requests
import pandas as pd
from fetch_premier_league_api import fetch_league_matches
from Train_Model import train_model
from Predict_New_Match import predict_match
from Preprocess_Data import preprocess_data

def fetch_league_teams(api_key, league_code):
    headers = {'X-Auth-Token': api_key}
    url = f'https://api.football-data.org/v4/competitions/{league_code}/teams'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Failed to fetch team list: {response.status_code}")
        return []

    data = response.json()
    return [team["name"] for team in data.get("teams", [])]

def run_prediction():
    API_KEY = 'beccff234225471281fc3cfa3bf50ca1'  # Replace with your actual API key
    seasons = [2022, 2023, 2024, 2025]
    league_names = {
        'PL': 'Premier League',
        'PD': 'La Liga',
        'BL1': 'Bundesliga',
        'SA': 'Serie A',
        'FL1': 'Ligue 1'
    }

    print("\nAvailable Leagues:")
    for code, name in league_names.items():
        print(f"  {code}: {name}")

    # Prompt for league until valid input
    selected_league = ""
    while selected_league not in league_names:
        selected_league = input("\nEnter the league code you want to use: ").strip().upper()
        if selected_league not in league_names:
            print("❌ Invalid league code. Try again.")

    # Fetch current teams from API
    print(f"Fetching current teams in {league_names[selected_league]}...")
    teams = fetch_league_teams(API_KEY, selected_league)
    if not teams:
        print("❌ No teams found for this league.")
        return

    team_lookup = {t.lower(): t for t in teams}
    print(f"✅ Found {len(teams)} teams:")

    for team in teams:
        print(f" - {team}")

    # Input home and away teams with retry + case-insensitive match
    home_team = ""
    while home_team.lower() not in team_lookup:
        home_team = input("\nEnter the home team: ").strip()
        if home_team.lower() not in team_lookup:
            print("❌ Invalid team name. Try again.")

    away_team = ""
    while away_team.lower() not in team_lookup or away_team.lower() == home_team.lower():
        away_team = input("Enter the away team: ").strip()
        if away_team.lower() not in team_lookup:
            print("❌ Invalid team name. Try again.")
        elif away_team.lower() == home_team.lower():
            print("❌ Home and away teams must be different.")

    # Correct team names
    home_team = team_lookup[home_team.lower()]
    away_team = team_lookup[away_team.lower()]

    # Fetch historical data to train model
    print("🔄 Fetching match history...")
    df = fetch_league_matches(API_KEY, selected_league, seasons)
    if df.empty:
        print("❌ No match history available.")
        return

    df, team_encoder, result_encoder = preprocess_data(df)
    model, _, _ = train_model(df)

    result = predict_match(model, home_team, away_team, team_encoder, result_encoder)
    print(f"\n🔮 Prediction for {home_team} vs {away_team}: {result}")

def main():
    print("⚽ Welcome to the Interactive Match Predictor ⚽")
    while True:
        run_prediction()
        again = input("\nWould you like to check another match? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ An error occurred: {e}")