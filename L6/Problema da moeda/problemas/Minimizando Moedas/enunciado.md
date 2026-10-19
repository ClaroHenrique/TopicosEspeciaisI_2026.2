# CSES - Minimizando Moedas (Minimizing Coins)

Fonte: Minimizing Coins - CSES [https://cses.fi/problemset/task/1634](https://cses.fi/problemset/task/1634)

## Descrição

Considere um sistema monetário constituído por $n$ moedas. Cada moeda possui um valor inteiro positivo. Sua tarefa é produzir uma soma de dinheiro $x$ usando as moedas disponíveis de forma que o número de moedas seja o menor possível.

Por exemplo, se as moedas forem $\{1, 5, 7\}$ e a soma desejada for $11$, uma solução ótima é $5 + 5 + 1$, que requer $3$ moedas.


## Entrada

- A primeira linha da entrada contém dois inteiros $n$ e $x$: o número de moedas e a soma de dinheiro desejada.
- A segunda linha contém $n$ inteiros distintos $c_1, c_2, \dots, c_n$: o valor de cada moeda.


## Saída

- Imprima um número inteiro: o número mínimo de moedas necessário. Se não for possível produzir a soma desejada, imprima `-1`.

---

## Restrições

- $1 \le n \le 100$
- $1 \le x \le 10^6$
- $1 \le c_i \le 10^6$

---

## Exemplo

**Entrada:**
```text
3 11
1 5 7
```

**Saída:**
```text
3
```