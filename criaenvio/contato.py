from requests import Response

from criaenvio.cliente import APIClienteCriaEnvio


class ContatoCriaEnvioAPI(APIClienteCriaEnvio):
    """
        Classe Responsavel pelos endpoints do recurso de contatos da API
    """

    RECURSO = 'contatos'

    def criar(self, nome, email, sexo=None, data_de_nascimento=None) -> dict:
        """
        API que cadastra um novo contato

        Parametros:
            nome: nome do contato - obrigatorio
            email: email do contato - obrigatorio
            sexo: gênero do contato, Masculino (M) e Feminino (F)
            data_de_nascimento: data de nascimento no formato brasileiro de data (DD/MM/YYYY)

        Retorno:
            HttpResponse da biblioteca requests

        Exemplo:
            /contatos/
        """

        corpo_requisicao = {
            "nome": nome,
            "email": email,
            "sexo": sexo,
            "data_de_nascimento": data_de_nascimento
        }

        return self._requisicao_post(self._obter_url(), corpo_requisicao)

    def listar(self) -> dict:
        """
             API retorna uma lista de Contatos

             Exemplo:
                /contatos/
        """

        return self._requisicao_get(self._obter_url())

    def obter_por_id(self, id):
        """
            API visualiza um unico contato por id

            Exemplo:
                /contatos/{id}?{embeds}
        """

        return self._requisicao_get(self._obter_url(url=id))

    def atualizar(self, id, nome, email, sexo=None, data_de_nascimento=None) -> dict:
        corpo_requisicao = {
            "nome": nome,
            "email": email,
            "sexo": sexo,
            "data_de_nascimento": data_de_nascimento
        }

        return self._requisicao_put(self._obter_url(url=id), corpo_requisicao)

    def inscrever_em_lista(self, id, listas):
        # TODO
        # Receber uma lista de string e separar por virgulas para atender a demanda da API

        """
        Inscreve o contato em uma ou mais listas.

        Parametros:
            id: Id do contato
            listas: Lista de id separado por virgula


        Exemplo:
            /contatos/{id}/inscrever
        """

        corpo_requisicao = {
            "idGrupos": listas
        }

        return self._requisicao_post(self._obter_url(url=f'{id}/inscrever'), corpo_requisicao)
