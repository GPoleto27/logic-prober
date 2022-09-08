# Logic Prober

Pesquisar e desenvolver analisadores lexical, sintático e semântico para expressões lógicas e integrá-los entre si e com um otimizador.

> *Detalhes de implementação descritos nos comentários do código*


### Done

- Reestruturação do Analisador Lexical
- Reestruturação do Analisador Sintático
- Desenvolvimento do Analisador Semântico
- Integração dos analisadores com o otimizador (Mapa de Karnaugh)


## Análise Lexical

Para o desenvolvimento do analisador lexical foi implementada a máquina de estados descrita em  [LEXF: Um Analisador Lexical Eficiente
e Multipropósito](https://eventos.utfpr.edu.br//sicite/sicite2020/paper/view/7353):

![Autômato base](/automato_base.png)

A expressão é lida como _string_ e cada caracter é consumido de forma percorrer a máquina de estado por suas regras de transição. Se houver alguma transição inválida ou ao final da leitura da expressão o estado atual não for final a expressão será então recusada e mensagens de erro serão retornadas explicitando qual o tipo de erro e onde ele ocorre, caso contrário, a expressão é aceita e pode ser passada para a análise sintática. O analisador lexical retorna uma tupla contendo um booleano representando sucesso da operação, uma lista de tuplas _(token, valor)_ aceitas caso a operação tenha tido êxito ou _None_ caso contrário e uma lista de erros caso a operação tenha falhado ou _None_ caso contrário.


## Análise sintática

A análise sintática foi completamente reescrita e recebe como entrada uma lista de tuplas _(token, valor)_. O analisador então executa o algoritmo shunting yard para que a expressão seja estruturada seguindo a notação polonesa reversa (NPR), o que nos retorna uma fila de tuplas _(token, valor)_ em NPR para que então cada operação atômica seja validada de acordo com as regras sintáticas da lógica proposicional, se todas as operações atômicas forem aceitas, a expressão é aceita e pode ser passada para a análise semântica. O analisador sintático retorna uma tupla contendo um booleano representando sucesso da operação, uma fila de tuplas _(token, valor)_ em NPR aceitos caso a operação tenha tido êxito ou _None_ caso contrário e uma lista de erros caso a operação tenha falhado ou _None_ caso contrário.


## Análise semântica

Para o desenvolvimento do analisador semântico é utilizada a estrtura de árvore de sintaxe abstrata para a valoração de todas as possiveis combinações e recebe como entrada uma fila de tuplas _(token, valor)_ em NPR a partir da qual a árvore é estruturada e então todas as combinações de valores das variáveis são valorados e adicionados a lista de booleanos representando a tabela verdade da expressão, que é retornada.


## Otimização de expressões lógicas

Para a integração do otimizador de expressões lógicas foi utilizado o [Kuine](https://github.com/luanaccampos/kuine), de onde foram extraídos [quine.py](/src/quine.py), [setCoverPD.py](/src/setCoverPD.py) e [setCoverGreedy.py](/src/setCoverGreedy.py) implementados por [Luana Cristina Guerreiro Campos](https://github.com/luanaccampos) e descritos no artigo [Software educacional para ensino de minimização de expressões lógicas](https://eventos.utfpr.edu.br/sicite/sicite2021/paper/view/7870).
