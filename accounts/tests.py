from django.test import TestCase
from accounts.models import Account


class AccountModelTests(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_create_user(self):
        """
        Test creating a new user
        """
        user = Account.objects.create_user(
            username='newuser',
            email='newuser@example.com',
            password='newpass'
        )
        self.assertIsInstance(user, Account)
        self.assertEqual(user.username, 'newuser')
        self.assertEqual(user.email, 'newuser@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_no_username(self):
        """
        Test creating a new user without username should raise ValueError.
        """
        with self.assertRaises(Exception):
            user = Account.objects.create_user(
                email='newuser@example.com',
                password='newpass'
            )

    def test_create_user_no_email(self):
        """
        Test creating a new user without email should raise ValueError.
        """
        with self.assertRaises(Exception):
            user = Account.objects.create_user(
                username='newuser',
                password='newpass'
            )

    def test_create_user_no_password(self):
        """
        Test creating a new user without password should raise ValueError.
        """
        with self.assertRaises(Exception):
            user = Account.objects.create_user(
                username='newuser',
                email='newuser@example.com',
            )

    def test_create_superuser(self):
        """
        Test creating a new superuser
        """
        user = Account.objects.create_superuser(
            username='newsuperuser',
            email='newsuperuser@example.com',
            password='newsuperpass'
        )
        self.assertIsInstance(user, Account)
        self.assertEqual(user.email, 'newsuperuser@example.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_username_max_length(self):
        """
        Test username max length
        """
        max_length = Account._meta.get_field('username').max_length
        self.assertEqual(max_length, 30)

    def test_string_representation(self):
        """
        Test string representation
        """
        self.assertEqual(str(self.user), self.user.email)

    def test_email_is_unique(self):
        """
        Test email is unique
        """
        with self.assertRaises(Exception):
            user = Account.objects.create_user(
                username='testuser2',
                email='testuser@example.com',
                password='testpass2'
            )

    def test_normalize_email(self):
        """
        Test email normalization
        """
        user = Account.objects.create_user(
            username='testuser3',
            email='testuser3@EXAMPLE.com',
            password='testpass3'
        )
        self.assertEqual(user.email, 'testuser3@example.com')

    def test_create_superuser_no_password(self):
        """
        Test creating a new superuser without password should raise ValueError.
        """
        with self.assertRaises(Exception):
            user = Account.objects.create_superuser(
                email='newsuperuser@example.com'
            )

    def test_create_superuser_no_email(self):
        """
        Test creating a new superuser without email should raise ValueError.
        """
        with self.assertRaises(Exception):
            user = Account.objects.create_superuser(
                password='newsuperpass'
            )

    def test_create_superuser_no_username(self):
        """
        Test creating a new superuser without username should raise ValueError.
        """
        with self.assertRaises(ValueError):
            user = Account.objects.create_superuser(
                email='newsuperuser@example.com',
                password='newsuperpass',
                username=''
            )
