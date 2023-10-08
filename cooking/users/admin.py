from django.contrib import admin
from .models import Profile
from django.utils.safestring import mark_safe


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'username', 'profile_img')

    def profile_img(self, image):
        if image.profile_image:
            return mark_safe(f"<img src='{image.profile_image.url}' width='50'>")


admin.site.register(Profile, ProfileAdmin)
