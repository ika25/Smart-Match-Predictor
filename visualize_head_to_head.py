import matplotlib.pyplot as plt

def visualize_head_to_head(df, team1, team2):
    h2h_matches = df[((df['HomeTeam'] == team1) & (df['AwayTeam'] == team2)) |
                     ((df['HomeTeam'] == team2) & (df['AwayTeam'] == team1))]

    if h2h_matches.empty:
        print(f"No head-to-head history found between {team1} and {team2}.")
        return

    h2h_matches = h2h_matches.sort_values(by='Season')

    outcomes = []
    for _, row in h2h_matches.iterrows():
        winner = "Draw"
        if row['FTR'] == 'H':
            winner = row['HomeTeam']
        elif row['FTR'] == 'A':
            winner = row['AwayTeam']
        outcomes.append(winner)

    seasons = h2h_matches['Season'].astype(str)
    colors = ['green' if winner == team1 else 'blue' if winner == team2 else 'gray' for winner in outcomes]

    plt.figure(figsize=(10, 5))
    plt.bar(seasons, [1]*len(outcomes), color=colors)
    plt.title(f"Head-to-Head History: {team1} vs {team2}")
    plt.xlabel("Season")
    plt.ylabel("Winner (1 = Match)")
    plt.xticks(rotation=45)

    legend_labels = []
    if team1 in outcomes:
        legend_labels.append(plt.Line2D([0], [0], color='green', lw=4, label=team1))
    if team2 in outcomes:
        legend_labels.append(plt.Line2D([0], [0], color='blue', lw=4, label=team2))
    if "Draw" in outcomes:
        legend_labels.append(plt.Line2D([0], [0], color='gray', lw=4, label='Draw'))

    plt.legend(handles=legend_labels, loc='upper left')
    plt.tight_layout()
    plt.show()
