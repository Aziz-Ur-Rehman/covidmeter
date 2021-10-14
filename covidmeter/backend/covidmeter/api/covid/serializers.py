from rest_framework import serializers

from .models import Continent, Country, DailyReport


class ContinentSerializer(serializers.ModelSerializer):
    """
    Serializes the instances of :model:`covid.Continent`.
    """

    class Meta:
        model = Continent
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    """
    Serializes the instances of :model:`covid.Country`.
    """

    continent = ContinentSerializer()

    class Meta:
        model = Country
        fields = "__all__"


class DailyReportSerializer(serializers.ModelSerializer):
    """
    Serializes the instances of :model:`covid.DailyReports`.
    """

    country = CountrySerializer(read_only=True)

    class Meta:
        model = DailyReport
        fields = "__all__"


class GraphDataSerializer(serializers.Serializer):
    """
    Serializes the queryset that contains the data for plotting a graphs.
    """

    date = serializers.DateField()
    cases = serializers.IntegerField()
    deaths = serializers.IntegerField()
    cases_per_100000 = serializers.FloatField()
