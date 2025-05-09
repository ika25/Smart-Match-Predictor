
import matplotlib.pyplot as plt

def visualize_team_history(df, team_name):
    team_matches = df[(df['HomeTeam'] == team_name) | (df['AwayTeam'] == team_name)]

    if team_matches.empty:
        print(f"No match history found for {team_name}.")
        return

    # Count matches and goals per season
    season_stats = (
        team_matches
        .groupby('Season')
        .agg(
            Matches=('FTR', 'count'),
            GoalsScored=lambda x: (
                team_matches.loc[x.index, 'FTHG'] * (team_matches.loc[x.index, 'HomeTeam'] == team_name) +
                team_matches.loc[x.index, 'FTAG'] * (team_matches.loc[x.index, 'AwayTeam'] == team_name)
            ).sum(),
            GoalsConceded=lambda x: (
                team_matches.loc[x.index, 'FTAG'] * (team_matches.loc[x.index, 'HomeTeam'] == team_name) +
                team_matches.loc[x.index, 'FTHG'] * (team_matches.loc[x.index, 'AwayTeam'] == team_name)
            ).sum()
        )
        .reset_index()
    )

    # Plotting
    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.bar(season_stats['Season'], season_stats['Matches'], alpha=0.6, label='Matches Played', color='skyblue')
    ax1.set_ylabel('Matches Played')
    ax1.set_xlabel('Season')
    ax1.set_title(f"{team_name} - Match History by Season")
    ax1.tick_params(axis='x', rotation=45)

    # Overlay goals scored and conceded
    ax2 = ax1.twinx()
    ax2.plot(season_stats['Season'], season_stats['GoalsScored'], label='Goals Scored', color='green', marker='o')
    ax2.plot(season_stats['Season'], season_stats['GoalsConceded'], label='Goals Conceded', color='red', marker='o')
    ax2.set_ylabel('Goals')

    fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
    plt.tight_layout()
    plt.show()
