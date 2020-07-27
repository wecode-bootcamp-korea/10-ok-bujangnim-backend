from django.db import models
from main.models import Category
# Create your models here.


class Subtitle(models.Model):
    name = models.CharField(max_length = 200)
    subscription = models.CharField(max_length = 500)
    number = models.CharField(max_length =100)
    cate = models.OneToOneField(Category, on_delete = models.CASCADE,primary_key=True)
    is_activated = models.CharField(max_length = 10, default='Y', null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(null=True)
    # is_activated = models.CharField(max_length = 10, default='Y', null=False, blank=True)
    
    # updated_at = models.DateTimeField(default='now')
    
    

    class Meta:
        db_table = 'subtitles'

    def __str__(self):
        return self.name
