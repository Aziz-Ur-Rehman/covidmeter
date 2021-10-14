from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ScenarioHash(models.Model):
    """
    Stores a single scenario hash entry containing its params and results.
    """

    class Meta:
        verbose_name = "Scenario result"
        verbose_name_plural = "Scenario results"

    params = models.JSONField(blank=True, null=True)
    param_hash = models.BinaryField(unique=True)
    result = models.JSONField(blank=True, null=True)


class UserScenario(models.Model):
    """
    Stores a single User scenario entry, related to :model:`scenario.ScenarioHash`.
    """

    class Meta:
        verbose_name = "User Scenario"
        verbose_name_plural = "User Scenarios"
        unique_together = ("name", "user")

    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scenario_hash = models.ForeignKey(
        ScenarioHash, on_delete=models.CASCADE, null=True, blank=True
    )
    is_delete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
