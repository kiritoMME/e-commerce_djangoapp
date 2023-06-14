from django.contrib import admin
from .models import product, testimonial, order, confirmed_orders

# Register your models here.
admin.site.register(product)
admin.site.register(testimonial)
admin.site.register(order)
admin.site.register(confirmed_orders)