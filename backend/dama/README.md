# DAMA

# 👩‍💻 Colaboradores

- Felipe - [@github](https://github.com/)
- Giovana - [@github](https://github.com/)
- Leandro - [@github](https://github.com/)
- Luana - [@github](https://github.com/)
- Igor - [@github](https://github.com/)

# 🛠️ Tecnologias Utilizadas

- ![Django Rest Framework](https://img.shields.io/badge/Django%20Rest-Framework-green)
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue)
- ![Angular](https://img.shields.io/badge/Angular)
- ![TypeScript](https://img.shields.io/badge/TypeScript-cyan)
- ![Bootstrap](https://img.shields.io/badge/Bootstrap)

# 📃 Documentação

[Link para os documentos do projeto](doc/documentacao.md)

# 🔧 Instalação

# Guia de Instalação do Projeto DAMA

**Este guia fornece instruções detalhadas sobre como configurar e iniciar o ambiente de desenvolvimento para o backend do projeto DAMA.**


## **Configuração do Ambiente Virtual**

**Criando o Ambiente Virtual**

1. Abra o terminal e execute o seguinte comando para criar um ambiente virtual Python. Este ambiente isola as dependências do projeto.

`python -m venv env`

**Ativando o Ambiente Virtual**

2. Ative o ambiente virtual criado. A ativação varia conforme o sistema operacional:

**Linux/MacOS:**

`source ./env/bin/activate`

**Windows:**

`.\env\Scripts\activate`

**Instalação das Dependências do Backend**

3. Com o ambiente virtual ativado, instale as dependências necessárias para o backend executando:

`pip install -r requirements.txt`

**Configuração do Backend**

4. Navegue até o diretório do backend do projeto:

`cd backend/dama`

5. Inicie o servidor backend localmente:

`python3 manage.py runserver`

**O servidor backend agora deve estar rodando e acessível localmente.**

## **Popular banco de dados**

1. Abra uma nova janela ou aba do terminal e navegue até a pasta onde está o arquivo manage.py do projeto:

`cd backend/dama`
2. Crie um super usuário e verifique no django admin as tabelas criadas:

`python3 manage.py createsuperuser`

3. Utilize o comando onde vamos utilizar as seeds:

`python3 manage.py seed-ong`
ou
`python3 manage.py seed-usuario`

**Outras formas de visualizar o backend**

1. Abra em seu navegador, após iniciar a aplicação localmente, no seguinte link:

`localhost:8000/api/test`

*** Este link abrirá o Swagger, onde é possível testar os endpoints e visualizar as respostas das requisições de forma clara e interativa. ***

