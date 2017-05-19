from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView."""

    name = serializers.CharField(max_length=50)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers for our User Profile object."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password':{ 'write_only': True } }

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name'],
        )
        user.set_password(validated_data['password'])

        user.save()

        return user