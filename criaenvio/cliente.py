from abc import ABC
from typing import Dict, Any
from urllib.parse import urlencode

import requests


class APIClienteCriaEnvio(ABC):
    """
    Classe abstrata que represente um cliente da API Criaenvio versão 1

    A autenticação é realizada através da inclusão do parâmetro “chave” na URL. Esta chave pode ser gerada no sistema,
    na seção "Chaves da API".

    Para requisições POST e PUT, os parâmetros não incluidos na URL devem ser codificados em JSON com um header
    "Content-Type: application/json".

    Requisições que retornam múltiplos itens serão paginadas com 30 itens por padrão. Você pode especificar as páginas
    através do parâmetro "page". Para alguns recursos você pode definir um tamanho de página, com um limite superior de
    100 itens, através do parâmetro "number". Essas requisições acompanham um objeto JSON chamado "pagination",
    com informações adicionais sobre a paginação.
    """

    URL_API = 'https://api.criaenvio.com/v1'
    RECURSO = None

    def __init__(self, chave_api: str):
        self._chave_api = chave_api

    def _obter_url(self, **kwargs) -> str:
        """

        A url da API pode conter um caminho/acao e/ou parametros (query string);
        Toda requisição envia uma query string na URL chave, que contem o valor da chave de autenticacao.

        Exemplo:
            https://api.criaenvio.com/v1/campos?chave=V2FASZTf208fhs98cwuTVZ4WHcuZkcwMWguDssY=

        exemplo com caminho id:
            https://api.criaenvio.com/v1/contatos/{id}

        exemplo com caminho id mais acao
            https://api.criaenvio.com/v1/contatos/{id}/ativar
            https://api.criaenvio.com/v1/contatos/{id}/desativar

        exemplo com caminho id mais parametros
            https://api.criaenvio.com/v1/contatos/{id}?{embeds}

        exemplo com caminho id mais acao mais parametros
            https://api.criaenvio.com/v1/contatos/{id}/inscrever?{embeds}

        Saiba mais em: https://novo.nitronews.com.br/integracao/documentacao-api
        """

        url_completa = f'{self.URL_API}/{self.RECURSO}'

        caminho = kwargs.get('caminho', '')
        parametros = kwargs.get('parametros', {})

        url_completa += caminho

        if not parametros:
            return f'{url_completa}?chave={self._chave_api}'

        parametros_url = urlencode(parametros)
        url_completa += f'?{parametros_url}&chave={self._chave_api}'

        return url_completa

    def _requisicao_get(self, url: str) -> Dict[Any, Any]:
        return requests.get(url).json()

    def _requisicao_post(self, url: str, corpo_requisicao: dict = None) -> Dict[Any, Any]:
        return requests.post(url, data=corpo_requisicao).json()

    def _requisicao_put(self, url: str, corpo_requisicao: dict = None) -> Dict[Any, Any]:
        return requests.put(url, data=corpo_requisicao).json()

    def _requisicao_delete(self, url) -> Dict[Any, Any]:
        return requests.delete(url).json()
