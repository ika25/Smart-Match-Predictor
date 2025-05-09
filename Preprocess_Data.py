import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    team_encoder = LabelEncoder()
    result_encoder = LabelEncoder()

    # Fit encoders
    teams = pd.concat([df['HomeTeam'], df['AwayTeam']]).unique()
    team_encoder.fit(teams)

    df['HomeTeam_enc'] = team_encoder.transform(df['HomeTeam'])
    df['AwayTeam_enc'] = team_encoder.transform(df['AwayTeam'])
    df['FTR_enc'] = result_encoder.fit_transform(df['FTR'])

    return df, team_encoder, result_encoder
