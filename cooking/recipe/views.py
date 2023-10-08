from django.shortcuts import render, redirect
from .models import Recipe, Tags
from django.contrib import messages
from .forms import RecipeForm, CommentForm
from django.contrib.auth.decorators import login_required
from .utils import search_rec, paginator
from django.db.models import Q


def home(request):
    rec = search_rec(request)
    context = {
        'recipies': rec,
    }
    return render(request, 'recipe/home.html', context)


def recipes(request):
    rec, search_query = search_rec(request)
    custom_range, rec = paginator(request, rec, 2)

    context = {
        'recipes': rec,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'recipe/recipes.html', context)


def recipe_detail(request, pk):
    recipe_d = Recipe.objects.get(id=pk)
    comment = CommentForm()

    if request.method == 'POST':
        comment = CommentForm(request.POST)
        com = comment.save(commit=False)
        com.recipe = recipe_d
        com.owner = request.user.profile
        com.save()

        recipe_d.get_vote_count()
        recipe_d.get_mark_count(pk)

        return redirect('recipe_detail', pk=recipe_d.id)

    context = {
        'recipe_d': recipe_d,
        'comment': comment,
    }
    return render(request, 'recipe/recipe_detail.html', context)


@login_required(login_url='login_user')
def add_recipe(request):
    act = 'add'
    profile = request.user.profile
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            form.save_m2m()
            messages.success(request, 'Вы успешно добавили рецепт')
            return redirect('recipes')

    context = {
        'form': form,
        'act': act,
    }

    return render(request, 'recipe/addrecipe.html', context)


@login_required(login_url='login_user')
def edit_recipe(request, pk):
    act = 'edit'
    profile = request.user.profile
    recipe = profile.recipe_set.get(id=pk)
    form = RecipeForm(instance=recipe)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно изменили рецепт')
            return redirect('profile')

    context = {
        'form': form,
        'recipe': recipe,
        'act': act,
    }
    return render(request, 'recipe/addrecipe.html', context)


@login_required(login_url='login_user')
def delete_recipe(request, pk):
    profile = request.user.profile
    recipe = profile.recipe_set.get(id=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('profile')

    context = {
        'object': recipe,
    }
    return render(request, 'recipe/delete-recipe.html', context)
