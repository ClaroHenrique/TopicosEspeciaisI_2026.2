# Máquinas de Fábrica

Fonte: CSES [https://cses.fi/problemset/task/1620](https://cses.fi/problemset/task/1620)

## Descrição do Problema

Uma fábrica possui $n$ máquinas que podem ser utilizadas para fabricar produtos. Seu objetivo é produzir um total de $t$ produtos.

Para cada máquina, você sabe o tempo em segundos necessário para fabricar um único produto. As máquinas podem operar simultaneamente, e você pode definir livremente o cronograma de trabalho delas.

Qual é o menor tempo necessário para fabricar os $t$ produtos?

---

## Entrada

- A primeira linha de entrada contém dois números inteiros $n$ e $t$: o número de máquinas e o total de produtos a serem fabricados, respectivamente.
- A segunda linha contém $n$ inteiros $k_1, k_2, \dots, k_n$: o tempo necessário para cada máquina fabricar um produto.

---

## Saída

- Imprima um único número inteiro: o tempo mínimo necessário para produzir $t$ produtos.

---

## Restrições

- $1 \le n \le 2 \cdot 10^5$
- $1 \le t \le 10^9$
- $1 \le k_i \le 10^9$

---

## Exemplo

### Entrada:
```text
3 7
3 2 5
```

### Saída:
```text
8
```

### Explicação:
Em 8 segundos, a máquina 1 produz $2$ produtos (leva $6$ s), a máquina 2 produz $4$ produtos (leva $8$ s) e a máquina 3 produz $1$ produto (leva $5$ s). O total de produtos fabricados é $2 + 4 + 1 = 7$ produtos em $8$ segundos.
