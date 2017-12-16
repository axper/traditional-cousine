from django.contrib import admin

# Register your models here.
from core import models


class StepAdmin(admin.StackedInline):
    model = models.Step


class RecipeAdmin(admin.ModelAdmin):
    inlines = [StepAdmin]


admin.site.register(models.Ingredient)
admin.site.register(models.Location)
admin.site.register(models.Recipe, RecipeAdmin)
