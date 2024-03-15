from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Recipe

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('recipe_list')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipe_list')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        else:
            return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    author_name = recipe.author.username if recipe.author else "Anonymous"
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'author_name': author_name})
