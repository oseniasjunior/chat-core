from urllib import parse

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from core import tasks


class ConsumerBase(AsyncJsonWebsocketConsumer):

    def get_query_params(self):
        query_string = self.scope['query_string'].decode()
        return dict(parse.parse_qsl(query_string))

    def get_group_name(self):
        raise NotImplementedError('You must create subclasses and implement this method')

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(self.get_group_name(), self.channel_name)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.get_group_name(), self.channel_name)

    async def group_message(self, event):
        await self.send_json(content=event["content"])


class ConversationConsumer(ConsumerBase):
    def get_group_name(self):
        query_params = self.get_query_params()
        return 'chat-{}'.format(query_params.get('chat'))

    async def receive_json(self, content, **kwargs):
        params = dict()
        params['chat'] = self.get_query_params().get('chat')
        params['username'] = content['username']
        params['message'] = content['message']

        tasks.save_messages.apply_async([params])
        await self.channel_layer.group_send(
            self.get_group_name(),
            {"type": "group.message", "content": content}
        )
