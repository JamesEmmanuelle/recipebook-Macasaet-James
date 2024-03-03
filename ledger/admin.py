from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

class RecipeIngredientInline(admin.TabularInline):  
    model = RecipeIngredient
    extra = 1  

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    inlines = [RecipeIngredientInline]
