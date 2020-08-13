from criaenvio.contato import ContatoCriaEnvioAPI
from criaenvio.lista import ListaCriaEnvioAPI
from decouple import config

CHAVE_API = config('CHAVE_API')

contato_cliente = ContatoCriaEnvioAPI(CHAVE_API)

# novo_contato = contato_cliente.criar('teste', 'gpeixoto3@gmail.com')

# novo_contato_id = novo_contato['id']

# contato_cliente.inscrever_em_lista(novo_contato_id, )

contatos = contato_cliente.listar()
print(contatos)

contato = contato_cliente.obter_por_id('qLGoa')
print(contato)

grupos_cliente = ListaCriaEnvioAPI(CHAVE_API)

grupos = grupos_cliente.listar()

print(grupos)

inscricao_lista = contato_cliente.inscrever_em_lista('qLGoa', 'LljW')

print(inscricao_lista)
