from datetime import datetime

from django.contrib.auth import get_user_model
from rest_framework import status

from .setup import SetUpClass

User = get_user_model()


class UserRetrieveTests(SetUpClass):
    def test_user_retrieve_status(self) -> None:
        """Test status code for user retrieve"""
        response = self.client.get("/api/user/1/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_data(self) -> None:
        """Test user data"""
        response = self.client.get("/api/user/1/", format="json")

        self.assertEqual(
            response.data["id"],
            self.users[0].id,
        )
        self.assertEqual(
            response.data["email"],
            self.users[0].email,
        )
        self.assertEqual(
            response.data["first_name"],
            self.users[0].first_name,
        )
        self.assertEqual(
            response.data["last_name"],
            self.users[0].last_name,
        )
        self.assertEqual(
            response.data["profile_picture"],
            self.users[0].profile_picture,
        )
        self.assertEqual(
            response.data["is_staff"],
            False,
        )
        self.assertEqual(
            response.data["is_active"],
            True,
        )
        self.assertEqual(
            response.data["is_superuser"],
            False,
        )


class UserUpdateTests(SetUpClass):
    def test_unauthenticated_user_update_status(self) -> None:
        """Test update user with unauthenticated request"""
        self.client.force_authenticate(user=None)

        data = {
            "email": "test@gmail.com",
            "password": "test",
            "first_name": "test",
            "last_name": "user",
            "date_of_birth": "2000-04-25",
        }
        response = self.client.patch("/api/user/1/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_update(self) -> None:
        """Test update user with valid authenticated request"""
        data = {
            "date_of_birth": datetime.today().strftime("%Y-%m-%d"),
        }
        response = self.client.patch("/api/user/1/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["date_of_birth"], datetime.today().strftime("%Y-%m-%d")
        )

    def test_authenticated_other_user_update(self) -> None:
        """Test update user with authenicated request and for other user"""
        data = {
            "date_of_birth": datetime.today().strftime("%Y-%m-%d"),
        }
        response = self.client.patch("/api/user/2/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_update_with_already_existed_email(self) -> None:
        """Test update user with already existed email"""
        data = {
            "email": self.users[1].email,
        }
        response = self.client.patch("/api/user/1/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"email": ["user with this email address already exists."]}
        )


class UserDeleteTests(SetUpClass):
    def test_unauthorized_user_delete_status(self) -> None:
        """Test status code for user unauthorized delete"""
        self.client.force_authenticate(user=None)

        response = self.client.delete("/api/user/1/", format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_other_user_update(self) -> None:
        """Test delete user with authenicated request"""
        response = self.client.delete("/api/user/1/", format="json")

        user = User.objects.get(id=1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(user.is_active, False)

    def test_authenticated_other_user_delete(self) -> None:
        """Test delete user with authenicated request for other user"""

        response = self.client.delete("/api/user/2/", format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
