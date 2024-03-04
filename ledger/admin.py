from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):  
    model = RecipeIngredient
    extra = 1  

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    inlines = [RecipeIngredientInline]

# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at', 'updated_at')
#     search_fields = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)



