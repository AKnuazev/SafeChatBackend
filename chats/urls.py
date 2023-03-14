from django.urls import path
from .views import ChatListCreateView, ChatDetailView, \
    MessageListCreateView, MessageDetailView, SendMessage

urlpatterns = [
    path('chats/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='chat-retrieve-update-destroy'),
    path('chats/<int:chat_id>/send/', SendMessage.as_view(), name='send_message'),
]
