from django.db import models
from .catagory import Catagory

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uplodedimages/')

    @staticmethod
    def get_all():
        return Product.objects.all()

    @staticmethod
    def get_all_by_categoryid(catagory_id):
        if catagory_id:

            return Product.objects.filter(catagory = catagory_id)
        else:
            return Product.get_all()
