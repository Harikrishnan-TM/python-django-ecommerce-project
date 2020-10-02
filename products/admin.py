from django.contrib import admin
from .models import product,Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')


# Register your models here.
admin.site.register(product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)

