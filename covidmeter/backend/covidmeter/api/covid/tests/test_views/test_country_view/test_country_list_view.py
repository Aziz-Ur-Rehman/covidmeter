from rest_framework import status

from .setup import SetUpClass


class CountryListTests(SetUpClass):
    def test_country_list_status(self) -> None:
        """Test status code for country list"""
        response = self.client.get("/api/covid/country/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_list_count(self) -> None:
        """Test number of countries"""
        response = self.client.get("/api/covid/country/", format="json")

        self.assertEqual(len(response.data), 8)


class CountryRetrieveViewsetTests(SetUpClass):
    def test_country_retrieve_status(self) -> None:
        """Test status code for country retrieve"""
        response = self.client.get("/api/covid/country/1/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_data(self) -> None:
        """Test country's data"""
        response = self.client.get("/api/covid/country/1/", format="json")

        self.assertEqual(
            response.data["id"],
            self.countries[0].id,
        )
        self.assertEqual(
            response.data["name"],
            self.countries[0].name,
        )
        self.assertEqual(
            response.data["geoid"],
            self.countries[0].geoid,
        )
        self.assertEqual(
            response.data["country_code"],
            self.countries[0].country_code,
        )
        self.assertEqual(
            response.data["population"],
            self.countries[0].population,
        )

    def test_country_404(self) -> None:
        """Test country 404"""
        response = self.client.get("/api/covid/country/15/", format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
