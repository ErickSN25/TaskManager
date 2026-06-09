# Post-Mortem — Missão de Release

## Time
- Tech Lead: Erick
- Dev A: Kevylly
- Dev B: F. Salesvanio
- QA/Release: F. Salesvanio

---

## O que funcionou bem

--> O que foi feito pelo Tech Lead (Erick), e que deu certo:


--------------------

--> O que foi feito na Feature A (Kev), e que deu certo:

Como Dev A, criei a branch feature/dev-a a partir da develop para implementar a melhoria no formato de exibição das tarefas (utils.py). Garanti a criação de commits atômicos e semânticos (como 'feat: improve task formatting', 'fix: standardize task formatting output' e 'refactor: improve task display layout') para estruturar bem o histórico. O desenvolvimento da lógica funcionou perfeitamente e a integração inicial com a develop foi bem-sucedida após a revisão do Tech Lead.

--------------------

--> O que foi feito na Feature B (Sales), e que deu certo: 

Eu criei a branch para começar o desenvolvimento. Adicionei 3 commits conforme indicado:
feat: exibi a prioridade no format_task
fix: corrigi o bug na nova funcionalidade
refactor: inverti a logica de apresentação em filter_tasks

Até o momento a atividade estava de certo modo Ok e funcionando. No entanto, necessitei fazer o rebase para poder subir as atualizações, ai que começou a ficar difícil, pricipalmente porque nunca tinha feito isso antes.

-----------------

--> O que foi feito pelo QA/Release (Sales), e que deu certo:

O QA criou a nova bramch Release/1.0 para inseri um bug ao código em produção na main e realizar, posteriormente, o HotFix (um conserto rápido do código que está na produção).
Deste modo, criei o PR da nova branch (release/1.0) para a main (aprovado pelo Tech Lead) o erro foi para aprodução. Então criei uma branch HotFix para consertar rapidamente e enviei para o github e pedi um PR novamente para corrigir o erro.

## O que deu errado ou foi difícil

--> Relato Dev B (Sales):
O que foi difícil doi o rebase, pois nunca tinha visto ou feito antes. Mas consegui reralizar a junção dos conflitos e garantir que ambos os lados do código estivessem em coexistentes. Antes de abrir o PR fiz o git rebase develop na minha feature (feature/dev-b) para poder atualizar a minha branch do que tinha de mais atual na develop. Resolvi os conflitos de forma manual, tentando garantir os dois lados do conflito (o que gerou confusão pois foi complicado),  mas consegui. A partir disso fiz o push da minha feature e criei um PR para a develop. (que foi analisado por Erick).

--> Relato Dev A (Kev):

O maior desafio foi compreender e lidar com o fluxo de integração e as regras de mensagens exigidas nas etapas finais. Após o merge do PR na branch principal via interface do GitHub, houve uma pequena confusão de comunicação sobre a necessidade de customizar a mensagem de commit do merge para incluir as palavras "merge" e "release". Como o PR já havia sido fechado e consolidado como "Merged", foi difícil tentar alterar o histórico retroativamente de forma remota, e também enfrentamos problemas temporários de conexão ("Connection was reset") no terminal ao tentar rodar comandos de sincronização (git pull) devido a conflitos de concorrência com o OneDrive local. Resolvemos registrando a documentação da release através dos comentários do próprio Pull Request para manter o histórico transparente sem corromper a árvore de commits.

--> Relato QA (Sales):
Foi meio difícil começar nesse novo modo de produção por ser o primeiro contato, mas rapidadmente consegui compreender o fluxo do processo de produção, o que fez muito mais sentido para sempre garantir que tudo ocorra certo e sem erros, e atê quando os erros existirem uma maneira de trabalhar já está articulada.

## Onde usamos rebase (e por quê)

O rebase foi utilizado por Sales para trazer as atualizações da develop para sua feature (feature B), e garantir que sua branch estivesse atulizado com a develop para subir suas novas adições ao github.

## Onde usamos merge (e por quê)

O merge foi utilizado em duas situações cruciais:
1. Pelo GitHub, na interface dos Pull Requests, para integrar as branches de feature concluídas de volta para a branch develop, mantendo o registro visual e cronológico das entregas em equipe.
2. No processo de Hotfix, onde as correções aplicadas na branch hotfix/fix-filter foram obrigatoriamente mescladas (via merge) tanto na branch main quanto na branch develop. Isso garantiu que o bug fosse corrigido imediatamente no código de produção e que o ambiente de desenvolvimento não ficasse desatualizado.

## O que faríamos diferente

No geral nada em específico, o resultado foi satisfatório no geral