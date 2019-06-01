from django.db.models import Prefetch
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core import models, serializers, serializers_params, mixins, filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_class = filters.UserFilter
    ordering_fields = '__all__'
    ordering = ('-id',)


class DepartmentViewSet(viewsets.ModelViewSet, mixins.DepartmentMixin):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    filter_class = filters.DepartmentFilter
    ordering_fields = '__all__'
    ordering = ('-id',)

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset_default_or_prefetch(request=request)
        return super(DepartmentViewSet, self).list(request, *args, **kwargs)


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = models.Notice.objects.all()
    serializer_class = serializers.NoticeSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)


class ChatViewSet(viewsets.ModelViewSet, mixins.ChatMixin):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)

    @action(detail=False, methods=['POST'])
    def get_or_create(self, request, *args, **kwargs):
        result_serializer = serializers_params.ChatSerializerParam(data=request.data, context={'request': request})
        result_serializer.is_valid(raise_exception=True)
        chat = self.get_or_create_chat(users=result_serializer.validated_data['users'])
        result_serializer = self.get_serializer(chat)
        return Response(data=result_serializer.data, status=status.HTTP_200_OK)


class ChatUserViewSet(viewsets.ModelViewSet):
    queryset = models.ChatUser.objects.all()
    serializer_class = serializers.ChatUserSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = models.ChatMessage.objects.all()
    serializer_class = serializers.ChatMessageSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)
