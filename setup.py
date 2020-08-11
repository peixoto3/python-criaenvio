from setuptools import setup

setup(name='py-criaenvio',
      version='0.1',
      description='Integração da API Criaenvio com python',
      url='https://github.com/peixoto3/python-criaenvio',
      author='Guilherme Peixoto',
      author_email='gpeixoto3@gmail.com',
      license='MIT',
      packages=['criaenvio'],
      install_requires=["requests", ],
      zip_safe=False)
