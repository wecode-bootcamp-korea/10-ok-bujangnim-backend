from django.urls import path
from .views import CartItem

urlpatterns = [
   # path('', views.get, name='index')
   path('',CartItem.as_view(),name='index')
]
