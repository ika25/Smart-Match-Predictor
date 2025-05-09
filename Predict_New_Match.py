import pandas as pd

def predict_match(model, label_encoder, home_wins, away_wins, home_avg_goals, away_avg_goals):
    new_match = pd.DataFrame({
        "HomeWinsLast5": [home_wins],
        "AwayWinsLast5": [away_wins],
        "HomeGoalsAvg": [home_avg_goals],
        "AwayGoalsAvg": [away_avg_goals]
    })

    prediction = model.predict(new_match)
    return label_encoder.inverse_transform(prediction)[0]
