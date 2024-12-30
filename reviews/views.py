# from django.shortcuts import render
# from .forms import ReviewForm
# from .models import Review
# from ml.predict import predict_sentiment

# def index(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.sentiment = predict_sentiment(review.text)
#             review.save()
#     else:
#         form = ReviewForm()

#     reviews = Review.objects.all()
#     return render(request, 'index.html', {'form': form, 'reviews': reviews})
