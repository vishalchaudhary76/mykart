from .models import Product,Contact,Orders,OrderUpdate

from django.contrib import admin

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)