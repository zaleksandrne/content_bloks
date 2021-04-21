from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )


urlpatterns = [
    path("", views.index, name="index"),
    path("senf_email/",
         views.send_email,
         name="send_email"
         ),
    path('api/v1/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    ]
