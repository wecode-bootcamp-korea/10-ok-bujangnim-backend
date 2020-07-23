from django.db import models

# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length = 255)
    is_activated = models.CharField(max_length = 10, default='Y', null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'catalogs'

    def __str__(self):
        return self.name

class Category(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    is_activated = models.CharField(max_length = 10, default='Y', null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

