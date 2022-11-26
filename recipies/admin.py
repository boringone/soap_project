from django.contrib import admin
from .models import Ingredient, Recipe, Tag

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Tag)