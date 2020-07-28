from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from board.models import Product, FaceType


def get(request, product_id):
    product_item = Product\
        .objects.prefetch_related(
        'pricebysize_set',
        'image_set',
        'facetypeproduct_set__faceType',
        'usability_set',
        'ingredient_set',
        'howtouse_set', 'characteristic_set', 'recommendation_set__recommendationitems_set').filter(id=product_id)


    product_result = [{
        'id': product.id,
        'category_id': product.category_id,
        'image_url': product.image_set.all()[0].image_url,
        'name': product.name,
        'description': product.description,
        'skin_types': [
            {
                'name': FaceType.objects.get(id=faceType.faceType_id).name
            }
            for faceType in product.facetypeproduct_set.all()

        ],
        'usability': product.usability_set.all()[0].usability,
        'main_ingredient': product.ingredient_set.all()[0].main_ingredient,
        'size': [
            {
                'id': size.id,
                'size': size.size,
                'price': size.price
            }
            for size in product.pricebysize_set.all()
        ],
        'ingredient': product.ingredient_set.all()[0].ingredient,
        'sub_image_url': product.image_set.all()[0].sub_image_url,
        'method': product.howtouse_set.all()[0].method,
        'amount': product.howtouse_set.all()[0].amount,
        'texture': product.characteristic_set.all()[0].texture,
        'scent': product.characteristic_set.all()[0].scent,
        'recommendation_desctiption': product.recommendation_set.all()[0].description,
        'recommendation_items': [{
            'id': recommendation_item.product.id,
            'product': recommendation_item.product.name,
        } for recommendation_item in product.recommendation_set.all()[0].recommendationitems_set.all()]

    } for product in product_item]

    return JsonResponse({'result': 'SUCCESS', 'data': {'item': list(product_result)}}, status=200)