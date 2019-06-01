from typing import List

from django.db.models import Count, Prefetch

from core import models


class DepartmentMixin:
    @staticmethod
    def get_queryset_default_or_prefetch(request):
        if 'user_not_in' in request.query_params:
            return models.Department.objects.all()
        return models.Department.objects.prefetch_related(
            Prefetch('users', queryset=models.User.objects.all())
        ).all()


class ChatMixin:
    @staticmethod
    def get_or_create_chat(users: List['models.User']):
        chat_users = models.ChatUser.objects.filter(
            user__in=users
        ).values('chat').annotate(
            counter=Count('id')
        ).filter(counter=2)

        if chat_users.exists():
            return models.Chat.objects.get(pk=chat_users[0]['chat'])

        chat = models.Chat.objects.create()
        for user in users:
            chat_user = models.ChatUser()
            chat_user.user = user
            chat_user.chat = chat
            chat_user.save()

        return chat
