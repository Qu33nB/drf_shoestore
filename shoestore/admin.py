from django.contrib import admin

from shoestore.models import Manufacturer, ShoeColor, ShoeType, Shoe

admin.site.register(Manufacturer)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)
admin.site.register(Shoe)
