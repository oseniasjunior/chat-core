from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from core import models


class SerializerBase(FlexFieldsModelSerializer, serializers.HyperlinkedModelSerializer):

    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        fields.insert(0, 'id')
        return fields


class UserSerializer(SerializerBase):
    class Meta:
        model = models.User
        fields = ['url', 'id', 'username']


class DepartmentSerializer(SerializerBase):
    class Meta:
        model = models.Department
        fields = '__all__'

    expandable_fields = {
        'users': (
            UserSerializer,
            {'source': 'users', 'fields': ['url', 'id', 'username'], 'many': True}
        )
    }


class NoticeSerializer(SerializerBase):
    class Meta:
        model = models.Notice
        fields = '__all__'


class ChatSerializer(SerializerBase):
    class Meta:
        model = models.Chat
        fields = '__all__'


class ChatUserSerializer(SerializerBase):
    class Meta:
        model = models.ChatUser
        fields = '__all__'


class ChatMessageSerializer(SerializerBase):
    username = serializers.SlugRelatedField(read_only=True, source='user', slug_field='username')

    class Meta:
        model = models.ChatMessage
        fields = '__all__'
