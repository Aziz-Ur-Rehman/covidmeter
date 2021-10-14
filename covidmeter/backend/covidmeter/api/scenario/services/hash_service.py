import hashlib
import json

from api.covid.services.graph_service import GraphDataComputer
from api.scenario.models import ScenarioHash


class HashService:
    """
    HashService class

    Attributes
    ----------
    params: dict
    date: dict
    hash_params: str
    """

    def __init__(self, params: dict) -> None:
        self.params = self.sort_params(params)
        self.date = {
            "year": self.params.get("year"),
            "month": self.params.get("month"),
            "day": self.params.get("day"),
        }
        self.hash_param = self.compute_hash()

    def sort_params(self, params: dict) -> dict:
        """
        Sorts and lower countries and continents

        @param params: A dict of parameters
        @return: A param dict with sorted countries and continents
        @raises: Raises no exception
        """
        countries = params.get("country")
        countries = [country.upper() for country in countries] if countries else []

        continents = params.get("continent")
        continents = [cont.upper() for cont in continents] if continents else []

        params["country"] = sorted(list(set(countries)))
        params["continent"] = sorted(list(set(continents)))

        return params

    def compute_hash(self) -> any:
        """
        Compute hash for params

        @return: SHA256 Hash
        @raises: Raises no exception
        """
        dumped_params = json.dumps(self.params, sort_keys=True).encode("utf-8")
        return hashlib.sha256(dumped_params).digest()

    def get_or_create_hash(self) -> ScenarioHash:
        """
        Gets or creates a new hash

        @return: Scenario hash instance
        @raises: Raises no exception
        """

        instance, created = ScenarioHash.objects.get_or_create(
            param_hash=self.hash_param
        )
        if created:
            instance.params = self.params
            instance.result = self.compute_result()
            instance.save()

        return instance

    def compute_result(self) -> dict:
        """
        Computes the results for a hash

        @return: A dict with hash results
        @raises: Raises no exception
        """
        result = {"country": [], "continent": []}
        for cont in self.params["continent"]:
            result["continent"].append(self.graph_data(continent=cont))

        for country in self.params["country"]:
            result["country"].append(self.graph_data(country=country))

        if not (len(self.params["country"]) or len(self.params["continent"])):
            result["world"] = self.graph_data()

        return result

    def graph_data(self, continent=None, country=None) -> dict:
        """
        Computer graph data for a continent or country

        @param continent: continent name
        @param country: country geoid
        @return: a dict with graph details
        @raises: Raises no exception
        """
        graph_computer = GraphDataComputer(continent, country, self.date)
        return graph_computer.eval_graph_data()
