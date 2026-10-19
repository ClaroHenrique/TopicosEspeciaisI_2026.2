# Consultas de Soma de Intervalo Estático

Fonte: [https://cses.fi/problemset/task/1646](https://cses.fi/problemset/task/1646)

## Descrição

Dado um array de $n$ inteiros, sua tarefa é processar $q$ consultas na forma: qual é a soma dos valores no intervalo $[a, b]$?

---

## Entrada

A primeira linha da entrada contém dois inteiros $n$ e $q$: o número de valores e o número de consultas.


A segunda linha contém $n$ inteiros $x_1, x_2, \dots, x_n$: os valores do array.


Por fim, há $q$ linhas descrevendo as consultas. Cada linha contém dois inteiros $a$ e $b$: qual é a soma dos valores no intervalo $[a, b]$?


## Saída

Imprima o resultado de cada consulta.


## Restrições

- $1 \le n, q \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$
- $1 \le a \le b \le n$


## Exemplo

### Entrada:
```text
8 4
3 2 4 5 1 1 5 3
2 4
5 6
1 8
3 3
```

### Saída:
```text
11
2
24
4
```