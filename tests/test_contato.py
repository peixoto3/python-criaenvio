import unittest
from unittest.mock import Mock, patch

from decouple import config
from criaenvio.contato import ContatoCriaEnvioAPI


class TestContatoCliente(unittest.TestCase):

    def setUp(self) -> None:
        self.chave_api = config('CHAVE_API')

        self.cliente_contato = ContatoCriaEnvioAPI(self.chave_api)

    def test_criacao_cliente_contato_api(self):
        self.assertTrue(isinstance(self.cliente_contato, ContatoCriaEnvioAPI))

    def test_recurso(self):
        recurso_esperado = 'contatos'

        self.assertEqual(recurso_esperado, self.cliente_contato.RECURSO)

    def test_obter_url(self):
        url = self.cliente_contato._obter_url('?id=4')

        url_esperada = f'https://api.criaenvio.com/v1/contatos/?id=4?chave={self.chave_api}'

        self.assertEqual(url_esperada, url)

    @patch('requests.get')
    def test_obter_contato_por_id(self, mock_obter_contato_por_id):
        contato = {
            'data': {
                'id': 'aBGoa',
                'nome': 'Guilherme Peixoto',
                'email': 'gpeixoto3@gmail.com',
                'qualidade': '5',
                'ativo': True,
                'descadastrado': False,
                'sexo': 'm',
                'dataNascimento': '1994-05-03',
                'dataCadastro': '2020-08-10 18:58:16.133884'
            },
            'embeds': [
                'grupos',
                'campos'
            ]
        }

        mock_obter_contato_por_id.return_value.json.return_value = contato

        contato_esperado = self.cliente_contato.obter_por_id('id_teste')

        self.assertEqual(contato_esperado, contato)

    @patch('requests.get')
    def test_obter_lista_de_contatos(self, mock_obter_lista_de_contatos):
        pass
