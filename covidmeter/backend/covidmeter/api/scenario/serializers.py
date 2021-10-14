from rest_framework import serializers

from .models import ScenarioHash, UserScenario


class ScenarioHashSerializer(serializers.ModelSerializer):
    """
    Serializes the instances of :model:`scenario.ScenarioHash`.
    """

    class Meta:
        model = ScenarioHash
        fields = "__all__"


class UserScenarioSerializer(serializers.ModelSerializer):
    """
    Serializes the instances of :model:`scenario.UserScenario`.
    """

    scenario_hash = ScenarioHashSerializer(read_only=True)

    class Meta:
        model = UserScenario
        fields = "__all__"
