from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Country


@receiver(post_save, sender=Country, dispatch_uid="Update_continent_population")
def update_continent_population(sender, instance, created, **kwargs):
    """
    Post save signal for adding country's population to it's continent's population
    """
    if created and instance.population:
        instance.continent.population += instance.population
        instance.continent.save()
