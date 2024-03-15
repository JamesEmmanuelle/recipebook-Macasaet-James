from django.urls import path
from . import views

urlpatterns = [
    path('/login/', views.custom_login, name='login'),
    path('/logout/', views.custom_logout, name='logout'),
    path('/recipe/<int:pk>/', views.recipe_detail, name='recipe-detail'),
]
