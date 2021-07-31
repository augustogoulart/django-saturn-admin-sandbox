from django.contrib import admin

# from saturn.admin import site as saturn_admin
from .models import BuyerProfile

# Register to Django Admin
admin.site.register([BuyerProfile])

# Register to Saturn Admin
# saturn_admin.register([BuyerProfile])
