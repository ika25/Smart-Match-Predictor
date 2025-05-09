import pandas as pd
import matplotlib.pyplot as plt

def predict_match(model, home_team, away_team, team_encoder, result_encoder):
    home_enc = team_encoder.transform([home_team])[0]
    away_enc = team_encoder.transform([away_team])[0]

    input_df = pd.DataFrame([[home_enc, away_enc]], columns=['HomeTeam_enc', 'AwayTeam_enc'])

    # Predict probabilities
    proba = model.predict_proba(input_df)[0]
    predicted_class = model.predict(input_df)[0]
    predicted_label = result_encoder.inverse_transform([predicted_class])[0]

    # Decode class labels
    class_labels = result_encoder.inverse_transform(model.classes_)

    # Visualization
    plt.figure(figsize=(6, 4))
    plt.bar(class_labels, proba, color='skyblue')
    plt.title(f"Prediction Confidence: {home_team} vs {away_team}")
    plt.xlabel("Match Outcome")
    plt.ylabel("Probability")
    plt.ylim(0, 1)
    for i, v in enumerate(proba):
        plt.text(i, v + 0.01, f"{v:.2f}", ha='center')
    plt.tight_layout()
    plt.show()

    return predicted_label



