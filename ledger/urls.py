from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe-list'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe-detail'),
]

app_name = 'recipes'
