from django.urls import path
from board import views
from board.views import GetBoardByCatalog, GetBoardByCategory

urlpatterns = [
    path('<int:catalog_id>', GetBoardByCatalog.as_view()),
    path('<int:catalog_id>/<int:category_id>', GetBoardByCategory.as_view())
]
