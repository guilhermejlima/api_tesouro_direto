from django.contrib.auth.models import User, Group
from rest_framework import serializers

from tesouro_direto.tesouro.models import Titulo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields = '__all__'
