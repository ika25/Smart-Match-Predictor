import plotly.graph_objects as go
import pandas as pd
import os

def visualize_team_history(df, team_name, filename='static/team1_chart.html'):
    print(f"📊 [Plotly] visualize_team_history() called for {team_name}")

    team_matches = df[(df['HomeTeam'] == team_name) | (df['AwayTeam'] == team_name)].copy()

    if team_matches.empty:
        print(f"⚠️ No match history found for {team_name}. Chart not generated.")
        return None

    # Calculate team goals
    team_matches['TeamGoals'] = team_matches.apply(
        lambda row: row['FTHG'] if row['HomeTeam'] == team_name else row['FTAG'], axis=1)
    team_matches['OpponentGoals'] = team_matches.apply(
        lambda row: row['FTAG'] if row['HomeTeam'] == team_name else row['FTHG'], axis=1)

    # Group by season
    season_stats = (
        team_matches
        .groupby('Season')
        .agg(Matches=('FTR', 'count'), GoalsScored=('TeamGoals', 'sum'), GoalsConceded=('OpponentGoals', 'sum'))
        .reset_index()
    )

    # Plot using Plotly
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=season_stats['Season'],
        y=season_stats['Matches'],
        name='Matches Played',
        marker_color='lightblue'
    ))

    fig.add_trace(go.Scatter(
        x=season_stats['Season'],
        y=season_stats['GoalsScored'],
        mode='lines+markers',
        name='Goals Scored',
        line=dict(color='green')
    ))

    fig.add_trace(go.Scatter(
        x=season_stats['Season'],
        y=season_stats['GoalsConceded'],
        mode='lines+markers',
        name='Goals Conceded',
        line=dict(color='red')
    ))

    fig.update_layout(
        title=f"{team_name} - Match History by Season",
        xaxis_title='Season',
        yaxis_title='Count',
        template='plotly_white',
        legend=dict(x=0.01, y=0.99)
    )

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fig.write_html(filename)
    print(f"✅ Plotly chart saved: {filename}")
    return filename