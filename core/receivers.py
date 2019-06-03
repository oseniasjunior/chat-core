from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from core import models


@receiver(post_save, sender=models.User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
