from django.db import models
from swampdragon.models import SelfPublishModel
from chat.serializers import ChatListSerializer, ChatItemSerializer


class ChatList(SelfPublishModel, models.Model):
    serializer_class = ChatListSerializer
    name = models.CharField(max_length=100)
    description = models.TextField()


class ChatItem(SelfPublishModel, models.Model):
    serializer_class = ChatItemSerializer
    chat_list = models.ForeignKey(ChatList)
    done = models.BooleanField(default=False)
    text = models.CharField(max_length=100)
