from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from board.models import PriceBySize, Product
from main.models import Catalog, Category


def get(request, catalog_id):

    catalog = Catalog.objects.filter(id=catalog_id).values()
    category_list = Category.objects.filter(catalog_id=catalog_id).values()
    board_list = Product\
        .objects.prefetch_related('pricebysize_set', 'image_set')

    board_result = [{
        'id': board.id,
        'category_id': board.category_id,
        'name': board.name,
        'image_url': board.image_set.all()[0].image_url,
        'size': [
            {
                'id': size.id,
                'size': size.size,
                'price': size.price
            }
            for size in board.pricebysize_set.all()
        ]
    } for board in board_list]

    return JsonResponse({'result': 'SUCCESS',
                         'data': {'catalog': list(catalog), 'category': list(category_list), 'items': list(board_result)}}, status=200)
