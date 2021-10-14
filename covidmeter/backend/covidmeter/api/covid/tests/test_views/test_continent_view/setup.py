from rest_framework.test import APITransactionTestCase

from api.covid.tests.factories import ContinentFactory


class SetUpClass(APITransactionTestCase):
    reset_sequences = True

    def setUp(self) -> None:
        self.continents = ContinentFactory.create_batch(3)
