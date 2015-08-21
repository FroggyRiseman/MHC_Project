from swampdragon.serializers.model_serializer import ModelSerializer

class ChatListSerializer(ModelSerializer):
    class Meta:
        model = 'chat.ChatList'
        publish_fields = ('name', 'description')


class ChatItemSerializer(ModelSerializer):
    class Meta:
        model = 'chat.ChatItem'
        publish_fields = ('done', 'text')
        update_fields = ('done',)
