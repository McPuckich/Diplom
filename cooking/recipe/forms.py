from django.forms import ModelForm
from django.forms import inlineformset_factory
from .models import Recipe, Comment
from django import forms


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'tags', 'main_image']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'ingredients': 'Ингредиенты',
            'steps': 'Шаги',
            'tags': 'Тэги',
            'main_image': 'Основное изображение',
        }
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['value', 'mark', 'comment']

        labels = {
            'value': 'Оставте ваше мнение',
            'mark': 'Оставте вашу оценку',
            'comment': 'Оставте ваш комментарий',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
