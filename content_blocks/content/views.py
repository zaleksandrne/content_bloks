from django.shortcuts import get_object_or_404, render 
from .models import Block_1, Block_2, Block_3, Sorting
from django.contrib.auth import get_user_model
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

User = get_user_model()


def index(request):
    users_count = User.objects.all().count
    blocks1 = list(Block_1.objects.values())
    blocks2 = list(Block_2.objects.values())
    blocks3 = list(Block_3.objects.values())
    blocks = blocks1 + blocks2 + blocks3
    sort = get_object_or_404(Sorting, id=1).sort_field
    sorted_blocks = sorted(blocks, key=lambda k: k[sort])
    return render(
         request,
         'index.html',
         {"users_count": users_count,
          "blocks1": blocks1,
          "blocks2": blocks2,
          "blocks3": blocks3,
          'blocks': sorted_blocks})


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
            return HttpResponse('Ошибка запроса')
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Проверьте, что в вашем профиле указана почта')
