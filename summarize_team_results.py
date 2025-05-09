
def summarize_team_results(df, team_name):
    matches = df[(df['HomeTeam'] == team_name) | (df['AwayTeam'] == team_name)].copy()
    if matches.empty:
        print(f"No results found for {team_name}.")
        return

    results = {'Wins': 0, 'Draws': 0, 'Losses': 0}
    goals_scored = 0
    goals_conceded = 0

    for _, row in matches.iterrows():
        if row['HomeTeam'] == team_name:
            scored = row['FTHG']
            conceded = row['FTAG']
            result = row['FTR']
            if result == 'H':
                results['Wins'] += 1
            elif result == 'D':
                results['Draws'] += 1
            else:
                results['Losses'] += 1
        else:
            scored = row['FTAG']
            conceded = row['FTHG']
            result = row['FTR']
            if result == 'A':
                results['Wins'] += 1
            elif result == 'D':
                results['Draws'] += 1
            else:
                results['Losses'] += 1

        goals_scored += scored
        goals_conceded += conceded

    total = results['Wins'] + results['Draws'] + results['Losses']
    print(f"\n📈 Match Result Summary for {team_name}:")
    print(f"  Matches Played: {total}")
    print(f"  Wins: {results['Wins']}  Draws: {results['Draws']}  Losses: {results['Losses']}")
    print(f"  Total Goals Scored: {goals_scored}  |  Goals Conceded: {goals_conceded}")
    print(f"  Avg Goals Scored: {goals_scored / total:.2f}  |  Avg Goals Conceded: {goals_conceded / total:.2f}")
