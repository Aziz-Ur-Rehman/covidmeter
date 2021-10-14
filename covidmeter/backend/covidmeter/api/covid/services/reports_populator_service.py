from django.db.utils import IntegrityError

from api.covid.models import Continent, Country, DailyReport
from .report_cleaner_service import ReportCleanerService


class ReportsPopulatorService:
    """
    ReportsPopulatorService class

    Attributes
    ----------
    COUNTRY_DETAIL_TAGS: list[str]
    """

    def __init__(self, reports: list[dict]) -> None:
        self.reports = ReportCleanerService().clean_reports(reports)

    def populate_country(self, country_details: dict) -> Country:
        """
        Populate country dict into model

        @param country_detals: A dict with country data
        @return: Country model instance
        @raise: This function doesn't raise any exception.
        """
        continent_details = {"name": country_details.pop("continent")}
        continent_instance, created = Continent.objects.get_or_create(
            **continent_details
        )

        country_details["continent"] = continent_instance
        instance, created = Country.objects.get_or_create(**country_details)
        instance.continent = continent_instance
        instance.save()

        return instance

    def populate_report(self) -> None:
        """
        Populate covid records into model

        @param reports: a list of daily covid records
        @return: None
        @raise: This function doesn't raise any exception.
        """
        for report in self.reports:
            country = self.populate_country(report.pop("country"))

            instance = DailyReport(**report)
            setattr(instance, "country", country)

            try:
                instance.save()
            except IntegrityError:
                pass
