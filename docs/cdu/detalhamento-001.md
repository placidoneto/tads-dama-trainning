# CDU001 - Publicar Material Educativo

- **Ator principal**: Usuários do tipo ONG ou Profissionais
- **Resumo**: Profissional ou ONG publica um material educativo no sistema
- **Pré-condição**: Usuário estar logado e ser um profissional ou uma ONG

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O usuário clica em Publicar Material na página de usuário logado | |  
| | 2 - O sistema mostra uma página com uma caixa de texto e os botões Aceitar os Termos da Plataforma e Submeter Conteúdo | 
| 3 - O usuário digita o conteúdo a ser publicado  e clica nos dois botões | |
| | 4 -O sistema exibe uma mensagem que o conteúdo submetido irá passar po análise antes de ser publicado e um botão Confirmar |
| 5- O usuário clica no botão | |
| | 6- O Sistema direciona para a página de usuário logado |
| | |


## Fluxo Alternativo I - Passo 1
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário clica em Publicar Material na página de exibição de materiais educativos | |  
| | 1.2 - O usuário é direcionado ao passo 2 |
| | |

## Fluxo de Exceção I - passo 3
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - O usuário não digita o conteúdo a ser publicado e clica nos dois botões | |  
| | 2.2 - O sistema exibe uma mensagem pedindo que o usuário digite o conteudo do relato |  
| | 2.3 O usuário é direcionado ao passo 3 |
| | |

## Fluxo de Exceção II - passo 3
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 3.1 O usuário digita o conteúdo a ser publicado e clica apenas em Submeter Conteúdo | |
| | 3.2  O sistema exibe uma mensagem pedindo que o usuário aceite os termos da plataforma |
| | 3.3 o usuário é direcionado ao passo 3 |
| | |

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...