from criaenvio.contato import ContatoCriaEnvioAPI
from criaenvio.lista import ListaCriaEnvioAPI
from decouple import config

CHAVE_API = config('CHAVE_API')

contato_cliente = ContatoCriaEnvioAPI(CHAVE_API)

print(contato_cliente.listar())

# grupos_cliente = ListaCriaEnvioAPI(CHAVE_API)

'''
grupos = grupos_cliente.listar()
print(grupos)
'''

# contato = contato_cliente.obter_por_id('qLGoa')
# print(contato)

# contato = contato_cliente.obter_por_id('qLGoa', grupos=True)
# print(contato)

# teste_contato = contato_cliente.criar('Guilherme Peixoto', 'gpeixoto3@gmail.com')
# print(teste_contato)

'''
contatos = contato_cliente.listar()
print(contatos)


contato = contato_cliente.obter_por_id('qLGoa')
print(contato)


print(grupos)

inscricao_lista = contato_cliente.inscrever_em_lista('qLGoa', 'LljW')

print(inscricao_lista)
'''
