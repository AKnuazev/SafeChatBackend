from rest_framework import serializers
from .models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    """
    Serializer for Chat model.
    """
    class Meta:
        model = Chat
        fields = ('id', 'name', 'members')


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message model.
    """
    class Meta:
        model = Message
        fields = ('id', 'chat', 'sender', 'text', 'created_at')
