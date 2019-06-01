from typing import List

from django.db.models import Count

from core import models


class ChatActions:
    @staticmethod
    def get_or_create_chat(users: List['models.User']):
        chat_users = models.ChatUser.objects.chat_user_by_users(users=users)
        if chat_users.exists():
            return models.Chat.objects.get(pk=chat_users[0]['chat'])

        chat = models.Chat.objects.create()
        for user in users:
            chat_user = models.ChatUser()
            chat_user.user = user
            chat_user.chat = chat
            chat_user.save()

        return chat
