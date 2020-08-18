from typing import Dict, List

from requests import Response

from criaenvio.cliente import APIClienteCriaEnvio


class ContatoCriaEnvioAPI(APIClienteCriaEnvio):
    """
        Classe Responsavel pelos endpoints do recurso de contatos da API
    """

    RECURSO = 'contatos'

    def criar(self, nome: str, email: str, sexo: str = None, data_de_nascimento: str = None):
        """
        API que cadastra um novo contato

        Parametros:
            nome: nome do contato - obrigatorio
            email: email do contato - obrigatorio
            sexo: gênero do contato, Masculino (M) e Feminino (F)
            data_de_nascimento: data de nascimento no formato brasileiro de data (DD/MM/YYYY)
        """

        corpo_requisicao = {
            "nome": nome,
            "email": email,
            "sexo": sexo,
            "data_de_nascimento": data_de_nascimento
        }

        return self._requisicao_post(self._obter_url(), corpo_requisicao)

    def listar(self, numero_pagina: str = '', tamanho_pagina: str = ''):
        """
         API retorna uma lista de Contatos

         Parametros:
            numero_pagina: numero da pagina caso a consulta for paginada
            tamanho_pagina: quantidade de registro por pagina
        """

        parametros = {
            'page': numero_pagina,
            'number': tamanho_pagina,
        }

        return self._requisicao_get(self._obter_url(parametros=parametros))

    def obter_por_id(self, id: str, grupos=False):
        """
        API visualiza um unico contato por id como tambem os grupos do contato se passado como True.
        """

        caminho_url = f'/{id}'

        parametros = {
            'embeds': 'grupos' if grupos else ''
        }

        return self._requisicao_get(self._obter_url(caminho=caminho_url, parametros=parametros))

    def atualizar(self,
                  id: str,
                  nome: str,
                  email: str,
                  sexo: str = None,
                  data_de_nascimento: str = None
                  ) -> Dict[str, str]:
        caminho_url = f'/{id}'

        corpo_requisicao = {
            "nome": nome,
            "email": email,
            "sexo": sexo,
            "data_de_nascimento": data_de_nascimento
        }

        return self._requisicao_put(self._obter_url(caminho=caminho_url), corpo_requisicao)

    def inscrever_em_lista(self, id: str, listas: List[str]):
        """
        Inscreve o contato em uma ou mais listas.

        Parametros:
            id: Id do contato
            listas: array de id de listas.
        """
        caminho_url = f'/{id}/inscrever'

        corpo_requisicao = {
            "idGrupos": ','.join(listas)  # transformando em string sparada por virgula por demanda da API.
        }

        return self._requisicao_post(self._obter_url(caminho=caminho_url), corpo_requisicao)

    def desincrever_em_lista(self):
        pass

    def ativar(self):
        pass

    def desativar(self):
        pass

    def atualizar_campos_personalizados(self):
        pass
