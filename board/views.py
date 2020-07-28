from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views import View

from board.models import FaceType
from main.models import Catalog, Category


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
                'image_url': product.image_set.all()[0].image_url,
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
            'products': [{
                'id': product.id,
                'category_id': product.category_id,
                'name': product.name,
                'image_url': product.image_set.all()[0].image_url,
                'usability': product.usability_set.all()[0].usability,
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
                                      'products': list(product_items_result)}}, status=200)