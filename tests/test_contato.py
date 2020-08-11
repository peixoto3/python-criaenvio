import unittest

from criaenvio.contato import ContatoCriaEnvioAPI


class TestContatoCliente(unittest.TestCase):

    def setUp(self) -> None:
        self.cliente_contato = ContatoCriaEnvioAPI('RzRyVE4ua2d3OVUuendxUGIuTFVyQmVwLkhpV2Zp')

    def test_recurso(self):
        recurso_esperado = 'contatos'

        self.assertEqual(recurso_esperado, self.cliente_contato.RECURSO)

    def test_obter_contato_por_id(self):
        contato_esperado = self.cliente_contato.obter_por_id('qLGoa')['data']['id']

        self.assertEqual(contato_esperado, 'qLGoa')
