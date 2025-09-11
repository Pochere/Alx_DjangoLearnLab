from django.contrib import admin
from .models import UserProfile  # ✅ new addition


# Register your models here.
# Register UserProfile so it shows in admin
admin.site.register(UserProfile)