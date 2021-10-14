from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
    Object manager for :model:`user.User`
    """

    def create_user(self, email, password, **extra_fields):
        """
        Creates user instance in :model:`user:User`
        """
        if not email:
            raise ValueError(_("The Email must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates superuser instance in :model:`user:User`
        """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
