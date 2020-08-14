import unittest
from unittest.mock import Mock, patch

from decouple import config

from criaenvio.contato import ContatoCriaEnvioAPI


class TestContatoCliente(unittest.TestCase):

    # TODO
    # separar teste do metodo obter_url para uma classe de teste especifica

    def setUp(self) -> None:
        self.chave_api = config('CHAVE_API')

        self.cliente_contato = ContatoCriaEnvioAPI(self.chave_api)

    def test_criacao_cliente_contato_api(self):
        self.assertTrue(isinstance(self.cliente_contato, ContatoCriaEnvioAPI))

    def test_recurso(self):
        recurso_esperado = 'contatos'

        self.assertEqual(recurso_esperado, self.cliente_contato.RECURSO)

    def test_obter_url_com_caminho(self):
        caminho_url = '/4'
        url = self.cliente_contato._obter_url(caminho=caminho_url)
        url_esperada = f'https://api.criaenvio.com/v1/contatos/4?chave={self.chave_api}'

        self.assertEqual(url_esperada, url)

    def test_obter_url_com_parametro(self):
        parametros = {'embeds': 'grupos'}
        url = self.cliente_contato._obter_url(parametros=parametros)
        url_esperada = f'https://api.criaenvio.com/v1/contatos?embeds=grupos&chave={self.chave_api}'

        self.assertEqual(url_esperada, url)

    def test_obter_url_sem_parametros_e_sem_caminho(self):
        url_esperada = f'https://api.criaenvio.com/v1/contatos?chave={self.chave_api}'

        url = self.cliente_contato._obter_url()

        self.assertEqual(url_esperada, url)

    def test_obter_url_com_caminho_e_parametro(self):
        parametros = {'embeds': 'grupos'}
        caminho_url = '/4/inscrever'
        url = self.cliente_contato._obter_url(caminho=caminho_url, parametros=parametros)
        url_esperada = f'https://api.criaenvio.com/v1/contatos/4/inscrever?embeds=grupos&chave={self.chave_api}'

        self.assertEqual(url_esperada, url)

    @patch('requests.get')
    def test_obter_contato_por_id(self, mock_obter_contato_por_id):
        contato_esperado = {
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

        mock_obter_contato_por_id.return_value.json.return_value = contato_esperado

        contato = self.cliente_contato.obter_por_id('id_teste')

        self.assertEqual(contato_esperado, contato)

    @patch('requests.post')
    def test_criar_contato(self, mock_criar_contato):
        nome = 'Guilherme Peixoto'
        email = 'gpeixoto3@gmail.com'

        contato_esperado = {
            'data': {
                'id': 'qLGoa',
                'nome': 'Guilherme Peixoto',
                'email': 'gpeixoto3@gmail.com',
                'qualidade': '5',
                'ativo': True,
                'descadastrado': False,
                'sexo': '',
                'dataNascimento': '',
                'dataCadastro': '2020-08-14 00:05:00'
            },
            'embeds': [
                'grupos',
                'campos'
            ]
        }

        mock_criar_contato.return_value.json.return_value = contato_esperado

        contato = self.cliente_contato.criar(nome, email)

        self.assertEqual(contato_esperado, contato)

    @patch('requests.get')
    def test_obter_contato_por_id(self, mock_obter_contato_por_id):
        contato_esperado = {
            'data': {
                'id': 'qLGoa',
                'nome': 'Guilherme Peixoto',
                'email': 'gpeixoto3@gmail.com',
                'qualidade': '5',
                'ativo': True,
                'descadastrado': False,
                'sexo': None,
                'dataNascimento': None,
                'dataCadastro': '2020-08-14 00:05:00'
            },
            'embeds': [
                'grupos',
                'campos'
            ]
        }

        mock_obter_contato_por_id.return_value.json.return_value = contato_esperado

        contato = self.cliente_contato.obter_por_id('qLGoa')

        self.assertEqual(contato_esperado, contato)

    @patch('requests.get')
    def test_obter_lista_de_contatos(self, mock_obter_lista_de_contatos):
        lista_contatos_esperada = {
            'data': [
                {
                    'id': 'qLGoa',
                    'nome': 'Guilherme Peixoto',
                    'email': 'gpeixoto3@gmail.com',
                    'qualidade': '5',
                    'ativo': True,
                    'descadastrado': False,
                    'sexo': None,
                    'dataNascimento': None,
                    'dataCadastro': '2020-08-14 00:05:00'
                },
                {
                    'id': 'q-5nG',
                    'nome': 'Teste 1',
                    'email': 'teste@gmail.com',
                    'qualidade': '5',
                    'ativo': True,
                    'descadastrado': False,
                    'sexo': None,
                    'dataNascimento': None,
                    'dataCadastro': '2020-08-13 22:25:14.865734'
                },
                {
                    'id': 'q-5n5',
                    'nome': 'Teste 2',
                    'email': 'teste2@gmail.com',
                    'qualidade': '5',
                    'ativo': True,
                    'descadastrado': False,
                    'sexo': None,
                    'dataNascimento': None,
                    'dataCadastro': '2020-08-13 22:25:25.110743'
                }
            ],
            'embeds': [
                'grupos',
                'campos'
            ],
            'pagination': {
                'total': 3,
                'count': 3,
                'per_page': 30,
                'current_page': 1,
                'total_pages': 1,
                'links': []
            }
        }

        mock_obter_lista_de_contatos.return_value.json.return_value = lista_contatos_esperada

        contatos = self.cliente_contato.listar()

        self.assertEqual(lista_contatos_esperada, contatos)

    @patch('requests.post')
    def test_inscrever_em_lista(self, mock_inscrever_em_lista):
        retorno_insricao_lista_esperado = {
            "data": {
                "OK": "OK"
            }
        }

        mock_inscrever_em_lista.return_value.json.return_value = retorno_insricao_lista_esperado

        id_contato_para_inscricao = 'qLGoa'
        lista_para_inscricao = ['LljW', ]

        retorno = self.cliente_contato.inscrever_em_lista(id_contato_para_inscricao, lista_para_inscricao)

        self.assertEqual(retorno_insricao_lista_esperado, retorno)

    @patch('requests.post')
    def test_inscrever_em_varias_listas(self, mock_inscrever_em_varias_listas):
        retorno_insricao_lista_esperado = {
            "data": {
                "OK": "OK"
            }
        }

        mock_inscrever_em_varias_listas.return_value.json.return_value = retorno_insricao_lista_esperado

        id_contato_para_inscricao = 'qLGoa'
        listas_para_inscricao = ['LljW', 'Lljs', 'LljD', 'aljW']

        retorno = self.cliente_contato.inscrever_em_lista(id_contato_para_inscricao, listas_para_inscricao)

        self.assertEqual(retorno_insricao_lista_esperado, retorno)
