from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from core import models, exceptions


class ChatSerializerParam(serializers.Serializer):
    users = serializers.ListField(
        child=serializers.HyperlinkedRelatedField(
            view_name='user-detail',
            queryset=models.User.objects.all(),
            required=True
        ),
        min_length=2,
        max_length=2,
        error_messages={'min_length': _('Must have at least 2 users'), 'max_length': _('Must have a maximum 2 users')}
    )

    def validate(self, attrs):
        users = attrs['users']
        if users[0] == users[1]:
            raise exceptions.UserCanNotBeSome()
        return super(ChatSerializerParam, self).validate(attrs=attrs)
