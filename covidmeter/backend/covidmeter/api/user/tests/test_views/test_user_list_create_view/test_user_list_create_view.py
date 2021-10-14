from rest_framework import status

from .setup import SetUpClass


class UserListTests(SetUpClass):
    def test_user_list_status(self) -> None:
        """Test status code for user list"""
        response = self.client.get("/api/user/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_users_count(self) -> None:
        """Test the count and pagination"""
        response = self.client.get("/api/user/", format="json")

        self.assertEqual(response.data["count"], 20)
        self.assertLessEqual(len(response.data["results"]), 100)

    def test_users_data(self) -> None:
        """Test data"""
        response = self.client.get("/api/user/", format="json")

        self.assertEqual(
            response.data["results"][0]["id"],
            self.users[0].id,
        )
        self.assertEqual(
            response.data["results"][0]["email"],
            self.users[0].email,
        )
        self.assertEqual(
            response.data["results"][0]["first_name"],
            self.users[0].first_name,
        )
        self.assertEqual(
            response.data["results"][0]["last_name"],
            self.users[0].last_name,
        )
        self.assertEqual(
            response.data["results"][0]["profile_picture"],
            self.users[0].profile_picture,
        )
        self.assertEqual(
            response.data["results"][0]["is_staff"],
            False,
        )
        self.assertEqual(
            response.data["results"][0]["is_active"],
            True,
        )
        self.assertEqual(
            response.data["results"][0]["is_superuser"],
            False,
        )


class UserCreateTest(SetUpClass):
    def test_create_user(self) -> None:
        """Test simple create user status and data"""
        data = {
            "email": "test@gmail.com",
            "password": "test",
            "first_name": "test",
            "last_name": "user",
            "date_of_birth": "2000-04-25",
        }

        response = self.client.post("/api/user/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertEqual(response.data["email"], data["email"])
        self.assertEqual(response.data["first_name"], data["first_name"])
        self.assertEqual(response.data["last_name"], data["last_name"])
        self.assertEqual(response.data["profile_picture"], None)
        self.assertEqual(response.data["date_of_birth"], data["date_of_birth"])
        self.assertEqual(response.data["is_staff"], False)
        self.assertEqual(response.data["is_active"], True)
        self.assertEqual(response.data["is_superuser"], False)
        self.assertIn("last_login", response.data)
        self.assertIn("date_joined", response.data)

    def test_create_user_without_email(self) -> None:
        """Test create user without email address"""
        data = {
            "password": "test",
            "first_name": "test",
            "last_name": "user",
            "date_of_birth": "2000-04-25",
        }

        response = self.client.post("/api/user/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"email": ["This field is required."]})

    def test_create_user_without_password(self) -> None:
        """Test create user without password"""
        data = {
            "email": "test@gmail.com",
            "first_name": "test",
            "last_name": "user",
            "date_of_birth": "2000-04-25",
        }

        response = self.client.post("/api/user/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"password": ["This field is required."]})

    def test_create_user_with_same_email(self) -> None:
        """test create user with an email that already exists"""
        data = {
            "email": self.users[0].email,
            "password": "test",
            "first_name": "test",
            "last_name": "user",
            "date_of_birth": "2000-04-25",
        }

        response = self.client.post("/api/user/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"email": ["user with this email address already exists."]}
        )

    def test_create_user_with_invalid_dob(self) -> None:
        """test create user with invalid date format"""
        data = {
            "email": "test@gmail.com",
            "password": "test",
            "first_name": "test",
            "last_name": "user",
            "date_of_birth": "2000-04",
        }

        response = self.client.post("/api/user/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data,
            {
                "date_of_birth": [
                    "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
                ]
            },
        )

    def test_create_user_with_invalid_permissions(self) -> None:
        """test create user with is_staff and is_superuser as True and is_active=False"""
        data = {
            "email": "test@gmail.com",
            "password": "test",
            "first_name": "test",
            "last_name": "user",
            "date_of_birth": "2000-04-25",
            "is_staff": True,
            "is_superuser": True,
            "is_active": False,
        }

        response = self.client.post("/api/user/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["is_staff"], False)
        self.assertEqual(response.data["is_active"], True)
        self.assertEqual(response.data["is_superuser"], False)
