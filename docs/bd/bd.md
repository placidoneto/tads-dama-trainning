# Modelo de Dados

## Diagrama ER

<img src="https://imgur.com/dK4NCFY.png" width="600" height="100%" />

## Modelo Relacional

<img src="https://imgur.com/QpFkOqc.png" width="600" height="100%" />

## Dicionário de Dados

--- 
*Tabela* : Usuário Anônimo

Descrição : Armazena as informações dos usuários anônimos						

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| usuario | Instância de django.User | django.contrib.auth.models.User |  | &#9744;  | &#9745; | &#9744; | &#9745; | &#9744; |   |   | 
| nome_login | nome de login do usuário | TEXT | 100  | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| senha | senha de acesso do usuário | VARCHAR | 20 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 

*Tabela* : Usuário Profissional								

Descrição : Armazena as informações dos usuários profissionais									

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| usuario | Instância de django.User | django.contrib.auth.models.User |  | &#9744;  | &#9745; | &#9744; | &#9745; | &#9744; |   |   | 
| nome_login | nome de login do usuário | TEXT | 100  | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| senha | senha de acesso do usuário | VARCHAR | 20 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| telefone | telefone para contato do usuário | INTEGER | 11 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| email | email para contato | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| nome_completo | nome completo para verificações profissionais | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| cadastro_crp | forma para confirmar o profissional | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9745; | &#9744; |   |   | 

*Tabela* : Usuário ONG									

Descrição : Armazena as informações dos usuários ONGs									


| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| usuario | Instância de django.User | django.contrib.auth.models.User |  | &#9744;  | &#9745; | &#9744; | &#9745; | &#9744; |   |   | 
| nome_login | nome de login do usuário | CHAR | 100  | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| senha | senha de acesso do usuário | VARCHAR | 20 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| telefone | telefone para contato do usuário | INTEGER | 11 | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| razão_social | forma de confirmação do tipo ONG | TEXT |  | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| email | email para contato | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 

--- 
*Tabela* : Denúncia

Descrição : Armazena as informações das denuncias

Observações :

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| descricao_denuncia | Texto da denuncia | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| tipo_local | local onde ocorreu | CHAR | 30  | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| tipo_vitima | tipo da vítima | CHAR | 30  | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| relacao_autor | relacao da vitima com o autor | TEXT | 30  | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| zona_cidade | zona da cidade onde ocorreu | CHAR | 30  | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| idade_vitima | idade da vitima | INTEGER |   | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| data_denuncia | data de quando ocorrreu | DATE |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| denuncia_id | identificação da denuncia | INTEGER |   | &#9744;  | &#9745; | &#9744; | &#9744; | &#9744; |   |   | 


--- 
*Tabela* : Relato

Descrição : Armazena as informações dos relatos

Observações : Esta tabela utilizara uma chave estrangeira da tabela Usuário

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| texto_relato | Texto descrito no relato | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| relato_id | identificação do relato | INTEGER |   | &#9744;  | &#9745; | &#9744; | &#9744; | &#9744; |   |   | 
| usuario_id | identificação do usuario | INTEGER |   | &#9744;  | &#9744; | &#9745; | &#9744; | &#9744; |   |   | 
| data_relato | data de publicação do relato | DATE |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 

--- 
*Tabela* : Material

Descrição : Armazena os materiais didaticos do site

Observações : Esta tabela utiliza a a chave estrangeira da tabela usuario.

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| conteúdo | Conteudo do material publicado | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| arquivo_anexado | arquivos que fazem referencia ao material postado | VARCHAR | 255  | &#9745;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| usuario_id | identificação do usuario que fez a publicação | INTEGER |   | &#9744;  | &#9744; | &#9745; | &#9744; | &#9744; |   |   | 
| material_id | identificação do material | INTEGER |   | &#9744;  | &#9745; | &#9744; | &#9744; | &#9744; |   |   | 
| data_material | Data do momento que foi publicado o material | DATE |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 

--- 
*Tabela* : Comentário

Descrição : Armazena os comentários em relatos

Observações : Esta tabela utiliza a a chave estrangeira da tabela relato.

| Nome | Descrição | Tipo de Dado | Tamanho | Null | PK | FK | Unique | Identity | Default | Check | 
| ------- | --------- | ------------ | ------- | ---- | -- | -- | ------ | -------- | ------- | ----- |
| conteudo | Conteudo do material publicado | TEXT |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   | 
| usuario_id | identificação do usuario que fez a publicação | INTEGER |   | &#9744;  | &#9744; | &#9745; | &#9744; | &#9744; |   |   | 
| comentario_id | identificação do relato comentado | INTEGER |   | &#9744;  | &#9745; | &#9744; | &#9744; | &#9744; |   |   |
| relato_id | identificação do relato | INTEGER |   | &#9744;  | &#9744; | &#9745; | &#9744; | &#9744; |   |   | 
| data_comentario | Data do momento que foi publicado o comentário | DATE |   | &#9744;  | &#9744; | &#9744; | &#9744; | &#9744; |   |   |