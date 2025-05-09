import pandas as pd

def predict_match(model, home_team, away_team, le):
    home_team_enc = le.transform([home_team])[0]
    away_team_enc = le.transform([away_team])[0]
    prediction = model.predict([[home_team_enc, away_team_enc]])
    return le.inverse_transform(prediction)[0]

