# Defesa e Apoio às Mulheres Agredidas - DAMA 

<img src="https://imgur.com/fktwWmk.png" width="600" height="100%" />

O projeto DAMA (Defesa e Apoio às Mulheres Agredidas) é uma ferramenta digital dedicada ao apoio, orientação e defesa das mulheres vítimas de qualquer tipo de violência. O site oferece recursos educacionais, visando fornecer suporte seguro para as usuárias.

## Frontend

### Pré-requisitos

Essas instruções ajudarão você a configurar o projeto DAMA na sua máquina local para fins de desenvolvimento e testes.

Para rodar este projeto, você precisará:

1. **Node.js** e **npm**: o Node.js é o ambiente de execução, já o npm é o gerenciador de pacotes do Node. Verifique a instalação com os seguintes comandos:
```
node -v
npm -v
```
Caso não tenha instalado, baixe a versão mais recente. 

2. **Angular CLI**: utilize o comando abaixo caso ainda não tenha instalado. 
```
npm install -g @angular/cli
```

3. **Git**: para clonar o projeto do repositório. 

### Execução do projeto:

Após a instalação dos pré-requisitos, siga os passos abaixo para executar o projeto. 

1. Clone o repositório do projeto DAMA:
```
git clone https://github.com/placidoneto/tads-dama-trainning.git
```
2. Acesse o repositório do projeto:
```
cd dama 
```
3. Instale as dependencias do projeto utilizando o npm:
```
npm install
```
4. Inicie o servidor para executar localmente com o comando abaixo:
```
ng serve 
```
5. O servidor de desenvolvimento estará disponível em: http://localhost:4200.

## Backend

### Pré-requisitos: 

Essas instruções fornecem instruções detalhadas sobre como configurar e iniciar o ambiente de desenvolvimento para o backend do projeto DAMA.


### Para configuração do ambiente virtual: 

1. Crie o ambiente virtual
```
python -m venv env 
```
Esse comando cria um ambiente virtual que isola as dependências do projeto.

2. Ative o ambiente virtual
   
Linux/MacOS:
```
source ./env/bin/activate
```
Windows:
```
.\env\Scripts\activate
```

3. Instale as dependências
Instale as dependências necessárias para o backend executando o seguinte comando:
```
pip install -r requirements.txt
```

4. Acesse o repositório do projeto:
```
cd dama 
```

5. Inicie o servidor backend localmente:
```
python3 manage.py runserver
```

### Populando o banco de dados:

1. Abra uma nova janela ou aba do terminal e navegue até a pasta onde está o arquivo manage.py do projeto
2. Crie um super usuário e verifique no django admin as tabelas criadas:
```
python3 manage.py createsuperuser
```
3. Utilize o comando onde vamos utilizar as seeds:
```
python3 manage.py seed-ong
ou
python3 manage.py seed-usuario
```

### Outras formas de visualizar o backend:

1. Abra em seu navegador, após iniciar a aplicação localmente, no seguinte link:
```
localhost:8000/api/test
```
Este link abrirá o Swagger, onde é possível testar os endpoints e visualizar as respostas das requisições de forma clara e interativa. 
