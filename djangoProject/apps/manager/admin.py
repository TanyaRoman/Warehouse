from django.contrib import admin

from .models import Manager

#  Даем права на изменения Goods админу
admin.site.register(Manager)