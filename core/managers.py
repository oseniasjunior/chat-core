from typing import List

from django.db import models
from django.db.models import Count

from core import models as core_models


class ChatUserManager(models.Manager):
    def chat_user_by_users(self, users: List['core_models.User']):
        return self.get_queryset().filter(
            user__in=users
        ).values('chat').annotate(
            counter=Count('id')
        ).filter(counter=2)
