from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics

from tesouro_direto.tesouro.models import Titulo
from tesouro_direto.tesouro.serializers import UserSerializer, GroupSerializer, TituloSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TituloViewSet(generics.ListCreateAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer