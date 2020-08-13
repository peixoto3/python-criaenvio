from abc import ABC
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

    def _obter_url(self, url: str = '') -> str:
        return f'{self.URL_API}/{self.RECURSO}/{url}?chave={self._chave_api}'

    def _requisicao_get(self, url: str) -> dict:
        return requests.get(url).json()

    def _requisicao_post(self, url: str, corpo_requisicao: dict = None) -> dict:
        return requests.post(url, data=corpo_requisicao).json()

    def _requisicao_put(self, url: str, corpo_requisicao: dict = None) -> dict:
        return requests.put(url, data=corpo_requisicao).json()

    def _requisicao_delete(self, url) -> dict:
        pass
