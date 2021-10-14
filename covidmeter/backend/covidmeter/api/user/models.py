from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from api.covid.models import Country


def profile_image_path(instance, filename, **kwargs) -> str:
    """
    Returns the file name for user profile picture
    """
    return f"profile/{timezone.now()}.{filename.split('.')[-1]}"


class User(AbstractBaseUser, PermissionsMixin):
    """
    Stores a single user entry.
    """

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(
        _("first name"), max_length=150, blank=True, null=True
    )
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True)
    profile_picture = models.ImageField(
        _("profile picture"), upload_to=profile_image_path, blank=True, null=True
    )
    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True
    )
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active status"), default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
