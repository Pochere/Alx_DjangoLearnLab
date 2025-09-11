from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Customize the admin interface for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

# Register the custom user model with its admin
admin.site.register(CustomUser, CustomUserAdmin)
