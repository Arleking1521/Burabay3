from django.shortcuts import get_object_or_404, render, redirect
from .forms import ReviewForm, AnswerForm
from .models import Reviews, Answer
from django.core.mail import send_mail
# Create your views here.
def review_list(request):
    reviews = Reviews.objects.all()
    for review in reviews:
        answer = Answer.objects.filter(review_id = review.pk)
        review.answer = answer
    return render(request, 'reviewsPages/reviews_list.html', {'reviews':reviews})

def add_review(request):
    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()

            author = form.cleaned_data['author']
            iin = form.cleaned_data['IIN']
            message = form.cleaned_data['review']

            # Отправка письма на почту компании
            subject = f"Новый отзыв от {author}"
            body = f"Автор: {author}\nИИН: {iin}\nОтзыв: {message}"
            from_email = 'karimknewit@gmail.com'
            recipient_list = ['abdukarim600@gmail.com',]  # Список получателей

            send_mail(subject, body, from_email, recipient_list, fail_silently=False)

            return redirect('reviews')  
    return render(request, 'reviewsPages/add_review.html', {'form': form})

def add_answer(request, rid):
    review = get_object_or_404(Reviews, id=rid)
    print(f"review:{review}")
    if request.method != 'POST':
        form = AnswerForm()
    else:
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.review = review
            response.save()
            return redirect('reviews')
    return render(request, 'reviewsPages/add_answer.html', {'review': review, 'form': form})