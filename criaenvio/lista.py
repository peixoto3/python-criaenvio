from criaenvio.cliente import APIClienteCriaEnvio


class ListaCriaEnvioAPI(APIClienteCriaEnvio):
    RECURSO = 'grupos'

    def listar(self):
        return self._requisicao_get(self._montar_url())
