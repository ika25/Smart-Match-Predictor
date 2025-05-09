import pandas as pd

from sklearn.preprocessing import LabelEncoder
def load_real_data(file_path):
    """
    Load Premier League match data from a CSV file.
    """
    df = pd.read_csv(file_path)
    # Example: select needed columns (adapt as needed)
    df = df[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]
    return df

def preprocess_data(df):
    le = LabelEncoder()
    df['HomeTeam_enc'] = le.fit_transform(df['HomeTeam'])
    df['AwayTeam_enc'] = le.transform(df['AwayTeam'])
    df['FTR_enc'] = le.fit_transform(df['FTR'])
    return df
