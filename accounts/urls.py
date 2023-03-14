from django.urls import path
from .views import AccountListCreateView, AccountDetailView


urlpatterns = [
    path('', AccountListCreateView.as_view(), name='account-list-create'),
    # The above URL pattern maps to the AccountListCreateView and is named 'account-list-create'.
    # It handles HTTP GET and POST requests to retrieve a list of all accounts and to create a new account respectively.
    path('<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    # The above URL pattern maps to the AccountDetailView and takes an integer argument 'pk'
    # representing the primary key of the account and is named 'account-detail'.
    # It handles HTTP GET, PUT, PATCH, and DELETE requests to retrieve, update, partially update,
    # and delete a single account respectively.
]