from django.db import models
from board.models import Product,PriceBySize
from user.models import User

# Create your models here.


class Cart(models.Model):
    user         = models.ForeignKey(User,on_delete    = models.SET_NULL, null=True)
    product      = models.ForeignKey(Product,on_delete = models.SET_NULL, null=True)
    is_activated = models.CharField(max_length         = 10, default     = 'Y', null = False, blank = True)
    created_at   = models.DateTimeField(auto_now_add   = True)
    updated_at   = models.DateTimeField(auto_now_add   = True)
    pricebysize = models.ForeignKey(PriceBySize, on_delete = models.SET_NULL, null=True)
    quantity = models.PositiveSmallIntegerField(null=True, default = 0)
   
    class Meta:
        db_table = 'carts'

    def __str__(self):
        return self.product.name
class Order_Status(models.Model):
    status_name = models.CharField(max_length = 10)

    class Meta:
        db_table = 'orderstatus'
    def __str__(self):
        return self.product.name


class User_Order(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete = models.SET_NULL, null=True)
    order_status_id = models.ForeignKey(Order_Status, on_delete = models.SET_NULL, null=True)
    active = models.BooleanField(default = True)
    is_activate = models.CharField(max_length             = 10, default     = 'Y', null = False, blank = True)
    created_at  = models.DateTimeField(auto_now_add       = True)
    updated_at  = models.DateTimeField(auto_now_add       = True)
    User_Product = models.ManyToManyField(Product, through='Order_Product')
    
    class Meta:
        db_table = 'userorders'


    def __str__(self):
        return self.product
class Order_Product(models.Model):
    user_order_id = models.ForeignKey(User_Order,on_delete = models.SET_NULL, null=True)
    product_id = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)


