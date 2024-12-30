from predict import predict_sentiment

test_text = "I absolutely love this product!"
print(f"Text: {test_text}")
print(f"Sentiment: {predict_sentiment(test_text)}")
