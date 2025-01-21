from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(CustomUser)
admin.site.register(CommonOrderDetails)
admin.site.register(Shirt)
admin.site.register(Pant)
admin.site.register(WomensOrderDetails)
