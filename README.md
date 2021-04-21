<div align="center">
  <a href="https://www.ceeita.com/"><img src="./front/public/logos/logo_red.svg" alt="CEE" width="200"></a>
</div>

<h1 align=center>Website CEE</h1>

## Sobre o projeto
---

O projeto mira a criação de um site com base de dados interna acessível a alunos do Instituto Tecnológico de Aeronáutica, e a automatização de uma série de processos, como, por exemplo, a publicação de uma vaga.

### Tecnologias utilizadas

- Django
- React
- Next.js

## Instalação
---

### Prerequisitos

- node, npm
- python

### Setup

1. Veja as instruções para o setup do [Back](back/README.md) e do [Front](front/cee/README.md).

2. Precisamos agora executar o back e front em paralelo. Em uma linha de comando, digite:

        $ python back/manage.py runserver
        $ cd front; npm run dev

3. Basta agora acessar http://localhost:3000 para verificar que o site está funcionando corretamente.
