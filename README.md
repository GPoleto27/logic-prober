# Logic Prober - Semantic Analysis
Pesquisar e desenvolver um analisador semântico para expressões lógicas e integrá-lo com os analisadores Lexical, Sintático e Otimizador.
Analisador implementado em Python, análise lexical descrita pelo autômato representado em *automato_base.png*

> *Detalhes de implementação descritos nos comentários do código*

## Done
- Reestruturação do Analisador Lexical

## To-Do
- Reestruturação do Analisador Sintático
- Desenvolvimento do Analisador Semântico
- Integração dos analisadores com o otimizador (Mapa de Karnaugh)

# O que pesquisar para a análise semântica
## Shunting-yard Algorithm
Is a method for parsing mathematical expressions specified in infix notation. It can produce either a postfix notation string, also known as Reverse Polish notation (RPN), or an abstract syntax tree (AST).

## Reverse Polish Notation (RPN)
Is a mathematical notation in which operators follow their operands, in contrast to Polish notation (PN), in which operators precede their operands. It does not need any parentheses as long as each operator has a fixed number of operands.