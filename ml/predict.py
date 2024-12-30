import joblib

model = joblib.load('ml/sentiment_model.pkl')

def predict_sentiment(text):
    """Predicts the sentiment of the given text."""
    prediction = model.predict([text])
    return "Positive" if prediction[0] == 1 else "Negative"
