from rest_framework.test import APITransactionTestCase

from api.covid.tests.factories import CountryFactory


class SetUpClass(APITransactionTestCase):
    reset_sequences = True

    def setUp(self) -> None:
        self.countries = CountryFactory.create_batch(8)
