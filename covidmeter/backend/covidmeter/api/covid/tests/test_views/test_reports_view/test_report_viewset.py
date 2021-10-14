from rest_framework import status

from .setup import SetUpClass


class ReportsListTests(SetUpClass):
    def test_list_reports_status(self) -> None:
        """Test the status code of the response"""
        response = self.client.get("/api/covid/report/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_reports_count(self) -> None:
        """Test the count and pagination"""
        response = self.client.get("/api/covid/report/", format="json")

        self.assertEqual(response.data["count"], 101)
        self.assertLessEqual(len(response.data["results"]), 100)

    def test_reports_data(self) -> None:
        """Test data"""
        response = self.client.get("/api/covid/report/", format="json")

        self.assertEqual(
            response.data["results"][0]["id"],
            self.reports[0].id,
        )
        self.assertEqual(
            response.data["results"][0]["country"]["id"],
            self.reports[0].country.id,
        )
        self.assertEqual(
            response.data["results"][0]["cases"],
            self.reports[0].cases,
        )
        self.assertEqual(
            response.data["results"][0]["deaths"],
            self.reports[0].deaths,
        )
        self.assertEqual(
            response.data["results"][0]["cases_per_100000"],
            self.reports[0].cases_per_100000,
        )

    def test_reports_valid_country_filter(self) -> None:
        """Test country filtrer"""
        response = self.client.get(
            f"/api/covid/report/?country_geoid={self.reports[0].country.geoid}",
            format="json",
        )

        self.assertEqual(response.data["count"], 1)
        self.assertLessEqual(len(response.data["results"]), 100)

    def test_reports_invalid_country_filter(self) -> None:
        """Test invalid country filtrer"""
        response = self.client.get(
            "/api/covid/report/?country_geoid=waj", format="json"
        )

        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])


class ReportsRetrieveTests(SetUpClass):
    def test_retrieve_reports_status(self) -> None:
        """Test status code for valid request"""
        response = self.client.get("/api/covid/report/1/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reports_data(self) -> None:
        """Test data"""
        response = self.client.get("/api/covid/report/1/", format="json")

        self.assertEqual(
            response.data["id"],
            self.reports[0].id,
        )
        self.assertEqual(
            response.data["country"]["id"],
            self.reports[0].country.id,
        )
        self.assertEqual(
            response.data["cases"],
            self.reports[0].cases,
        )
        self.assertEqual(
            response.data["deaths"],
            self.reports[0].deaths,
        )
        self.assertEqual(
            response.data["cases_per_100000"],
            self.reports[0].cases_per_100000,
        )

    def test_report_not_found_status(self) -> None:
        """Test invalid country status code and message"""
        response = self.client.get("/api/covid/report/102/", format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
