from django.db import models


class Continent(models.Model):
    """
    Stores a single continent entry.
    """

    class Meta:
        verbose_name = "Continent"
        verbose_name_plural = "Continents"
        indexes = [
            models.Index(fields=["name"], name="name_index"),
        ]
        ordering = ("name",)

    name = models.CharField(max_length=50, null=True, unique=True)
    population = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        """
        Returns the name of continent if instance is converted to str.
        """
        return self.name


class Country(models.Model):
    """
    Stores a single country entry, related to :model:`covid.Continent`.
    """

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        indexes = [
            models.Index(fields=["geoid"], name="geoid_index"),
        ]
        ordering = ("name",)

    name = models.CharField(max_length=50)
    geoid = models.CharField(max_length=50, unique=True)
    country_code = models.CharField(max_length=50, null=True)
    population = models.BigIntegerField(null=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, db_index=True)

    def __str__(self) -> str:
        """
        Returns the name of country if instance is converted to str.
        """
        return self.name


class DailyReport(models.Model):
    """
    Stores a single daily report entry, related to :model:`covid.Country`.
    """

    class Meta:
        verbose_name = "Daily Report"
        verbose_name_plural = "Daily Reports"
        unique_together = ("country", "date")

    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_index=True)
    date = models.DateField()
    cases = models.IntegerField()
    deaths = models.IntegerField()
    cases_per_100000 = models.FloatField(null=True)

    def __str__(self) -> str:
        """
        Returns report date and its country's name if instance is converted to str.
        """
        return f"{self.date} - {self.country.name}"
