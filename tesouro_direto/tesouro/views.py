from rest_framework import generics

from tesouro_direto.tesouro.models import Titulo
from tesouro_direto.tesouro.serializers import TituloSerializer


class TituloList(generics.ListCreateAPIView):

    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer


class TituloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer