from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
# filepath: c:\Users\krich\Desktop\Smart Match Predictor\Smart-Match-Predictor\Train_Model.py
from PL_match_data import df


def train_model(df):
    features = df[["HomeWinsLast5", "AwayWinsLast5", "HomeGoalsAvg", "AwayGoalsAvg"]]
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(df["Result"])

    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions, target_names=label_encoder.classes_, output_dict=True)

    return model, label_encoder, report

# Export the DataFrame
__all__ = ["df"]