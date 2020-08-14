# pycriaenvio

Biblioteca python para consumo da API CriaEnvio. Permite realizar várias transações para
para gerênciar contatos, listas (grupos) e envio de mensagens. 

Para mais informações sobre a documentação consulte: 

https://novo.nitronews.com.br/integracao/documentacao-api 

# Recursos Disponíveis

- Contatos

- [x]  Criação
- [x]  Listar todos os contatos
- [x]  Consultar Contato por id
- [x]  Atualizar
- [x] Inscrever contato em uma ou mais lista

- Listas (Grupos)

- Envio


# Instalação

```bash
$ pip install pycriaenvio
```
ou

```bash
$ python setup.py install
```

# Modo de usar

## Listar Contatos

````python3
from criaenvio.contato import ContatoCriaEnvioAPI
from decouple import config

contato_cliente = ContatoCriaEnvioAPI(config('CHAVE_API'))

contatos = contato_cliente.listar()
````

## Obter Contato por id

````python3
from criaenvio.contato import ContatoCriaEnvioAPI
from decouple import config

contato_cliente = ContatoCriaEnvioAPI(config('CHAVE_API'))

contato = contato_cliente.obter_por_id('qLGoa')
````
Para visualizar os grupos que o usuário pertence, basta passar o parâmetro grupos como True:
````python3
contato = contato_cliente.obter_por_id('qLGoa', grupos=True)
````

## Criar Contato
````python3
from criaenvio.contato import ContatoCriaEnvioAPI
from decouple import config

contato_cliente = ContatoCriaEnvioAPI(config('CHAVE_API'))

nome = 'Guilherme Peixoto'
email = 'gpeixoto3@gmail.com'
sexo = 'M' # or 'F'
data_nascimento = '03/05/1994'

contato = contato_cliente.criar(nome, email, sexo, data_nascimento)
````

## Atualizar Contato
````python3
from criaenvio.contato import ContatoCriaEnvioAPI
from decouple import config

contato_cliente = ContatoCriaEnvioAPI(config('CHAVE_API'))

id = 'qLGoa'
nome = 'Guilherme Peixoto'
email = 'gpeixoto3@gmail.com'
sexo = 'M' # or 'F'
data_nascimento = '03/05/1994'

contato = contato_cliente.atualizar(id, nome, email, sexo, data_nascimento)
````

## Inscrever Contato em uma ou mais listas 
````python3
from criaenvio.contato import ContatoCriaEnvioAPI
from decouple import config

contato_cliente = ContatoCriaEnvioAPI(config('CHAVE_API'))

id_contato = 'qLGoa'
listas = ['Lljy', 'LljW']

# para inscrever em uma unica lista
lista = ['Lljy', ]

contato = contato_cliente.inscrever_em_lista(id_contato, listas)
````

## Contribua

Clone o projeto repositório:

```bash
$ git clone https://github.com/peixoto3/python-criaenvio
```

Certifique-se de que o [Pipenv](https://github.com/kennethreitz/pipenv) está instalado, caso contrário:

```bash
$ pip install pipenv
```

Instale as dependências:

```bash
$ pipenv install --dev
```

Para executar os testes:

```bash
$ pipenv run python -m unittest
```


## Dependências

- [Python 3.7+](https://www.python.org/downloads/release/python-374/)
- [Pipenv](https://github.com/kennethreitz/pipenv)
- [Requests](https://requests.readthedocs.io/pt_BR/latest/user/install.html#install)

# Licença

[MIT](http://en.wikipedia.org/wiki/MIT_License)
