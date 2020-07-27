from django.urls import path
#from .views import SignUpView, SignInView
from sub import views
urlpatterns = [
    #path('/sign-up',SignUpView.as_view()),
    #path('/sign-in',SignInView.as_view()),
    path('',views.get, name='index')
]
