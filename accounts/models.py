from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    """
    Manager for the custom user model `Account`.
    """

    def create_user(self, email: str, password: str = None, **kwargs) -> 'Account':
        """
        Creates and saves a user with the given email and password.

        Required Args:
            email (str): Email of the user.

        Optional Args:
            password (str): Password for the user. If not provided, a random password will be generated.
            **kwargs: Additional fields to set on the user.

        Returns:
            Account: Newly created user object.
        """
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **kwargs) -> 'Account':
        """
        Creates and saves a superuser with the given email and password.

        Required Args:
            email (str): Email of the superuser.
            password (str): Password for the superuser.

        Optional Args:
            **kwargs: Additional fields to set on the user.

        Returns:
            Account: Newly created superuser object.
        """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(email, password, **kwargs)


class Account(AbstractBaseUser):
    """
    Custom user model for SafeChatBackend app.
    """
    email = models.EmailField(unique=True, verbose_name="Email address")
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name="Last name")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_staff = models.BooleanField(default=False, verbose_name="Staff status")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date joined")

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self) -> str:
        """
        Returns a string representation of the user.
        """
        return self.email

    def get_full_name(self) -> str:
        """
        Returns the user's full name.
        """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self) -> str:
        """
        Returns the user's first name.
        """
        return self.first_name
