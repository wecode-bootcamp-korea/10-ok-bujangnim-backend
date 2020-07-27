from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
#Create your views here.
from board.models import Product, Image


def get(request):
    main_objects = Image.objects.select_related('product').values('product__name', 'product__description', 'image_url').order_by('-product__name')[:6]
    print(main_objects.query)
    # print(serializers.serialize('json', main_objects))

    return JsonResponse({'result': 'SUCCESS', 'data': list(main_objects)}, status=200)

