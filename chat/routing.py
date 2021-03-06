from channels.routing import ProtocolTypeRouter, URLRouter
from channels.sessions import SessionMiddlewareStack
from django.urls import path

from core import consumers

urlrouter = [
    path('conversation/', consumers.ConversationConsumer),
]

application = ProtocolTypeRouter({
    "websocket": SessionMiddlewareStack(
        URLRouter(urlrouter),
    ),
})
