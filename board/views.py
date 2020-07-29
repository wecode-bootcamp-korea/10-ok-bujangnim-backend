from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views import View

from board.models import (
    FaceType,
    Product
)
from main.models import (
    Catalog,
    Category
)

class GetBoardByCatalog(View):
    def get(self, request, catalog_id):
        catalog = Catalog.objects.filter(id=catalog_id).values()
        category_list = Category.objects.filter(catalog_id=catalog_id, is_activated='Y').values()
        product_items = Category.objects.filter(is_activated='Y').prefetch_related('product_set', 'product_set__pricebysize_set',
                                                          'product_set__image_set')

        product_items_result = [{
            'category_info': {
                'id': category.id,
                'name': category.name,
                'description': category.description
            },
            'products': [{
                'id': product.id,
                'category_id': product.category_id,
                'name': product.name,
                'image_url': product.image_set.first().image_url,
                'size': [
                    {
                        'id': size.id,
                        'size': size.size,
                        'price': size.price
                    }
                    for size in product.pricebysize_set.all()
                ]
            } for product in category.product_set.all()]
        } for category in product_items]

        return JsonResponse({'result': 'SUCCESS',
                             'data': {'catalog': list(catalog), 'category': list(category_list),
                                      'item': list(product_items_result)}}, status=200)

class GetBoardByCategory(View):
    def get(self, request, catalog_id, category_id):
        catalog = Catalog.objects.filter(id=catalog_id).values()
        category_list = Category.objects.filter(is_activated='Y').values()

        next_category = category_list[category_id] if category_list[category_id] is not None else 'None'

        product_items = Category.objects.filter(id=category_id, is_activated='Y').prefetch_related(
            'product_set',
            'product_set__pricebysize_set',
            'product_set__image_set',
            'product_set__face_products__facetypeproduct_set',
            'product_set__usability_set')

        product_items_result = [{
            'category_info': {
                'id': category.id,
                'name': category.name,
                'description_title': category.description_title,
                'description_content': category.description_content
            },
            'next_category': next_category,
            'products': [{
                'id': product.id,
                'category_id': product.category_id,
                'name': product.name,
                'image_url': product.image_set.first().image_url,
                'usability': product.usability_set.first().usability,
                'size': [
                    {
                        'id': size.id,
                        'size': size.size,
                        'price': size.price
                    }
                    for size in product.pricebysize_set.all()
                ]
                ,
                'skin_types': [
                    {
                        'name': FaceType.objects.get(id=faceType.faceType_id).name
                    }for faceType in product.facetypeproduct_set.all()
                ],
            } for product in category.product_set.all()]
        } for category in product_items]

        return JsonResponse({'result': 'SUCCESS',
                             'data': {'catalog': list(catalog), 'category': list(category_list),
                                      'item': list(product_items_result)}}, status=200)

class GetProductById(View):
    def get(self, request, product_id):
        product_item = Product \
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
            'image_url': product.image_set.first().image_url,
            'name': product.name,
            'description': product.description,
            'skin_types': [
                {
                    'name': FaceType.objects.get(id=faceType.faceType_id).name
                }
                for faceType in product.facetypeproduct_set.all()

            ],
            'usability': product.usability_set.first().usability,
            'main_ingredient': product.ingredient_set.first().main_ingredient,
            'size': [
                {
                    'id': size.id,
                    'size': size.size,
                    'price': size.price
                }
                for size in product.pricebysize_set.all()
            ],
            'ingredient': product.ingredient_set.first().ingredient,
            'sub_image_url': product.image_set.first().sub_image_url,
            'method': product.howtouse_set.first().method,
            'amount': product.howtouse_set.first().amount,
            'texture': product.characteristic_set.first().texture,
            'scent': product.characteristic_set.first().scent,
            'recommendation_desctiption': product.recommendation_set.first().description,
            'recommendation_items': [{
                'id': recommendation_item.product.id,
                'product': recommendation_item.product.name,
                'image_url': recommendation_item.product.image_set.first().image_url
            } for recommendation_item in product.recommendation_set.first().recommendationitems_set.all()]

        } for product in product_item]

        return JsonResponse({'result': 'SUCCESS', 'data': {'item': list(product_result)}}, status=200)