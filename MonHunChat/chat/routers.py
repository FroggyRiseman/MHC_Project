from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from chat.models import ChatList, ChatItem
from chat.serializers import ChatListSerializer, ChatItemSerializer


class ChatListRouter(ModelRouter):
    route_name = 'chat-list'
    serializer_class = ChatListSerializer
    model = ChatList

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


class ChatItemRouter(ModelRouter):
    route_name = 'chat-item'
    serializer_class = ChatItemSerializer
    model = ChatItem

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.filter(chat_list__id=kwargs['list_id'])


route_handler.register(ChatListRouter)
route_handler.register(ChatItemRouter)
