import factory


class ContinentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "covid.Continent"
        django_get_or_create = ("name",)

    name = factory.Faker("name")


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "covid.Country"
        django_get_or_create = (
            "name",
            "continent",
            "geoid",
            "country_code",
            "population",
        )

    name = factory.Faker("name")
    continent = factory.SubFactory(ContinentFactory)
    geoid = factory.Faker("uuid4")
    country_code = factory.Faker("uuid4")
    population = factory.Faker("pyint")


class DailyReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "covid.DailyReport"
        django_get_or_create = (
            "country",
            "date",
            "cases",
            "deaths",
            "cases_per_100000",
        )

    date = factory.Faker("date")
    country = factory.SubFactory(CountryFactory)
    cases = factory.Faker("pyint")
    deaths = factory.Faker("pyint")
    cases_per_100000 = factory.Faker("pyfloat")
