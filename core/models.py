from django.db import models
from django.utils.translation import ugettext_lazy as _


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
        verbose_name=_('Id')
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True,
        verbose_name=_('Active')
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        null=False,
        auto_now_add=True,
        verbose_name=_('Created at')
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        null=True,
        auto_now=True,
        verbose_name=_('Modified at')
    )

    class Meta:
        abstract = True
        managed = True


class Department(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=64,
        null=False,
        unique=True,
        verbose_name=_('Name')
    )

    class Meta:
        db_table = 'department'
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')


class Notice(ModelBase):
    content = models.TextField(
        db_column='tx_content',
        null=False,
        verbose_name=_('Content')
    )

    class Meta:
        db_table = 'notice'
        verbose_name = _('Notice')
        verbose_name_plural = _('Notices')


class User(ModelBase):
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=False,
        db_index=False,
        related_name='users',
        verbose_name=_('Department')
    )
    name = models.CharField(
        db_column='tx_name',
        max_length=64,
        null=False,
        unique=True,
        verbose_name=_('Name')
    )

    class Meta:
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        indexes = [
            models.Index(fields=['department'])
        ]

    def __str__(self):
        return self.name


class Chat(ModelBase):
    class Meta:
        db_table = 'chat'
        verbose_name = _('Chat')
        verbose_name_plural = _('Chats')


class ChatUser(ModelBase):
    user = models.ForeignKey(
        to='User',
        on_delete=models.DO_NOTHING,
        db_column='id_user',
        null=False,
        db_index=False,
        related_name='chat_users',
        verbose_name=_('User')
    )
    chat = models.ForeignKey(
        to='Chat',
        on_delete=models.DO_NOTHING,
        db_column='id_chat',
        null=False,
        db_index=False,
        related_name='chat_users',
        verbose_name=_('Chat')
    )

    class Meta:
        db_table = 'chat_user'
        verbose_name = _('Chat user')
        verbose_name_plural = _('Chat users')
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['chat'])
        ]


class ChatMessage(ModelBase):
    user = models.ForeignKey(
        to='User',
        on_delete=models.DO_NOTHING,
        db_column='id_user',
        null=False,
        db_index=False,
        related_name='chat_messages',
        verbose_name=_('User')
    )
    chat = models.ForeignKey(
        to='Chat',
        on_delete=models.DO_NOTHING,
        db_column='id_chat',
        null=False,
        db_index=False,
        related_name='chat_messages',
        verbose_name=_('Chat')
    )
    message = models.TextField(
        db_column='tx_message',
        null=False,
        verbose_name=_('Message')
    )

    class Meta:
        db_table = 'chat_message'
        verbose_name = _('Chat message')
        verbose_name_plural = _('Chat messages')
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['chat'])
        ]
