import requests
import pandas as pd

def fetch_league_matches(api_key, league_code, seasons):
    headers = {'X-Auth-Token': api_key}
    all_matches = []

    for season in seasons:
        print(f"Fetching {league_code} season {season}...")
        url = f'https://api.football-data.org/v4/competitions/{league_code}/matches?season={season}'
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch {league_code} season {season}: {response.status_code}")
            continue

        data = response.json()
        matches = data.get('matches', [])

        for match in matches:
            home = match['homeTeam']['name']
            away = match['awayTeam']['name']
            score = match['score']['fullTime']
            hg = score.get('home')
            ag = score.get('away')

            if hg is not None and ag is not None:
                if hg > ag:
                    result = 'H'
                elif hg < ag:
                    result = 'A'
                else:
                    result = 'D'
                all_matches.append({
                    'HomeTeam': home,
                    'AwayTeam': away,
                    'FTHG': hg,
                    'FTAG': ag,
                    'FTR': result,
                    'Season': season,
                    'League': league_code
                })

    return pd.DataFrame(all_matches)

