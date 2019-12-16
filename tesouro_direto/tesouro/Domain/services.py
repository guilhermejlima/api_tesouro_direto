from rest_framework import generics

from tesouro_direto.tesouro.Infraestructure.repository.Entities import Titulo
from tesouro_direto.tesouro.Domain.serializers import TituloSerializer


class TituloList(generics.ListCreateAPIView):

    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer


class TituloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer