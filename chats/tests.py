from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Chat, Message

User = get_user_model()


class ChatModelTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='testuser1',
            email='testuser1@example.com',
            password='testpass1'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='testuser2@example.com',
            password='testpass2'
        )

    def test_chat_str_method_with_name(self):
        """
        Test Chat __str__ method with name.
        """
        chat = Chat.objects.create(name='Test Chat')
        chat.members.set([self.user1, self.user2])
        self.assertEqual(str(chat), 'Test Chat')

    def test_chat_str_method_without_name(self):
        """
        Test Chat __str__ method without name.
        """
        chat = Chat.objects.create()
        chat.members.set([self.user1, self.user2])
        self.assertEqual(str(chat), f'{self.user1}, {self.user2}')

    def test_chat_add_member(self):
        """
        Test adding a member to a chat.
        """
        chat = Chat.objects.create()
        chat.members.set([self.user1])
        chat.members.add(self.user2)
        self.assertEqual(chat.members.count(), 2)

    def test_chat_remove_member(self):
        """
        Test removing a member from a chat.
        """
        chat = Chat.objects.create()
        chat.members.set([self.user1, self.user2])
        chat.members.remove(self.user2)
        self.assertEqual(chat.members.count(), 1)
        self.assertEqual(chat.members.first(), self.user1)

    def test_chat_clear_members(self):
        """
        Test clearing all members from a chat.
        """
        chat = Chat.objects.create()
        chat.members.set([self.user1, self.user2])
        chat.members.clear()
        self.assertEqual(chat.members.count(), 0)


class MessageModelTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='testuser1',
            email='testuser1@example.com',
            password='testpass1'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='testuser2@example.com',
            password='testpass2'
        )
        self.chat = Chat.objects.create()
        self.chat.members.set([self.user1, self.user2])

    def test_message_str_method_short_text(self):
        """
        Test Message __str__ method with short text.
        """
        message = Message.objects.create(chat=self.chat, sender=self.user1, text='Test message')
        self.assertEqual(str(message), f'{self.user1}: Test message')

    def test_message_str_method_long_text(self):
        """
        Test Message __str__ method with long text.
        """
        message = Message.objects.create(chat=self.chat, sender=self.user1, text='a' * 50)
        self.assertEqual(str(message), f'{self.user1}: {"a" * 20}...')

    def test_message_created_at(self):
        """
        Test Message created_at field.
        """
        message = Message.objects.create(chat=self.chat, sender=self.user1, text='Test message')
        self.assertIsNotNone(message.created_at)

    def test_message_sender(self):
        """
        Test Message sender field.
        """
        message = Message.objects.create(chat=self.chat, sender=self.user1, text='Test message')
        self.assertEqual(message.sender, self.user1)

    def test_message(self):
        """
        Test creating and retrieving messages
        """
        chat = Chat.objects.create(name="Test Chat")
        sender = User.objects.create_user(username="testuser", email="testuser@example.com", password="testpass")
        message_text = "Hello, world!"
        message = Message.objects.create(chat=chat, sender=sender, text=message_text)

        # Test message creation
        self.assertIsInstance(message, Message)
        self.assertEqual(message.chat, chat)
        self.assertEqual(message.sender, sender)
        self.assertEqual(message.text, message_text)

        # Test message retrieval
        messages = Message.objects.filter(chat=chat)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0], message)

