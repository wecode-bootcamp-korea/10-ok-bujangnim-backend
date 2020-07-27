import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,HttpResponse
from board.models import Product,PriceBySize,Image
from .models import Subtitle


# Create your views here.


# def get(request):
#     #sub_objects = sub.objects.select_related('product').values('product__name', 'product__description', 'image_url').order_by('-product__name')[:6]
#     return 'ok'
# sub_objects = Subtitle.objects.select_related('product').values('name','subscription','number','cate_id').order_by('cate_id')
def get(request):
    sub_objects = Subtitle.objects.select_related('product').values('name','subscription','number','cate_id').order_by('cate_id')
    image_objects = Image.objects.select_related('product').values('image_url','product__name','id').order_by('id')
    price_objects = PriceBySize.objects.select_related('product').values('price', 'size', 'product__id').order_by('id')
    #result  = sub_objects.objects.get()
    print(type(sub_objects))
    #result.append(list((sub_objects)[0:1]))
    #result.append(list((image_objects)[0:8]))
    #result.append(list((price_objects)[0:10]))
    
    
    #sub = list(sub_objects)
    #image = list(image_objects)
    #price = list(price_objects)
    #print(type(sub), len(sub))
    #print(type(image), len(image))
    #result.append(list(sub[0]) + list(image[0]) + list(price[0]))

    

   # for i in range(0):
    #    result[i] = list(sub_objects[i]) + list(image_objects[i]) + list(price_objects[i])
    #product_price = Image.objects.select_related('price_by_size').values('image_url','product').order_by('id')
    

    #return JsonResponse({'result': 'SUCCESS', 'data': list(result)}, status=200)
    #return JsonResponse({'result': 'SUCCESS',
                    # 'data': {'catalog': list(catalog), 'category': list(category_list), 
                     # 'data': {'info': {'category': '클렌저', 'description': '크렌저 설명'}, 'items': list(board_result)}}}, status=200)
    #return JsonResponse({'result': 'SUCCESS' , 
    #'data' : {'sub_objects' :list(sub_objects)[0:1],'data' : {'image_objects' : list(image_objects)[0:11]},
    #'data' : {'price_objects':list(price_objects)[0:11]}}},status =200)

    # return JsonResponse({'result' : 'SUCCESS','data':{'left' : list(sub_objects),'image': list(image_objects),
    # }, 'price' : list(price_objects)}, status = 200)
    #return JsonResponse({'result' :'SUCCESS' , 'data' : list(sub_objects)}, status = 200)
    #return JsonResponse({'result' :'SUCCESS' , 'data' : list(image_objects)}, status = 200)
    return JsonResponse({'result' :'SUCCESS' , 'data' : list(price_objects)}, status = 200)
    
