from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    features = df[['HomeTeam_enc', 'AwayTeam_enc']]
    labels = df['FTR_enc']
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model


# Export the DataFrame
__all__ = ["df"]