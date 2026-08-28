# Soma de Dois Valores

Fonte: CSES [https://cses.fi/problemset/task/1640](https://cses.fi/problemset/task/1640)

## Descrição

Você recebe um array de $n$ números inteiros e sua tarefa é encontrar dois valores (em posições distintas) cuja soma seja igual a $x$.

## Entrada

- A primeira linha da entrada contém dois inteiros $n$ e $x$: o tamanho do array e a soma alvo.
- A segunda linha contém $n$ inteiros $a_1, a_2, \dots, a_n$: os valores do array.

## Saída

Imprima dois inteiros distintos $p1$ e $p2$: as posições (índices baseados em 1) dos dois valores. Se houver várias soluções possíveis, priorize a que tiver o menor valor de $p1$ e depois priorize o menor valor de $p2$. Caso não exista nenhuma solução, imprima `IMPOSSIBLE`.

## Restrições

- $1 \le n \le 2 \cdot 10^5$
- $1 \le x, a_i \le 10^9$

---

## Exemplo 1

### Entrada
```text
4 8
2 7 5 1
```

### Saída
```text
2 4
```


---

## Exemplo 2

### Entrada
```text
4 5
2 1 3 4
```

### Saída
```text
1 3
```

Note que você deve escolher os índices 1 e 3 ao invés de 1 e 4. Essa restrição foi adicionada para facilitar a correção e não existe no problema original.