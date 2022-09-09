# Integração e Otimização de um Analisador de Expressões da Lógica Proposicional

###### Guilherme Poleto, Gustavo Henrique Paetzold

## Introdução

## Materiais e Métodos

A álgebra booleana é um sistema de regras e valores que busca descrever problemas lógicos a partir de dois possíveis valores: verdadeiro ou falso, e três operações fundamentais: disjunção (_and_), conjunção (_or_) e negação (_not_), este conjunto de regras é a fundação da lógica proposicional, que é aplicada para definir o comportamento lógico de um conjunto de entradas.

Uma expressão lógica é um conjunto de conectivos (operações) e literais (variáveis) que possui um valor-verdade associado, esta expressão pode ser dividida em subconjuntos que respeitam a precedência de operações de seus conectivos, todos os subconjuntos possuem um valor-verdade associado, o componente elementar de uma expressão lógica é o literal que não possui conectivos. Valor-verdade é a valoração binária (verdadeiro ou falso) que uma expressão lógica apresenta, o conjunto de todos os valores-verdade de uma expressão lógica é chamada tabela verdade.

| A | B | ~A | ~B | A ∧ B | A ∨ B |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 |

#### Desenvolvimento e integração do analisador

Para a implementação do processo de análise de expressões lógicas, que consiste de três etapas, foi escrito um programa na linguagem de programação Python responsável por interfacear a entrada das proposições com o analisador, na analise léxica uma sequência de caracteres representando a expressão é consumida por uma máquina de estados que descreve as características léxicas da linguagem proposta para a representação das sentenças lógicas, para este fim, foi realizada a implementaçao máquina de estados descrita em [LEXF: Um Analisador Lexical Eficiente
e Multipropósito](https://eventos.utfpr.edu.br//sicite/sicite2020/paper/view/7353) que tem como resultado a _tokenização_ da expressão. [EXPLICAR TOKENIZAÇÃO] Na etapa seguinte é analisada a estrutura sintática da expressão, utilizando-se do algoritmo shunting-yard para a verificação a completude da expressão e de suas subdivisões e converter a notação convencional em notação polonesa reversa de forma a respeitar precedência de operações da álgebra de Boole. [EXPLICAR SHUNTING YARD] [EXPLICAR NOTAÇÃO POLONESA REVERSA] Na última etapa da análise é realizada a valoração de cada um de seus literais numa estrutura recursiva chamada árvore sintática abstrata que é construída de forma em que os nós-folha representem os componentes elementares da expressão, cada nó intermediário represente a valoração dos conectivos e o nó raiz represente o valor-verdade da expressão completa, a valoração ocorre de baixo para cima, ou seja, os primeiros nós a serem valorados são os nós-folha, precedidos por seus conectivos de forma recursiva até a valoração do nó raiz.

Como resultado dessa análise obtem-se os tokens léxicos estruturados em notação polonesa reversa e por fim a tabela verdade da expressão completa, com a qual podemos verificar os termos de satisfabilidade da expressão. É possível também valorar a tabela verdade de qualquer expressão intermediária a partir da valoração da sub-árvore que a representa.

#### Integração com minimizador de expressões lógicas

Para afirmar que duas expressões lógicas quaisquer são equivalentes é necessário que se observe o mesmo número de variáveis e a mesma tabela verdade associada a cada uma das expressões, otimização lógica é o processo de buscar uma expressão equivalente que minimize o número de operações intermediárias, para tanto foi integrado neste analisador o algoritmo de otimização de Quine-McCluskey descrito e implementado em [Software para minimização de expressões lógicas utilizando Mapas de Karnaugh](https://eventos.utfpr.edu.br//sicite/sicite2020/paper/view/6073), que conta com uma implementação de um algoritmo de programação dinâmica e outro algoritmo guloso para solução do problema. Quine-McCluskey baseia sua solução na análise de implicantes a partir de mapas de Karnaugh para representar a sentença na forma de soma de produtos, utilizando-se apenas das três operações básicas da álgebra booleana. [EXPLICAR SOMA DE PRODUTOS]

## Resultados e Discussões

## Conclusão

## Agradecimentos

## Disponibilidade de código

O código-fonte está disponibilizado na plataforma online [GitHub](github.com/GPoleto27/logic-prober) sob licença _GNU General Public License v3.0_.

## Conflito de interesse
Não há conflito de interesse.

## Referências
