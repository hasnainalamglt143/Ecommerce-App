from django.contrib import admin
from . import models

# Register your models here.
# Change admin site titles
admin.site.site_header = "Ecommerce Center Admin"          # Top-left header
admin.site.site_title = "commerce Center Admin Admin Portal"    # Browser tab title
admin.site.index_title = "Welcome to commerce Center Dashboard"  



admin.site.register(models.Category)  # Register your models here.
admin.site.register(models.Customer)  # Register your models here.
admin.site.register(models.Product)  # Register your models here.
admin.site.register(models.Order)  # Register your models here.