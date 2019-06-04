from celery import shared_task

from core import models


@shared_task()
def save_messages(params: dict):
    print(params)
    chat = models.Chat.objects.get(pk=params.get('chat'))
    user = models.User.objects.get(username=params.get('username'))
    models.ChatMessage.objects.create(
        chat=chat,
        user=user,
        message=params.get('message')
    )
