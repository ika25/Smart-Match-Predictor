import plotly.graph_objects as go
import pandas as pd
import os

def visualize_head_to_head(df, team1, team2, filename='static/h2h_chart.html'):
    print(f"⚔️ [Plotly] visualize_head_to_head() called for {team1} vs {team2}")
    h2h_matches = df[((df['HomeTeam'] == team1) & (df['AwayTeam'] == team2)) |
                     ((df['HomeTeam'] == team2) & (df['AwayTeam'] == team1))].copy()

    if h2h_matches.empty:
        print(f"⚠️ No head-to-head history found between {team1} and {team2}.")
        return None

    h2h_matches = h2h_matches.sort_values(by='Season')

    seasons = h2h_matches['Season'].astype(str)
    outcomes = []

    for _, row in h2h_matches.iterrows():
        if row['FTR'] == 'H':
            outcomes.append(row['HomeTeam'])
        elif row['FTR'] == 'A':
            outcomes.append(row['AwayTeam'])
        else:
            outcomes.append('Draw')

    counts = {'Draw': 0, team1: 0, team2: 0}
    bar_colors = []

    for winner in outcomes:
        counts[winner] += 1
        bar_colors.append('gray' if winner == 'Draw' else 'green' if winner == team1 else 'blue')

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=seasons,
        y=[1]*len(outcomes),
        marker_color=bar_colors,
        hovertext=outcomes,
        name='Match Result'
    ))

    fig.update_layout(
        title=f"Head-to-Head Results: {team1} vs {team2}",
        xaxis_title='Season',
        yaxis_title='Match Outcome (1 bar = 1 match)',
        showlegend=False,
        template='plotly_white'
    )

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fig.write_html(filename)
    print(f"✅ Plotly chart saved: {filename}")
    return filename

