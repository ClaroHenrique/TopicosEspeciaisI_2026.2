# Um positivo e um negativo

Este problema é uma versão mais fácil do problema "Produto do Intervalo" da Maratona de Programação 2012, Fase 2.

## Descrição

Dado um vetor de tamanho N composto apenas pelos inteiros 1 e -1, sua tarefa é responder a Q consultas no seguinte formato: qual o resultado da multiplicação de todos os elementos em um intervalo [L, R]?


## Entrada

A primeira linha contém dois inteiros `n` e `q`, indicando o tamanho do vetor e número de consultas.

Na próxima linha contém N inteiros separados por espaço, indicando os elementos do vetor $A_i$ na ordem correspondente (indexado em 0).

Por fim, há Q linhas indicando cada consulta que consiste de dois inteiros $L_i$ e $R_i$.


## Saída

Seu programa deve imprimir a resposta de cada consulta na ordem em que elas aparecem.

## Restrições

* $1 \le n \le 10^5$
* $1 \le q \le 10^5$
* $A_i \in \{-1, 1\}$
* $0 \le L_i \le R_i \le n-1$

---

## Exemplo

**Entrada:**
```text
5 3
1 -1 -1 1 -1
0 4
1 3
2 2
```

**Saída:**
```text
-1
1
-1
```

