from django.contrib import admin
from .models import Drum, Maintenance, Accessory

# Register your models here.
admin.site.register(Drum)
admin.site.register(Maintenance)
admin.site.register(Accessory)