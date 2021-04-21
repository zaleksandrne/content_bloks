from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("senf_email/",
         views.send_email,
         name="send_email"
         ),
    ]