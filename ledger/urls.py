from django.urls import path
from .views import recipe_list, recipe_detail, recipe1, recipe2

app_name = 'recipes'

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe-list'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe-detail'),
    path('recipe/1/', recipe1, name='recipe1'),
    path('recipe/2/', recipe2, name='recipe2'),
]
