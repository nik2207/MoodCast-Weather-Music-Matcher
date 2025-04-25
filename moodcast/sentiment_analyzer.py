from transformers import pipeline

# Force PyTorch
sentiment_pipeline = pipeline("sentiment-analysis", framework="pt")

def get_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']


