from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Serializer allow complex data structures such as querysets and model instances to be converted to native Python datatypes thatn can easily be rendered to JSON or XML

# ModelSerializer is a shortcut that lets you automatically create a Serializer class with fields that correspond to your Model fields
# is just like a regular serializer, except it will automatically generate a set of fields for you based on your model 

# HyperlinkedModelSerializer is similar to the ModelSerializer, except that it will use hyperlinks to represent relationships, rather than primary keys

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')