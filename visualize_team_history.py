import matplotlib.pyplot as plt
import os

def visualize_team_history(df, team_name, filename='static/team_history.png'):
    team_matches = df[(df['HomeTeam'] == team_name) | (df['AwayTeam'] == team_name)].copy()

    if team_matches.empty:
        print(f"No match history found for {team_name}.")
        return None

    team_matches['TeamGoals'] = team_matches.apply(
        lambda row: row['FTHG'] if row['HomeTeam'] == team_name else row['FTAG'], axis=1
    )
    team_matches['OpponentGoals'] = team_matches.apply(
        lambda row: row['FTAG'] if row['HomeTeam'] == team_name else row['FTHG'], axis=1
    )

    season_stats = (
        team_matches
        .groupby('Season')
        .agg({
            'FTR': 'count',
            'TeamGoals': 'sum',
            'OpponentGoals': 'sum'
        })
        .rename(columns={'FTR': 'Matches'})
        .reset_index()
    )

    # Plot
    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax1.bar(season_stats['Season'], season_stats['Matches'], alpha=0.6, label='Matches Played', color='skyblue')
    ax1.set_ylabel('Matches Played')
    ax1.set_xlabel('Season')
    ax1.set_title(f"{team_name} - Match History by Season")
    ax1.tick_params(axis='x', rotation=45)

    ax2 = ax1.twinx()
    ax2.plot(season_stats['Season'], season_stats['TeamGoals'], label='Goals Scored', color='green', marker='o')
    ax2.plot(season_stats['Season'], season_stats['OpponentGoals'], label='Goals Conceded', color='red', marker='o')
    ax2.set_ylabel('Goals')

    fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
    plt.tight_layout()

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename)
    plt.close()
    return filename