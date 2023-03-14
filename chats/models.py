from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Chat(models.Model):
    """
    Chat model that represents a conversation between users.
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    members = models.ManyToManyField(User, related_name='chats', blank=True)

    def __str__(self):
        return self.name or ', '.join(str(user) for user in self.members.all())


class Message(models.Model):
    """
    Message model that represents a message sent in a chat.
    """
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.text[:20]}{"..." if len(self.text) > 20 else ""}'
