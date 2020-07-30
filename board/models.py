from django.db import models

# Create your models here.
from main.models import Category


class Product(models.Model):
    category      = models.ForeignKey(Category,on_delete       = models.SET_NULL, null=True)
    name          = models.CharField(max_length                = 255)
    description   = models.CharField(max_length                = 255)
    face_products = models.ManyToManyField('FaceType', through = 'FaceTypeProduct')
    is_activated  = models.CharField(max_length                = 10, default        = 'Y', null = False, blank = True)
    created_at    = models.DateTimeField(auto_now_add          = True)
    updated_at    = models.DateTimeField()

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class PriceBySize(models.Model):
    product      = models.ForeignKey(Product, on_delete =models.SET_NULL, null=True)
    price        = models.CharField(max_length          = 255)
    size         = models.CharField(max_length          = 255)
    is_activated = models.CharField(max_length          = 10, default     = 'Y', null = False, blank = True)
    created_at   = models.DateTimeField(auto_now_add    = True)
    updated_at   = models.DateTimeField()

    class Meta:
        db_table = 'price_by_size'

    def __str__(self):
        return self.product.name

class Image(models.Model):
    product       = models.ForeignKey(Product, on_delete =models.SET_NULL, null=True)
    image_url     = models.URLField(max_length           = 1500)
    sub_image_url = models.URLField(max_length           = 1500, default   = '')
    is_activated  = models.CharField(max_length          = 10, default     = 'Y', null = False, blank = True)
    created_at    = models.DateTimeField(auto_now_add    = True)
    updated_at    = models.DateTimeField()

    class Meta:
        db_table = 'images'

    def __str__(self):
        return self.product.name

class FaceType(models.Model):
    name         = models.CharField(max_length       = 255)
    is_activated = models.CharField(max_length       = 10, default = 'Y', null = False, blank = True)
    created_at   = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField()

    class Meta:
        db_table = 'face_types'

    def __str__(self):
        return self.name

class FaceTypeProduct(models.Model):
    faceType     = models.ForeignKey(FaceType, on_delete = models.CASCADE)
    product      = models.ForeignKey(Product, on_delete  = models.CASCADE)
    is_activated = models.CharField(max_length           = 10, default     = 'Y', null = False, blank = True)
    created_at   = models.DateTimeField(auto_now_add     = True, null      = True)
    updated_at   = models.DateTimeField(null             = True)
    class Meta:
        db_table = 'face_type_product'

    def __str__(self):
        return self.product.name

class HowToUse(models.Model):
    product      = models.ForeignKey(Product,on_delete = models.CASCADE)
    method       = models.CharField(max_length         = 255)
    amount       = models.CharField(max_length         = 255)
    is_activated = models.CharField(max_length         = 10, default     = 'Y', null = False, blank = True)
    created_at   = models.DateTimeField(auto_now_add   = True)
    updated_at   = models.DateTimeField()

    class Meta:
        db_table = 'how_to_use'

    def __str__(self):
        return self.product.name

class Characteristic(models.Model):
    product      = models.ForeignKey(Product,on_delete = models.SET_NULL, null=True)
    texture      = models.CharField(max_length         = 255)
    scent        = models.CharField(max_length         = 255)
    is_activated = models.CharField(max_length         = 10, default     = 'Y', null = False, blank = True)
    created_at   = models.DateTimeField(auto_now_add   = True)
    updated_at   = models.DateTimeField()

    class Meta:
        db_table = 'characteristics'

    def __str__(self):
        return self.product.name


class Ingredient(models.Model):
    product         = models.ForeignKey(Product,on_delete = models.SET_NULL, null=True)
    main_ingredient = models.CharField(max_length         = 255)
    ingredient      = models.TextField(max_length         = 1000)
    is_activated    = models.CharField(max_length         = 10, default     = 'Y', null = False, blank = True)
    created_at      = models.DateTimeField(auto_now_add   = True)
    updated_at      = models.DateTimeField()

    class Meta:
        db_table = 'ingredients'

    def __str__(self):
        return self.product.name

class Usability(models.Model):
    product      = models.ForeignKey(Product,on_delete = models.SET_NULL, null=True)
    usability    = models.CharField(max_length         = 255)
    is_activated = models.CharField(max_length         = 10, default     = 'Y', null = False, blank = True)
    created_at   = models.DateTimeField(auto_now_add   = True)
    updated_at   = models.DateTimeField()

    class Meta:
        db_table = 'usability'

    def __str__(self):
        return self.product.name

class Recommendation(models.Model):
    product      = models.ForeignKey(Product,on_delete = models.SET_NULL, null=True)
    description  = models.CharField(max_length         = 255)
    is_activated = models.CharField(max_length         = 10, default     = 'Y', null = False, blank = True)
    created_at   = models.DateTimeField(auto_now_add   = True)
    updated_at   = models.DateTimeField()

    class Meta:
        db_table = 'recommendation'

    def __str__(self):
        return self.product.name

class RecommendationList(models.Model):
    recommendation = models.ForeignKey(Recommendation,on_delete = models.SET_NULL, null=True)
    product        = models.ForeignKey(Product,on_delete        = models.SET_NULL, null=True)
    is_activated   = models.CharField(max_length                = 10, default     = 'Y', null = False, blank = True)
    created_at     = models.DateTimeField(auto_now_add          = True)
    updated_at     = models.DateTimeField()

    class Meta:
        db_table = 'recommendation_list'

    def __str__(self):
        return self.product.name

class Subtitle(models.Model):
    name         = models.CharField(max_length = 50)
    subscription = models.CharField(max_length = 200)
    number       = models.CharField(max_length = 30)

    class Meta:
        db_table = 'subtitles'

    def __str__(self):
        return self.product.name
