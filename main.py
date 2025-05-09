from PL_match_data import load_dummy_data
from Train_Model import train_model
from Predict_New_Match import predict_match

def main():
    df = load_dummy_data()
    model, label_encoder, report = train_model(df)
    
    print("Model Evaluation Report:")
    for label, metrics in report.items():
        if isinstance(metrics, dict):
            print(f"{label}: Precision={metrics['precision']:.2f}, Recall={metrics['recall']:.2f}, F1={metrics['f1-score']:.2f}")

    # Example prediction
    result = predict_match(model, label_encoder, home_wins=3, away_wins=2, home_avg_goals=2.2, away_avg_goals=1.4)
    print("\nPrediction for New Match: ", result)

if __name__ == "__main__":
    main()
