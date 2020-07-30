from django.urls import path
from .views import SignUpView, SignInView, TokenCheckView

urlpatterns = [
    path('/sign-up',SignUpView.as_view()),
    path('/sign-in',SignInView.as_view()),
    path('/token',TokenCheckView.as_view()),
]
