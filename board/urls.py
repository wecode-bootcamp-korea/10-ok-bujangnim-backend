from django.urls import path
from board import views

urlpatterns = [
    path('/<int:catalog_id>', views.get, name='index')
]
