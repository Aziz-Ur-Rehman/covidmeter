import factory


class ScenarioHashFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "scenario.ScenarioHash"
        django_get_or_create = (
            "param_hash",
            "params",
            "result",
        )


class UserScenarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "scenario.UserScenario"
        django_get_or_create = (
            "name",
            "user",
            "scenario_hash",
        )

    name = factory.Faker("uuid4")
