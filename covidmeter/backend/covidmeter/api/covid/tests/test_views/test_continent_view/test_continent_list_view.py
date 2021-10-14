from rest_framework import status

from .setup import SetUpClass


class ContinentListViewsetTests(SetUpClass):
    def test_continent_list_status(self) -> None:
        """Test status code for continent list"""
        response = self.client.get("/api/covid/continent/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_continent_list_count(self) -> None:
        """Test number of continents"""
        response = self.client.get("/api/covid/continent/", format="json")

        self.assertEqual(len(response.data), 3)

    def test_continent_data(self) -> None:
        """Test continent's data"""
        response = self.client.get("/api/covid/continent/", format="json")

        self.assertEqual(response.data[0]["name"], self.continents[0].name)
        self.assertEqual(response.data[0]["population"], self.continents[0].population)


class ContinentRetrieveViewsetTests(SetUpClass):
    def test_continent_retrieve_status(self) -> None:
        """Test status code for continent retrieve"""
        response = self.client.get("/api/covid/continent/1/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_continent_data(self) -> None:
        """Test continent's data"""
        response = self.client.get("/api/covid/continent/1/", format="json")

        self.assertEqual(response.data["id"], self.continents[0].id)
        self.assertEqual(response.data["name"], self.continents[0].name)
        self.assertEqual(response.data["population"], self.continents[0].population)

    def test_continent_404(self) -> None:
        """Test continent 404"""
        response = self.client.get("/api/covid/continent/15/", format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
