from django.urls import path
from board.views import GetBoardByCatalog, GetBoardByCategory, GetProductById

urlpatterns = [
    path('<int:catalog_id>', GetBoardByCatalog.as_view()),
    path('<int:catalog_id>/<int:category_id>', GetBoardByCategory.as_view()),
    path('read/<int:product_id>', GetProductById.as_view())
]
