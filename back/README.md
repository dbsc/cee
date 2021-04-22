# Setup do Backend

## Instalação do Python

O primeiro passo é a instalação do [Python](https://www.python.org/downloads/)

Além disso, é necessário instalar o pacote `virtualenv` pelo `pip`. Após a instalação do Python, digite em um terminal:

    $ pip install virtualenv

## Criação do Ambiente Virtual

Para criar o ambiente virtual, digite o seguinte comando:

    $ virtualenv env

Devemos também ativá-lo.

    $ source env/bin/activate

Agora podemos instalar todos os pacotes necessários:

    $ pip install -r requirements.txt

Basta agora fazer a configuração da base de dados e executar o server.

    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
