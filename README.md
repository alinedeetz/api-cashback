 [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


 # Python Wallet - Cashback

Essa é uma API feita utilizando Python e Django REST Framework. 

Sua principal funcionalidade envolve receber dados de um cliente e sua respectiva compra, calcular o valor de cashback que esse cliente deve receber e enviar essa informação para uma API externa - que irá processar o pagamento do valor do benefício. 

Para utilizá-la, é necessário que o usuário esteja autenticado.


### Instalando os requisitos 

>$ pip install -r requirements.txt

### Criando um usuário

>$ python manage.py createsuperuser

### Realizando as migrações

>$ python manage.py makemigrations
>$ python manage.py migrate 


### Rodando a aplicação

>$ python manage.py runserver



