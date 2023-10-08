# Generated by Django 4.2.2 on 2023-10-04 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('profile_image', models.ImageField(default='profile/user-default.png', upload_to='profile/')),
                ('data_create', models.DateTimeField(auto_now_add=True)),
                ('prof', models.CharField(blank=True, max_length=200, null=True)),
                ('prof_info', models.TextField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]