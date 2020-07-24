from django.db import models

# Create your models here.
from board.models import Product


class User(models.Model):
    email = models.CharField(max_length = 255)
    first_name =  models.CharField(max_length = 255, null=True)
    last_name =  models.CharField(max_length = 255, null=True)
    password = models.CharField(max_length = 255)
    is_activated = models.CharField(max_length = 10, default='Y', null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    is_activated = models.CharField(max_length = 10, default='Y', null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'carts'

    def __str__(self):
        return self.product.name
