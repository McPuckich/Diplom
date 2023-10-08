from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.recipes, name='recipes'),
    path('recipe/<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('edit-recipe/<int:pk>', views.edit_recipe, name='edit-recipe'),
    path('delete-recipe/<int:pk>', views.delete_recipe, name='delete-recipe'),
]
