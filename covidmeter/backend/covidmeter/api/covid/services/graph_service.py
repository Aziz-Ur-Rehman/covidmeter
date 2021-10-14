from django.db.models import Avg, Sum

from api.covid.models import Continent, Country, DailyReport
from api.covid.serializers import (
    ContinentSerializer,
    CountrySerializer,
    GraphDataSerializer,
)


class GraphDataComputer:
    """
    GraphDataComputer class

    Attributes
    ----------
    continent: str
    geoid: str
    date: dict[str, str]
    """

    def __init__(self, continent: str, geoid: str, date: dict) -> None:
        self.geoid = geoid
        self.continent = continent
        self.date = date

    def eval_graph_data(self) -> dict:
        """
        Computes data that is required for covid stats graph

        @return: data for graph
        @raise: This function doesn't raise any exception.
        """
        data = {"data": self.eval_stats()}

        area_details = self.country_continent_details()

        if area_details:
            data.update(area_details)

        return data

    def country_continent_details(self) -> dict:
        """
        Fetches and returns data of a country or continent

        @return: data of country or continent
        @raise: This function doesn't raise any exception.
        """
        if self.continent:
            try:
                instance = Continent.objects.get(name__iexact=self.continent)
            except Continent.DoesNotExist:
                return {"continent": {}}

            serializer = ContinentSerializer(instance)
            return {"continent": serializer.data}
        elif self.geoid:
            try:
                instance = Country.objects.get(geoid__iexact=self.geoid)
            except Country.DoesNotExist:
                return {"country": {}}

            serializer = CountrySerializer(instance)
            return {"country": serializer.data}

        return None

    def eval_stats(self) -> list[dict]:
        """
        Fetches and returns sum of cases and deaths and
        their cumulative sums for all dates

        @return: sum of cases and deaths and their cumulative sums
        @raise: This function doesn't raise any exception.
        """
        if self.geoid:
            queryset = DailyReport.objects.filter(country__geoid__iexact=self.geoid)
        elif self.continent:
            queryset = DailyReport.objects.filter(
                country__continent__name__iexact=self.continent
            )
        else:
            queryset = DailyReport.objects.all()

        queryset = self.filter_date(queryset)

        queryset = (
            queryset.order_by("date")
            .values("date")
            .annotate(
                deaths=Sum("deaths"),
                cases=Sum("cases"),
                cases_per_100000=Avg("cases_per_100000"),
            )
        )

        statistics = GraphDataSerializer(queryset, many=True).data

        return self.cumulate_stats(statistics)

    def filter_date(self, queryset: any) -> any:
        """
        Filters results for date

        @param queryset: queryset of daily reports
        @return: queryset of daily reports with date filter
        @raise: This function doesn't raise any exception.
        """
        for key, value in self.date.items():
            if value:
                queryset = queryset.filter(**{"date__" + key: value})

        return queryset

    def cumulate_stats(self, statistics: list[dict]) -> list[dict]:
        """
        Calculate cumulative deaths and cases for all dates

        @param statistics: List of daily stats
        @return: List of stats with cumulative sum of deaths and cases
        @raise: This function doesn't raise any exception.
        """
        cum_deaths, cum_cases = 0, 0

        for stat_itter in range(len(statistics)):
            cum_cases += statistics[stat_itter]["cases"]
            statistics[stat_itter]["Cumulative Cases"] = cum_cases

            cum_deaths += statistics[stat_itter]["deaths"]
            statistics[stat_itter]["Cumulative Deaths"] = cum_deaths

        statistics_graph = [list(statistics[0].keys())]
        statistics_graph += [list(row.values()) for row in statistics]

        return statistics_graph
