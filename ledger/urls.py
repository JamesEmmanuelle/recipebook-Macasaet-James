from django.urls import path
from .views import RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]