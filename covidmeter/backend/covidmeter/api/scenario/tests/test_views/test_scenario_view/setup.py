import random

import factory
from rest_framework.test import APITransactionTestCase

from api.covid.models import DailyReport
from api.covid.tests.factories import (
    ContinentFactory,
    CountryFactory,
    DailyReportFactory,
)
from api.scenario.models import UserScenario
from api.scenario.tests.factories import ScenarioHashFactory, UserScenarioFactory
from api.scenario.services.hash_service import HashService
from api.user.tests.factories import UserFactory


class SetUpClass(APITransactionTestCase):
    reset_sequences = True

    def setUp(self) -> None:
        self.continents = self.create_continents()
        self.countries = self.create_countries()
        self.reports = self.create_reports()
        self.users = UserFactory.create_batch(2)
        self.scenarios = self.create_scenarios()

        self.client.force_authenticate(user=self.users[0])

    def create_continents(self) -> any:
        name = ["asia", "europe"]
        return ContinentFactory.create_batch(
            2,
            name=factory.Sequence(lambda continent_index: name[continent_index % 2]),
        )

    def create_countries(self) -> any:
        country_data = [
            {"name": "japan", "geoid": "jpn", "continent": self.continents[0]},
            {"name": "pakistan", "geoid": "pk", "continent": self.continents[0]},
            {"name": "india", "geoid": "ind", "continent": self.continents[0]},
            {"name": "norway", "geoid": "nw", "continent": self.continents[1]},
            {"name": "finland", "geoid": "fn", "continent": self.continents[1]},
            {"name": "Austria", "geoid": "as", "continent": self.continents[1]},
        ]

        return CountryFactory.create_batch(
            6,
            name=factory.Sequence(
                lambda country_index: country_data[country_index % 6]["name"]
            ),
            geoid=factory.Sequence(
                lambda country_index: country_data[country_index % 6]["geoid"]
            ),
            continent=factory.Sequence(
                lambda country_index: country_data[country_index % 6]["continent"]
            ),
        )

    def create_reports(self) -> any:
        for country in self.countries:
            DailyReportFactory.create_batch(
                30,
                country=country,
                date=factory.Sequence(lambda day: f"2021-09-{(day%30)+1:02}"),
            )

        return DailyReport.objects.all()

    def create_scenarios(self) -> any:
        for user in self.users:
            for _ in range(5):
                scenario_hash_instance = self.create_scenario_hash()
                UserScenarioFactory(scenario_hash=scenario_hash_instance, user=user)

        return UserScenario.objects.all()

    def scenario_country_list(self) -> list[str]:
        if random.randint(0, 1):
            return [
                self.countries[random.randint(0, len(self.countries) - 1)].geoid
                for _ in range(random.randint(0, len(self.countries)))
            ]
        return []

    def scenario_continent_list(self) -> list[str]:
        if random.randint(0, 1):
            return [
                self.continents[random.randint(0, len(self.continents) - 1)].name
                for _ in range(random.randint(0, len(self.continents)))
            ]

        return []

    def create_random_params(self) -> dict:
        day = random.randint(1, 60)
        return {
            "day": None if day > 30 else day,
            "country": self.scenario_country_list(),
            "continent": self.scenario_continent_list(),
        }

    def create_scenario_hash(self) -> any:
        params = self.create_random_params()
        hash_handler = HashService(params)

        return ScenarioHashFactory.create(
            params=hash_handler.params,
            param_hash=hash_handler.hash_param,
            result=hash_handler.compute_result(),
        )
