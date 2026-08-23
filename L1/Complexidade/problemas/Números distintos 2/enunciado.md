# Números distintos 2
Fonte: [https://cses.fi/problemset/task/1621](https://cses.fi/problemset/task/1621)
Observação: a única diferença para o problema "Números distintos 1" é que o tamanho do vetor pode ser maior.
Dica: você pode usar a função `sort(V, V+n)` da STL para ordenar um vetor.

Você recebe uma lista de $n$ inteiros. Sua tarefa é calcular a quantidade de valores distintos nessa lista.

### Entrada
A primeira linha de entrada contém um inteiro $n$: a quantidade de valores.
A segunda linha contém $n$ inteiros $x_1, x_2, \dots, x_n$.

### Saída
Imprima um único inteiro: a quantidade de valores distintos.

### Restrições
* $1 \le n \le 2 \cdot 10^5$
* $1 \le x_i \le 10^9$

### Exemplo

**Entrada:**
```text
5
2 3 2 2 3
```
**Saída:**
```text
2
```
