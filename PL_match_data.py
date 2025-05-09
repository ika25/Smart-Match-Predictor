import pandas as pd

# Sample Premier League match data
data = {
    "HomeTeam": ["Man City", "Liverpool", "Arsenal", "Chelsea", "Man United"],
    "AwayTeam": ["Liverpool", "Man City", "Chelsea", "Arsenal", "Spurs"],
    "HomeWinsLast5": [4, 3, 2, 1, 3],
    "AwayWinsLast5": [2, 4, 1, 3, 2],
    "HomeGoalsAvg": [2.8, 2.1, 2.0, 1.2, 1.5],
    "AwayGoalsAvg": [1.9, 2.7, 1.0, 1.3, 1.4],
    "Result": ["HomeWin", "AwayWin", "Draw", "AwayWin", "HomeWin"]
}

df = pd.DataFrame(data)
print(df)
