from rest_framework import status

from .setup import SetUpClass


class GraphGetTests(SetUpClass):
    def test_graph_status(self) -> None:
        """Test status code for valid graph"""
        response = self.client.get("/api/covid/graph/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_country_graph_status(self) -> None:
        """Test valid country graph status code"""
        response = self.client.get(
            f"/api/covid/graph/country/{self.reports[0].country.geoid}", format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_country_graph_status_data(self) -> None:
        """Test invalid country graph status code and message"""
        response = self.client.get("/api/covid/graph/country/ilta", format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "Country not found")

    def test_valid_continent_graph_status(self) -> None:
        """Test valid continent graph status code"""
        response = self.client.get(
            f"/api/covid/graph/continent/{self.reports[0].country.continent.name}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_country_graph_status_data(self) -> None:
        """Test invalid continent graph status code and message"""
        response = self.client.get("/api/covid/graph/continent/ilta", format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "Continent not found")
