from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from board.models import *




# # def get(request):
#     board_list = Product\
#         .objects.prefetch_related('image_set')\
#         .values('id', 'category_id', 'category__name', 'name', 'image__image_url')\
#         .order_by('id')
#     return JsonResponse({'result': 'SUCCESS', 'data': list(board_list)}, status=200)


def get(request):
    board_list = Product.objects.prefetch_related('image_set','pricebysize_set').values('id', 'category__id','category__name',\
        'name','image__image_url','pricebysize__size','pricebysize__price')\
        .order_by('id')
    pricesize_list =PriceBySize.objects.select_related('Product').values('product_id','size','price').order_by('id')
    #result = board_list.union(pricesize_list,all=True)
    
    

    #return JsonResponse({'result' : 'SUCCESS', 'data' : list(board_list), 'data1' :list(pricesize_list)}, status = 200)
    #return JsonResponse({'result' : 'SUCCESS', 'data' : list(board_list)}, status = 200)
    return JsonResponse({'result' : 'SUCCESS', 'data' : list(board_list)}, status = 200)