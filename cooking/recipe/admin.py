from django.contrib import admin
from .models import Recipe, Tags, Comment
from django.utils.safestring import mark_safe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'get_img')

    def get_img(self, image):
        if image.main_image:
            return mark_safe(f"<img src='{image.main_image.url}' width='50'>")


class CommentAdmin(admin.ModelAdmin):
    list_display = ('value', 'mark', 'owner', 'recipe', 'owner_img')

    def owner_img(self, image):
        if image.owner.profile_image:
            return mark_safe(f"<img src='{image.owner.profile_image.url}' width='50'>")


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tags)
admin.site.register(Comment, CommentAdmin)
