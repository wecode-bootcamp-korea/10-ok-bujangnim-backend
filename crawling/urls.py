from django.urls import path,include

from crawling import views
urlpatterns = [
    path('', views.get, name ='index'),
]
