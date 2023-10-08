from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'Логин'}


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'description', 'prof', 'prof_info', 'profile_image']
        labels = {
            'name': 'Имя',
            'email': 'Email',
            'username': 'Имя пользователя',
            'description': 'Описание',
            'prof': 'Профессия',
            'prof_info': 'Информация о профессии',
            'profile_image': 'Картинка профиля',
        }

        # должен добавить class
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})