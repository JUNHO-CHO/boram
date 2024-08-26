# myapp/signals.py

from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Article

@receiver(m2m_changed, sender=Article.like_users.through)
def update_like_count(sender, instance, **kwargs):
    instance.like_count = instance.like_users.count()
    instance.save()
