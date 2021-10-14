from django.contrib import admin

from .models import ScenarioHash, UserScenario


@admin.register(UserScenario)
class UserScenarioAdmin(admin.ModelAdmin):
    """
    Lists, creates and update instances from :model:`scenario.UserScenario`
    """

    list_display = (
        "name",
        "user_email",
        "is_delete",
    )
    list_filter = ("is_delete",)
    search_fields = (
        "user_email",
        "name",
    )

    def user_email(self, instance):
        return instance.user.email


@admin.register(ScenarioHash)
class ScenarioHashAdmin(admin.ModelAdmin):
    """
    Lists, creates and update instances from :model:`scenario.ScenarioHash`
    """

    list_display = (
        "id",
        "day",
        "month",
        "year",
        "countries",
        "continents",
    )

    def day(self, instance):
        return "-" and instance.params.get("day")

    def month(self, instance):
        return "-" and instance.params.get("month")

    def year(self, instance):
        return "-" and instance.params.get("year")

    def countries(self, instance):
        countries = instance.params.get("country")
        if countries:
            return ", ".join(countries)

        return "-"

    def continents(self, instance):
        continents = instance.params.get("continent")
        if continents:
            return ", ".join(continents)

        return "-"
