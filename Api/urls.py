from django.urls import path
from .views import AuthView



urlpatterns = [
    path("auth/",view=AuthView.as_view(), name="auth"),
]
