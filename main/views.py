from django.http import JsonResponse

# Create your views here.
from board.models import Image
from main.models import Catalog


def get(request):

    main_objects = Image.objects.select_related('product').values('product__name', 'product__description', 'image_url').order_by('?')[:5]
    catalogs = Catalog.objects.prefetch_related(
        'category_set',
        'category_set__product_set',
        'category_set__product_set__image_set',
        'category_set__product_set__pricebysize_set'
    )

    header_result = [{
        'catalog_info': {
            'id': catalog.id,
            'name': catalog.name,
            'category_info': [{
                'id': category.id,
                'name': category.name,
                'product': [{
                    'id': product.id,
                    'category_id': product.category_id,
                    'name': product.name,
                    'image_url': product.image_set.first().image_url,
                    'size': [
                        {
                            'id': size.id,
                            'size': size.size,
                            'price': size.price
                        }for size in product.pricebysize_set.all()]
                }for product in category.product_set.all()]
            }for category in catalog.category_set.all()]
        }
    }for catalog in catalogs]
    return JsonResponse({'result': 'SUCCESS', 'data': {'header': list(header_result), 'body': list(main_objects)}}, status=200)

