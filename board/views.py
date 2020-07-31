from django.http import JsonResponse
# Create your views here.
from django.views import View
from board.models import (
    FaceType,
    Product
)
from main.models import (
    Catalog, Category
)

class GetBoardByCatalog(View):
    def get(self, request, catalog_id):
        product_data = Catalog.objects.prefetch_related(
            'category_set',
            'category_set__product_set',
            'category_set__product_set__pricebysize_set',
            'category_set__product_set__image_set').filter(id=catalog_id, is_activated=True)

        data = {
            'catalog': list(product_data.values()),
            'category': list(product_data.first().category_set.filter(is_activated=True).values()),
            'item': [{
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
            }for category in product_data[0].category_set.filter(is_activated=True).all()]
        }
        return JsonResponse({'result': 'SUCCESS',
                             'data': data}, status=200)

class GetBoardByCategory(View):
    def get(self, request, catalog_id, category_id):
        product_data = Catalog.objects.prefetch_related(
            'category_set',
            'category_set__product_set',
            'category_set__product_set__pricebysize_set',
            'category_set__product_set__image_set').filter(id=catalog_id, is_activated=True)

        data = {
            'catalog': list(product_data.values()),
            'category': list(product_data.first().category_set.values()),
            'items': [{
                'category_info': {
                    'id': category.id,
                    'name': category.name,
                    'description_title': category.description_title,
                    'description_content': category.description_content
                },
                'next_category': {
                    'id': product_data.first().category_set.values()[category_id]['id'],
                    'catalog_id': product_data.first().category_set.values()[category_id]['catalog_id'],
                    'name': product_data.first().category_set.values()[category_id]['name'],
                    'description_title': product_data.first().category_set.values()[category_id]['description_title'],
                    'description': product_data.first().category_set.values()[category_id]['description'],
                    'description_content': product_data.first().category_set.values()[category_id]['description_content'],
                    'is_activated': product_data.first().category_set.values()[category_id]['is_activated'],
                    'image_url': category.product_set.filter(category_id=category_id)
                        .first().image_set.first().image_url

                },
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
                            'name': FaceType.objects.get(id=face_type.face_type_id).name
                        } for face_type in product.facetypeproduct_set.all()
                    ],
                } for product in category.product_set.all()]
            }for category in product_data.first().category_set.filter(id=category_id).all()]
        }
        return JsonResponse({'result': 'SUCCESS',
                             'data': data}, status=200)

class GetProductById(View):
    def get(self, request, product_id):
        product_item = Product \
            .objects.prefetch_related(
            'pricebysize_set',
            'image_set',
            'facetypeproduct_set__face_type',
            'usability_set',
            'ingredient_set',
            'howtouse_set', 'characteristic_set', 'recommendation_set__recommendationitems_set').filter(id=product_id).first()

        product_result = {
            'id': product_item.id,
            'category_id': product_item.category_id,
            'category_name': Category.objects.filter(id=product_item.category_id).first().name,
            'image_url': product_item.image_set.first().image_url,
            'name': product_item.name,
            'description': product_item.description,
            'skin_types': [
                {
                    'name': FaceType.objects.get(id=face_type.face_type.id).name
                }
                for face_type in product_item.facetypeproduct_set.all()

            ],
            'usability': product_item.usability_set.first().usability,
            'main_ingredient': product_item.ingredient_set.first().main_ingredient,
            'size': [
                {
                    'id': size.id,
                    'size': size.size,
                    'price': size.price
                }
                for size in product_item.pricebysize_set.all()
            ],
            'ingredient': product_item.ingredient_set.first().ingredient,
            'sub_image_url': product_item.image_set.first().sub_image_url,
            'method': product_item.howtouse_set.first().method,
            'amount': product_item.howtouse_set.first().amount,
            'texture': product_item.characteristic_set.first().texture,
            'scent': product_item.characteristic_set.first().scent,
            'recommendation_description': product_item.recommendation_set.first().description,
            'recommendation_items': [{
                'id': recommendation_item.product.id,
                'product': recommendation_item.product.name,
                'image_url': recommendation_item.product.image_set.first().image_url
            } for recommendation_item in product_item.recommendation_set.first().recommendationitems_set.all()]

        }

        return JsonResponse({'result': 'SUCCESS', 'data': [product_result]}, status=200)