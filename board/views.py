# Create your views here.
from board.models import Product, PriceBySize






def get(request):
    board_list = Product.objects.prefetch_related('image_set','pricebysize_set').values('id', 'category__id','category__name',\
        'name','image__image_url','pricebysize__size','pricebysize__price')\
        .order_by('id')
    pricesize_list =PriceBySize.objects.select_related('Product').values('product_id','size','price').order_by('id')


    return JsonResponse({ 'data' : list(board_list)}, status = 200)
