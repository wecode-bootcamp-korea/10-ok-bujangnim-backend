from django.shortcuts import render, redirect
from board.models import Product
from .models import Cart
from django.core.exceptions import ObjectDoesNotExist
from user.views import login_decorator
from board.views import Product, PriceBySize
from django.views import View
import json
from django.http import JsonResponse
from board.models import PriceBySize
from user.models import User

# Create your views here.
#장바구니에 상품담
class CartItem(View):
    @login_decorator
    def post(self,request):
        #프론트에서 값들을 준다.
        data = json.loads(request.body)
        print(data)
         
        #product_infomation = Product.objects.all()
        #try:
        #product = Product.objects.get(id = data['product_id'])
        user_id = request.user.id

        product_id = Product.objects.get(id =data['cart_id']).id
        print(product_id)
        if(Cart.objects.filter(product_id = product_id,user_id = user_id )).exists():
            a = Cart.objects.get(product_id=product_id,user_id = user_id)
            print(a)
            print(a.quantity)
            print(a.id)
            if(data['isPlus'] == "True"):
               a.quantity += 1
               a.save()
            else:
               a.quantity = data['quantity']
               a.save()
            return JsonResponse({'message' :'추가함'}, status =200)
        else:
            Cart(
                pricebysize_id = data['pricebysize_id'],    
                user_id = user_id,
                product_id = product_id,
                quantity =1
            ).save()
        
        cart_list = Cart.objects.select_related('product','pricebysize').all()
        
        cart_result = [{
            'id': cart.id,
            'product_id': cart.product.id,
            'product': cart.product.name,
            'pricebysize_id': cart.pricebysize_id,
            'size': cart.pricebysize.size,
            'price': cart.pricebysize.price,
            'quantity': cart.quantity
        } for cart in cart_list ]
        return JsonResponse({'message' : 'success', 'data' : list(cart_result)}, status = 200)
    
    
    @login_decorator
    def get(self,request):
        cart_list = Cart.objects.select_related('product','pricebysize').all()
       
        
        a = 0
        for i in range(len(cart_list)):
            b = cart_list[i].pricebysize.price.replace("₩ ", "")
            c = int(b.replace(",",""))
            
            a = a + c
        cart_result1 = [{
            'product' : cart.product.name,
            'size' : cart.pricebysize.size,
            'quantity' : cart.quantity,
            'price' : cart.pricebysize.price,
            #'cart_id' : cart.id,
        } for cart in cart_list ]
        return JsonResponse({'message' : 'success' , 'data' : list(cart_result1),'total' : a},status=200)
        



