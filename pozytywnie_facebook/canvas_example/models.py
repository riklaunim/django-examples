from django.db.models import signals
from django.dispatch import receiver

from facebook_auth import models
from facebook_datastore import engines


@receiver(signals.post_save, sender=models.FacebookUser)
def update_datastore(sender, instance, **kwargs):
    for engine in engines.ENGINES_ENABLED:
        print('Running engine', engine)
        runner = engine(instance)
        runner.run()
