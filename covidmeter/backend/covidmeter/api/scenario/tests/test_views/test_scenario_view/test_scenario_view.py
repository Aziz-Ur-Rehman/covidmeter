from rest_framework import status

from api.scenario.models import UserScenario
from .setup import SetUpClass


class ScenerioListTests(SetUpClass):
    def test_unauthorize_list_scenario_status(self) -> None:
        """Test status code for scenario unauthorized list"""
        self.client.force_authenticate(user=None)

        response = self.client.get("/api/scenario/", format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_scenario_list(self) -> None:
        """Test list scenarios with authenicated request"""

        response = self.client.get("/api/scenario/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_scenario_count(self) -> None:
        """Test the count and pagination"""
        response = self.client.get("/api/scenario/", format="json")

        self.assertEqual(response.data["count"], 5)
        self.assertLessEqual(len(response.data["results"]), 100)

    def test_scenario_data(self) -> None:
        """Test data"""
        response = self.client.get("/api/scenario/", format="json")

        self.assertEqual(
            response.data["results"][0]["id"],
            self.scenarios[0].id,
        )
        self.assertEqual(
            response.data["results"][0]["name"],
            self.scenarios[0].name,
        )
        self.assertEqual(
            response.data["results"][0]["is_delete"],
            self.scenarios[0].is_delete,
        )
        self.assertEqual(response.data["results"][0]["user"], self.scenarios[0].user.id)
        self.assertEqual(
            response.data["results"][0]["scenario_hash"]["id"],
            self.scenarios[0].scenario_hash.id,
        )
        self.assertEqual(
            response.data["results"][0]["scenario_hash"]["result"],
            self.scenarios[0].scenario_hash.result,
        )
        self.assertEqual(
            response.data["results"][0]["scenario_hash"]["params"],
            self.scenarios[0].scenario_hash.params,
        )


class ScenerioRetrieveTests(SetUpClass):
    def test_unauthorize_retrieve_scenario_status(self) -> None:
        """Test status code for scenario unauthorized retrieve"""
        self.client.force_authenticate(user=None)

        response = self.client.get("/api/scenario/1/", format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_scenario_retrieve(self) -> None:
        """Test retrieve scenarios with authenicated request"""
        response = self.client.get("/api/scenario/1/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_forbiden_scenario_retrieve(self) -> None:
        """Test retrieve forbiden scenarios with authenicated request
        as user with id 1 has only first five scenarios"""
        response = self.client.get("/api/scenario/6/", format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_scenario_for_other_user(self) -> None:
        """Test retrieve scenarios with authenicated request"""
        self.client.force_authenticate(user=self.users[1])
        response = self.client.get("/api/scenario/6/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ScenerioCreateTests(SetUpClass):
    def test_unauthorize_create_scenario_status(self) -> None:
        """Test status code for scenario unauthorized create"""
        self.client.force_authenticate(user=None)

        response = self.client.post("/api/scenario/", format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_scenario_create(self) -> None:
        """Test create scenarios with authenicated request"""
        data = {
            "user": 1,
            "name": "test1",
            "scenario_hash": {"country": ["pk", "ind"], "year": 2021},
        }

        response = self.client.post("/api/scenario/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"], data["user"])
        self.assertEqual(response.data["name"], data["name"])

    def test_same_hash_scenario_create(self) -> None:
        """
        Test create scenarios with authenicated request and equivalent
        but unsorted hashes
        """
        data1 = {
            "user": 1,
            "name": "test1",
            "scenario_hash": {"country": ["pk", "ind"], "year": 2021},
        }

        data2 = {
            "user": 1,
            "name": "test2",
            "scenario_hash": {"country": ["ind", "pk"], "year": 2021},
        }

        response1 = self.client.post("/api/scenario/", data=data1, format="json")
        response2 = self.client.post("/api/scenario/", data=data2, format="json")

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response1.data["scenario_hash"], response2.data["scenario_hash"]
        )

    def test_forbiden_scenario_create(self) -> None:
        """Test create forbiden scenarios with authenicated request"""
        data = {
            "user": 2,
            "name": "test1",
            "scenario_hash": {"country": ["pk", "ind"], "year": 2021},
        }

        response = self.client.post("/api/scenario/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"], 1)

    def test_same_name_scenario_create(self) -> None:
        """
        Test create scenarios with name already existed for user
        """
        data = {
            "user": 1,
            "name": "s1",
            "scenario_hash": {"country": ["pk", "ind"], "year": 2021},
        }

        response = self.client.post("/api/scenario/", data=data, format="json")
        response_dupicate_name = self.client.post(
            "/api/scenario/", data=data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response_dupicate_name.status_code, status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            response_dupicate_name.data,
            {"non_field_errors": ["The fields name, user must make a unique set."]},
        )


class ScenerioUpdateTests(SetUpClass):
    def test_unauthorize_update_scenario_status(self) -> None:
        """Test status code for scenario unauthorized update"""
        self.client.force_authenticate(user=None)

        response = self.client.patch("/api/scenario/1/", format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_scenario_update(self) -> None:
        """Test update scenarios with authenicated request"""
        data = {"name": "test_name"}

        response = self.client.patch("/api/scenario/1/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["name"], "test_name")

    def test_forbiden_scenario_update(self) -> None:
        """Test update scenarios with forbiden request
        as user with id 1 has only first five scenarios"""
        data = {"name": "test_name"}

        response = self.client.patch("/api/scenario/6/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_forbiden_scenario_user_update(self) -> None:
        """Test update user scenarios with forbiden request"""
        data = {"name": "test_name", "user": 2}

        response = self.client.patch("/api/scenario/1/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["name"], "test_name")
        self.assertEqual(response.data["user"], 1)

    def test_same_name_scenario_update(self) -> None:
        """
        Test update scenarios with name already existed for user
        """
        data = {"name": "test_name"}

        response = self.client.patch("/api/scenario/1/", data=data, format="json")
        response_duplicate_name = self.client.patch(
            "/api/scenario/2/", data=data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response_duplicate_name.status_code, status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            response_duplicate_name.data,
            {"non_field_errors": ["The fields name, user must make a unique set."]},
        )


class ScenarioDeleteTests(SetUpClass):
    def test_unauthorized_scenario_delete_status(self) -> None:
        """Test status code for scenario unauthorized delete"""
        self.client.force_authenticate(user=None)

        response = self.client.delete("/api/scenario/1/", format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_other_user_update(self) -> None:
        """Test delete user with authenicated request"""
        response = self.client.delete("/api/scenario/1/", format="json")
        scenario = UserScenario.objects.get(id=1)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(scenario.is_delete, True)

    def test_forbiden_delete_scenario(self) -> None:
        """Test delete scenario with authenicated request for other user
        as user with id 1 has only first five scenarios"""
        response = self.client.delete("/api/scenario/6/", format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_scenario_twice(self) -> None:
        """Test delete scenario twice with authenicated request"""
        response = self.client.delete("/api/scenario/1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete("/api/scenario/1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
