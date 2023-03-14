from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer


class AccountListCreateView(generics.ListCreateAPIView):
    """
    A view class for the Account model that handles listing and creating accounts.

    This view class inherits from the ListCreateAPIView class provided by the
    Django REST framework and is responsible for handling HTTP GET and POST
    requests to retrieve a list of all accounts and to create a new account respectively.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view class for the Account model that handles retrieving, updating and deleting accounts.

    This view class inherits from the RetrieveUpdateDestroyAPIView class provided by
    the Django REST framework and is responsible for handling HTTP GET, PUT, PATCH,
    and DELETE requests to retrieve, update, partially update, and delete a single account
    respectively.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
