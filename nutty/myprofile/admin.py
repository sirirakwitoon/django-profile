from django.contrib import admin
from myprofile.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =(
        "name","email",
    )

    search_fields =(
        "name",
    )