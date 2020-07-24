from django.urls import path
from read import views

urlpatterns = [
    path('/<int:product_id>', views.get, name='index')
]
