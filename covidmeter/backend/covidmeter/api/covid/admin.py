from django.contrib import admin

from .models import Continent, Country, DailyReport


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    """
    Lists, creates and update instances from :model:`covid.Continents`
    """

    list_display = (
        "name",
        "population",
    )
    search_fields = ("name",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
    Lists, creates and update instances from :model:`covid.Country`
    """

    list_display = (
        "name",
        "geoid",
        "country_code",
        "population",
        "continent",
    )
    list_filter = ("continent",)


@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    """
    Lists, creates and update instances from :model:`covid.DailyReport`
    """

    list_display = (
        "date",
        "country",
        "cases",
        "deaths",
    )
    list_filter = ("country",)
