from django.shortcuts import render
from .models import Review
from ml.predict import predict_sentiment

def index(request):
    if request.method == 'POST':
        text = request.POST.get('review_text')
        sentiment = predict_sentiment(text)
        review = Review.objects.create(text=text, sentiment=sentiment)
        return render(request, 'reviews/results.html', {'review': review})
    return render(request, 'reviews/index.html')


def review(request):
    if request.method == 'POST':
        text = request.POST.get('review_text')
        sentiment = predict_sentiment(text)
        return render(request, 'review_form.html', {'text': text, 'sentiment': sentiment})
    return render(request, 'review_form.html')

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})