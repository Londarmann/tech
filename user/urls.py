

from django.urls import path
from .views import LoginAPIView, SignUpAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,

)

urlpatterns = [
    path("register/", SignUpAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

]
