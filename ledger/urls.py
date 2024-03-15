from django.urls import path
from .views import RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]




# urlpatterns = [
#     path('recipes/list/', recipe_list, name='recipe-list'),
#     path('recipes/<int:pk>/', recipe_detail, name='recipe-detail'),
#     path('recipe/1/', recipe1, name='recipe1'),
#     path('recipe/2/', recipe2, name='recipe2'),
# ]
