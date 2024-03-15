from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView
from django.views.generic import DetailView


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"

# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     ctx = {"recipes": recipes}
#     return render(request, 'recipe_list.html', ctx)

# def recipe_detail(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     ctx = {"recipe": recipe}
#     return render(request, 'recipe_detail.html', ctx)

# def recipe1(request):
#     recipe = Recipe.objects.get(pk=1)  
#     ctx = {"recipe": recipe}
#     return render(request, 'recipe_detail.html', ctx)

# def recipe2(request):
#     recipe = Recipe.objects.get(pk=2)  
#     ctx = {"recipe": recipe}
#     return render(request, 'recipe_detail.html', ctx)
