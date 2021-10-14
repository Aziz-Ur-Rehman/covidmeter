from django.core.management.base import BaseCommand

from api.covid.services.report_file_reader_service import load_reports_file
from api.covid.services.reports_populator_service import ReportsPopulatorService


class Command(BaseCommand):
    """
    Management command 'loadreports', reads daily reports from a csv file
    and populates the reports into the database.
    """

    help = "Loads reports from csv file into models"

    def add_arguments(self, parser):
        """
        Adds aguments to the management command
        """
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        """
        Handles the command to populate data from csv file into database
        """
        try:
            reports = load_reports_file(options["file_path"])
        except FileNotFoundError as err:
            self.stdout.write(self.style.ERROR(err))
            return

        ReportsPopulatorService(reports).populate_report()
        self.stdout.write(self.style.SUCCESS("Reports loaded successfully"))
