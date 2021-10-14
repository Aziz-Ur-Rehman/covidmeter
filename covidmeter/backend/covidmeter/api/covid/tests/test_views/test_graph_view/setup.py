from rest_framework.test import APITransactionTestCase

from api.covid.tests.factories import DailyReportFactory


class SetUpClass(APITransactionTestCase):
    reset_sequences = True

    def setUp(self) -> None:
        self.reports = DailyReportFactory.create_batch(20)
