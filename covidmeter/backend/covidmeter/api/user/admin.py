from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreationForm, UserUpdateForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    """
    Lists, creates and update instances from :model:`user.User`
    """

    form = UserUpdateForm
    add_form = UserCreationForm

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
    )
    list_filter = (
        "is_active",
        "is_superuser",
        "is_staff",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "date_of_birth",
                    "profile_picture",
                    "country",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                    "is_staff",
                )
            },
        ),
        ("Timestamps", {"fields": ("date_joined",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
