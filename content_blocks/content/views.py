from django.shortcuts import render

from .models import Block_1, Block_2, Block_3


def index(request):
    blocks1 = Block_1.objects.all()
    blocks2 = Block_2.objects.all()
    blocks3 = Block_3.objects.all()
    return render(
         request,
         "index.html",
         {"blocks1": blocks1, "blocks2": blocks2, "blocks3": blocks3}
     )
