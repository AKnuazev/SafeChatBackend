from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    """
    A serializer class for the Account model.

    This serializer class is responsible for serializing and deserializing the
    Account model instances to and from JSON format.
    """
    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']
        # The `id` and `created_at` fields are read-only fields and should
        # not be allowed to be modified by the user.
