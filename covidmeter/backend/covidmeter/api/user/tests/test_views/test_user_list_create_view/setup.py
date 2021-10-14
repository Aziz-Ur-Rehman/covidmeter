from rest_framework.test import APITransactionTestCase

from api.user.tests.factories import UserFactory


class SetUpClass(APITransactionTestCase):
    reset_sequences = True

    def setUp(self) -> None:
        self.users = UserFactory.create_batch(20)
