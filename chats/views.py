from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer


class ChatListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating chats.
    """
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Add the requesting user as a member of the new chat.
        serializer.save(members=[self.request.user])


class ChatDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a single chat.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]


class MessageListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating messages in a chat.
    """
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return messages for the requested chat.
        chat_id = self.kwargs.get('chat_id')
        return Message.objects.filter(chat__id=chat_id)

    def perform_create(self, serializer):
        # Set the sender of the new message to the requesting user.
        serializer.save(sender=self.request.user)


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a single message in a chat.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class SendMessage(APIView):
    """
    View to handle sending messages.
    """

    def post(self, request, chat_id):
        """
        Send a message to the specified chat.

        Args:
            chat_id (int): The ID of the chat to send the message to.

        Returns:
            A serialized Message object with status code 201 if the message was sent successfully,
            or a serialized error response with status code 400 if the request data was invalid.
        """
        # Get the chat object
        try:
            chat = Chat.objects.get(pk=chat_id)
        except Chat.DoesNotExist:
            return Response(
                {"detail": f"Chat with id={chat_id} does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Deserialize the message data from the request body
        serializer = MessageSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Save the message and add it to the chat
        message = serializer.save(sender=request.user, chat=chat)

        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)
