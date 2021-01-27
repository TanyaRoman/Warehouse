from django.contrib import admin

from .models import Goods

#  Даем права на изменения Goods админу
admin.site.register(Goods)
