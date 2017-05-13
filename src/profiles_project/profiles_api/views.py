from django.shortcuts import render

# used for viewsets
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retruns a list of API View features."""

        an_apiview = [
        'Uses HTTP methods as function(get, post, patch, put, delete)',
        'It is similar to traditional Django view',
        'Gives you the most control over your logic',
        'its mapped manually to URLs', ]

        return Response({'message':'hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello %s" % name
            # message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""
        #pk is primary key

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handles patching an object-only updates fields provided in the request"""
        #pk is primary key

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Handles deleting an object """
        #pk is primary key

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Creating a new object in the system"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello %s" % name
            # message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""
        #pk is primary key

        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object by its ID."""
        #pk is primary key

        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles Partial Updating an object-only updates fields provided in the request"""
        #pk is primary key

        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles desrtroying / deleting an object """
        #pk is primary key

        return Response({'method': 'DELETE'})
