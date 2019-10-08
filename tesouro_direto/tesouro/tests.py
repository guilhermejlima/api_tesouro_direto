from tesouro_direto.tesouro.models import Titulo
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tesouro_direto.tesouro.models import Titulo


class TestApi(APITestCase):
    def setUp(self):
        self.nome = "Tesouro IPCA+ 2024"
        self.vencimento = "15/05/2035"
        self.taxa_rendimento = "IPCA + 2,61"
        self.valor_minimo = "R$57,20"
        self.preco = "R$2.860,49"

        self.titulo = Titulo.objects.create(nome= self.nome, vencimento= self.vencimento, taxa_rendimento= self.taxa_rendimento, valor_minimo= self.valor_minimo, preco= self.preco)

    def test_api_response(self):
        response = self.client.get('/titulos/', {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_response(self):
        response = self.client.get('/error/', {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


