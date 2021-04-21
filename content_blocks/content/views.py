from django.shortcuts import render 
from .models import Block_1, Block_2, Block_3
from django.contrib.auth import get_user_model
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

User = get_user_model()


def index(request):
    users_count = User.objects.all().count
    blocks1 = Block_1.objects.all()
    blocks2 = Block_2.objects.all()
    blocks3 = Block_3.objects.all()
    return render(
         request,
         "index.html",
         {"users_count": users_count,
          "blocks1": blocks1,
          "blocks2": blocks2,
          "blocks3": blocks3})


def send_email(request):
    user = request.user
    from_email = user.email
    if from_email:
        try:
            send_mail('Заявка',
                      f'Пользователь {user} отправил заявку',
                      from_email,
                      ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.info(request, 'Your password has been changed successfully!')
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Проверьте, что в вашем профиле указана почта')
