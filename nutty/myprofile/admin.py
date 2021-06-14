from django.contrib import admin
from myprofile.models import Profile, Subscriberlist
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name", "email", "tel", "facebook_url", "instagram_url", "github"
    )

    search_fields = (
        "name",
    )


@admin.register(Subscriberlist)
class Subscriberlist(admin.ModelAdmin):
    list_display = (
        "email",
    )
