import joblib

# Load the model
model = joblib.load('ml/sentiment_model.pkl')

def predict_sentiment(text):
    prediction = model.predict([text])[0]
    return 'Positive' if prediction == 1 else 'Negative'
