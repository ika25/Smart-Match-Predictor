import pandas as pd

from sklearn.preprocessing import LabelEncoder
def load_real_data():
    file_path = r"C:\Users\krich\Desktop\Smart Match Predictor\Smart-Match-Predictor\PL-Data_CSV\E0.csv"  # Use your actual path
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    le = LabelEncoder()
    df['HomeTeam_enc'] = le.fit_transform(df['HomeTeam'])
    df['AwayTeam_enc'] = le.transform(df['AwayTeam'])
    df['FTR_enc'] = le.fit_transform(df['FTR'])
    return df
