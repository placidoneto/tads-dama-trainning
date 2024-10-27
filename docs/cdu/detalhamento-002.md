# CDU002 - Manter Perfil

- **Ator principal**: Membros inscritos
- **Atores secundários**: 	 
- **Resumo**: O membro atualiza suas informações de perfil.
- **Pré-condição**: O membro deve estar logado.
- **Pós-Condição**: Os dados atualizados são salvos no perfil.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O membro clica em "Manter Perfil" na página de usuário logado. | |  
| | 2 - O sistema mostra os dados do usuário e um botão "Salvar Alterações". | 
| 3 - O usuário escolhe um ou mais dados e o(s) altera, depois clica em "confirmar". | |  
| | 4 - O sistema exibe uma mensagem informando que os dados foram salvos. | 

## Fluxo Alternativo I - Passo 3. 
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário deixa um ou mais dados em branco e tenta salvar. | |  
| | 1.2 - O sistema mostra uma mensagem pedindo para os dados sejam preenchidos.  |
| | 1.3 - O usuário é direcionado para o passo 2.  |


> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (https://imgur.com/8Qgk5LE.png)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto (https://imgur.com/depV7hH.png)

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...