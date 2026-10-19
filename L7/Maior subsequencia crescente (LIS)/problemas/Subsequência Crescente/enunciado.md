# Subsequência Crescente

Fonte: Exercício do CSES [https://cses.fi/problemset/task/1145](https://cses.fi/problemset/task/1145), mas com casos de teste menores ($n \le 5000$).

## Descrição

Dada uma lista contendo $n$ números inteiros, sua tarefa é determinar a subsequência crescente mais longa do array, ou seja, a maior subsequência onde cada elemento é estritamente maior que o anterior.

Uma *subsequência* é uma sequência que pode ser derivada do array original removendo alguns (ou nenhum) elementos, sem alterar a ordem dos elementos restantes.

## Entrada
* A primeira linha contém um inteiro $n$: o tamanho do *array*.
* A segunda linha contém $n$ inteiros $x_1, x_2, \dots, x_n$: os elementos do *array*.

## Saída
Imprima um único inteiro: o comprimento da subsequência crescente mais longa.

## Restrições
* $1 \le n \le 5000$
* $1 \le x_i \le 10^9$

## Exemplo
                    
### Entrada:
```text
8
7 3 5 3 6 2 9 8
```

### Saída:
```text
4
```