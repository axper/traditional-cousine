from django.contrib import admin

# Register your models here.
from core import models

admin.site.register(models.Ingredient)
admin.site.register(models.Location)
admin.site.register(models.Recipe)
