from django.contrib import admin

from .models import Item,Seller,Buyer,Delivery,Payment
admin.site.register(Item)
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Delivery)
admin.site.register(Payment)