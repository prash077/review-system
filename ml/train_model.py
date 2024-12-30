from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

texts = [
    "I love this product",  # Positive
    "This is the best thing I’ve ever bought",  # Positive
    "Absolutely fantastic service",  # Positive
    "Terrible experience",  # Negative
    "I hate it",  # Negative
    "Not worth the money",  # Negative
    "Awful quality",  # Negative
]
labels = [1, 1, 1, 0, 0, 0, 0]

pipeline = make_pipeline(CountVectorizer(), MultinomialNB())

pipeline.fit(texts, labels)

joblib.dump(pipeline, 'sentiment_model.pkl')
print("Model saved as 'sentiment_model.pkl'")
