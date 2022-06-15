from django.contrib import admin
from .models.product import Product
from .models.catagory import Catagory
from .models.customer import Customer



class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'catagory']


class AdminCatagory(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Product,AdminProduct)
admin.site.register(Catagory,AdminCatagory)
# Register your models here.
admin.site.register(Customer)