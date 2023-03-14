import random
import string
import sys
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from chats.models import Chat, Message
import os
import django

# sys.path.append(os.path.join(os.path.dirname(sys.path[0])))  # , '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

User = get_user_model()

# Create 10 users
for i in range(10):
    username = f'user{i+1}'
    email = f'{username}@example.com'
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    User.objects.create_user(username=username, email=email, password=password)

# Get all users
users = User.objects.all()

# Create 5 chats
for i in range(5):
    name = f'Chat {i+1}'
    chat = Chat.objects.create(name=name)
    chat.users.set(users)

# Get all chats
chats = Chat.objects.all()

# Create 50 messages in each chat
for chat in chats:
    for i in range(50):
        sender = random.choice(chat.users.all())
        recipient = chat.users.exclude(id=sender.id).first()
        content = f'Message {i+1} in {chat.name}'
        timestamp = timezone.now() - timedelta(days=random.randint(1, 30))
        Message.objects.create(chat=chat, sender=sender, recipient=recipient, content=content, timestamp=timestamp)
