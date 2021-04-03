# SETUP

## Instalação do Python

O primeiro passo é a instalação do [Python](https://www.python.org/downloads/)

Além disso, é necessário instalar o pacote `virtualenv` pelo `pip`. Após a instalação do Python, digite em um terminal:

    $ pip install virtualenv

## Criação do Ambiente Virtual

Para criar o ambiente virtual, digite o seguinte comando:

    $ virtualenv env

Devemos também ativá-lo.

No Linux e Mac:

    $ source env/bin/activate

No Windows:

    ./env/Script/activate.bat

Agora podemos instalar todos os pacotes necessários:

    $ pip install -r requirements.txt


