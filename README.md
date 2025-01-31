# API Blog

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Django](https://img.shields.io/badge/Django-4.x-green)

## Descrição

O **API Blog** é um projeto desenvolvido em Django para fornecer uma API RESTful que permite a criação, leitura, atualização e exclusão (CRUD) de postagens de blog. O objetivo deste projeto é facilitar a integração de um backend robusto com aplicações front-end ou serviços de terceiros.

## Funcionalidades

- CRUD de postagens de blog
- Endpoints organizados seguindo boas práticas REST
- Estrutura modular e escalável

## Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando:

- **Python 3.x**: Linguagem de programação principal do projeto.
- **Django 4.x**: Framework web utilizado para estruturar a API.
- **Django REST Framework (DRF)**: Extensão do Django para criação de APIs RESTful.
- **SQLite**: Banco de dados utilizado para armazenamento de informações.
- **Git e GitHub**: Para versionamento de código e colaboração.

## Habilidades Adquiridas

Durante o desenvolvimento deste projeto, adquiri e aprimorei diversas habilidades, incluindo:

- Criação e consumo de APIs RESTful com Django e DRF.
- Modelagem de banco de dados e utilização do ORM do Django.
- Boas práticas de versionamento de código e documentação.

## Requisitos

- Python 3.x instalado
- Pip e Virtualenv para gerenciamento de pacotes

## Instalação

Clone este repositório para sua máquina local:

```sh
git clone https://github.com/RafaSobral/APIblog.git
```

Entre no diretório do projeto:

```sh
cd APIblog
```

Crie um ambiente virtual e ative-o:

```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

Instale as dependências:

```sh
pip install -r requirements.txt
```

Realize as migrações do banco de dados:

```sh
python manage.py migrate
```

## Como Usar

Inicie o servidor de desenvolvimento:

```sh
python manage.py runserver
```

Agora a API estará disponível em `http://127.0.0.1:8000/`.

## Contribuição

Sinta-se à vontade para contribuir com melhorias e novas funcionalidades! Para isso:

1. Faça um fork do repositório
2. Crie uma branch com sua funcionalidade (`git checkout -b minha-feature`)
3. Commit suas alterações (`git commit -m 'Adicionando nova funcionalidade'`)
4. Envie para o repositório (`git push origin minha-feature`)
5. Abra um Pull Request

## Autor

Desenvolvido por [Rafael Sobral](https://github.com/RafaSobral).

