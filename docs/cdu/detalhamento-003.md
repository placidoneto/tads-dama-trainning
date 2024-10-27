# CDU003 - Publicar Relato

- **Ator principal**: Membros inscritos
- **Atores secundários**: 	 
- **Resumo**: O membro publica um relato.
- **Pré-condição**: O membro deve estar logado no sistema.
- **Pós-Condição**: O relato do membro é publicado no "Mural de Força".

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O membro clica em "Publicar Relato" na página do usuário logado. | |  
| | 2 - O sistema mostra uma página com uma caixa de texto.  | 
| 3 - O usuário digita seu relato e clica em "Publicar". | |  
| | 4 - O sistema pede para o usuário verificar o relato, informa que as informações passadas devem ser fidedignas e pede que ele aceite os Termos de Uso da plataforma.| 
| 5 - O usuário verifica, aceita os termos clica em "Confirmar". | |  
| | 6 - O sistema mostra uma mensagem de confirmação que o relato foi publicado e o membro é redirecionado para o "Mural de Força". | 

## Fluxo Alternativo I - Passo 1.
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O membro clica em "Publicar Relato" na página "Mural de Força". | |  
| | 1.2 - O usuário é devolvido para o passo 2. |

## Fluxo Alternativo II - Passo 2.
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - O usuário não digita o relato e clica em "Publicar". | |  
| | 2.2 - O sistema exibe uma mensagem de erro pedindo que o usário digite seu relato. |  
| | 2.3 - O usuário é devolvido para o passo 2. | 

## Fluxo Alternativo II - Passo 4.
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 3.1 - O usuário não  clica em "Aceitar os Termos da Plataforma" e clica em "Publicar". | |  
| | 3.2 - O sistema exibe uma mensagem de erro pedindo que o usário aceite os termos. |  
| | 3.3 - O usuário é devoldido para o passo 4. | 

## Imagem Representativa do Caso de Uso
![Caso de uso Relato](https://imgur.com/lMUB8qS.png)

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

![Caso de uso Relato](https://imgur.com/49rpdx7.png)

## Diagrama de Classes de Projeto

![Caso de uso Relato](https://imgur.com/gmKMUVW.png)