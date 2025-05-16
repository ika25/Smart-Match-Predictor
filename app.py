from flask import Flask, render_template, request
from fetch_premier_league_api import fetch_league_matches
from Train_Model import train_model
from Predict_New_Match import predict_match
from Preprocess_Data import preprocess_data
from visualize_team_history import visualize_team_history
from visualize_head_to_head import visualize_head_to_head
from summarize_team_results import summarize_team_results

import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

LEAGUES = {
    'PL': 'Premier League',
    'PD': 'La Liga',
    'BL1': 'Bundesliga',
    'SA': 'Serie A',
    'FL1': 'Ligue 1'
}

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    league_code = request.form.get("league")
    home_team = request.form.get("home_team")
    away_team = request.form.get("away_team")
    team_list = []
    team1_chart = team2_chart = h2h_chart = None

    if league_code:
        seasons = list(range(2010, datetime.now().year + 1))
        df = fetch_league_matches(API_KEY, league_code, seasons)
        if not df.empty:
            team_list = sorted(set(df['HomeTeam']).union(df['AwayTeam']))
            if home_team and away_team and home_team != away_team:
                print("🔄 Generating charts...")

                team1_chart = visualize_team_history(df, home_team, filename='static/team1_chart.html')
                team2_chart = visualize_team_history(df, away_team, filename='static/team2_chart.html')
                h2h_chart = visualize_head_to_head(df, home_team, away_team, filename='static/h2h_chart.html')

                print("✅ Chart files created:", team1_chart, team2_chart, h2h_chart)

                summarize_team_results(df, home_team)
                summarize_team_results(df, away_team)
                df, team_encoder, result_encoder = preprocess_data(df)
                model, _, _ = train_model(df)

                if home_team in team_encoder.classes_ and away_team in team_encoder.classes_:
                    prediction = predict_match(model, home_team, away_team, team_encoder, result_encoder)

    return render_template(
        "index.html",
        leagues=LEAGUES,
        teams=team_list,
        prediction=prediction,
        team1_chart=team1_chart,
        team2_chart=team2_chart,
        h2h_chart=h2h_chart
    )

if __name__ == "__main__":
    app.run(debug=True)
