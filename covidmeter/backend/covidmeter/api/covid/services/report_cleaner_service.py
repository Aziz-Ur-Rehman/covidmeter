class ReportCleanerService:
    """
    ReportCleanerService class

    Attributes
    ----------
    COUNTRY_DETAIL_TAGS: list[str]
    """

    COUNTRY_DETAIL_TAGS = ["name", "geoid", "country_code", "population", "continent"]

    def clean_reports(self, reports: list[dict]) -> list[dict]:
        """
        Cleans the daily covid records that are read from files.

        @param reports: uncleaned covid records
        @return: cleaned covid records
        @raise: This function doesn't raise any exception.
        """
        for report_itter in range(len(reports)):
            report = reports[report_itter]

            report = self.convert_datatypes(report)
            report = self.country_details(report)
            report = self.remove_date_keys(report)
            report = self.format_date(report)

            reports[report_itter] = report

        return reports

    def convert_datatypes(self, report: dict) -> dict:
        """
        Converts data type of a record value to int or float, if possible.

        @param reports: daily covid record
        @return: daily covid record with converted datatypes
        @raise: This function doesn't raise any exception.
        """
        for key, value in report.items():
            try:
                if value == "":
                    report[key] = None
                elif key == "cases_per_100000":
                    report[key] = float(value)
                else:
                    report[key] = int(value)
            except ValueError:
                pass

        return report

    def country_details(self, report: dict) -> dict:
        """
        Pop country info from record and store it in nested dict.

        @param reports: daily covid record
        @return: daily covid record with nested country info dict
        @raise: This function doesn't raise any exception.
        """
        report["name"] = report["country"]
        report["country"] = {key: report.pop(key) for key in self.COUNTRY_DETAIL_TAGS}

        return report

    def remove_date_keys(self, report: dict) -> dict:
        """
        Pops unwanted keys from covid record.

        @param reports: daily covid record
        @return: daily covid record with cleaned keys
        @raise: This function doesn't raise any exception.
        """
        return {
            key: value
            for key, value in report.items()
            if key not in ["day", "month", "year"]
        }

    def format_date(self, report: dict) -> dict:
        """
        Converts date format from DD/MM/YYYY to YYYY-MM-DD

        @param reports: daily covid record
        @return: daily covid record with formated date
        @raise: This function doesn't raise any exception.
        """
        report["date"] = "-".join(reversed(report["date"].split("/")))

        return report
