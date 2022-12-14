from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import PublishStateOptions, Video


@receiver(pre_save, sender=Video)
def publish_state_pre_save(sender, instance, *args, **kwargs):
    if instance.state == PublishStateOptions.PUBLISH and instance.publish_date is None:
        instance.publish_date = timezone.now()
    else:
        instance.publish_date = None
