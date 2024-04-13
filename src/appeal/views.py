from django.shortcuts import render
from .forms import UserFeedbackForm
from django.core.mail import EmailMessage

def user_feedback(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            form.save()

            # Получение данных из формы
            author = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Создание объекта EmailMessage
            subject = 'Новое обращение от пользователя'
            body = f'Автор: {author}\nEmail: {email}\nОбращение: {message}'
            from_email = 'karimknewit@gmail.com'  # Отправитель по умолчанию
            recipient_list = ['abdukarim600@gmail.com',]  # Список получателей

            email = EmailMessage(subject, body, from_email, recipient_list)
            email.send()

            return render(request, 'feedback/thank_you.html')
    else: 
        form = UserFeedbackForm() 
    return render(request, 'feedback/user_feedback_form.html', {'form': form})

