from django.contrib import admin

from saturn.admin import site as saturn_admin
from .models import Product

# Register to Django Admin
admin.site.register([Product])

# Register to Saturn Admin
saturn_admin.register([Product])
