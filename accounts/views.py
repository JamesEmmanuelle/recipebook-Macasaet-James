from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render, redirect
from .models import Recipe

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('recipe_list')
    else:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate (request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipe_list')
            else:
                return render(request, 'login.html', {'error': 'invalid credentials'})
        else:
            return render(request, 'login.html')

def custom_logout(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes: recipes'})

def recipe_detail(request, pk):
    recipes = Recipe.objects.get(pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
    