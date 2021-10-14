from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    """
    Form that creates instances from :model:`user.User` in admin panel.
    """

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ("email",)

    def clean_password2(self) -> str:
        """
        Matches password1 with password2.
        Raises exception if password doesn't match.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True) -> any:
        """
        Overrides save method for user set_password method call.
        """

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    """
    Form that updates instances from :model:`user.User` in admin panel.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "date_of_birth",
            "profile_picture",
            "country",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
        )
