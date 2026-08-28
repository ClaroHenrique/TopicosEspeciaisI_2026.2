# Consultas sobre elementos menores ou iguais

Fonte: Adaptado do Codeforces (casos de testes diferentes) - [https://codeforces.com/problemset/problem/600/B](https://codeforces.com/problemset/problem/600/B)

## Descrição do Problema

São dados dois vetores de números inteiros $a$ e $b$. Para cada elemento do segundo vetor $b_j$, você deve encontrar a quantidade de elementos no vetor $a$ que são menores ou iguais ao valor $b_j$.

---

## Entrada

- A primeira linha contém dois inteiros $n$ e $m$ ($1 \le n, m \le 2 \cdot 10^5$) — os tamanhos dos vetores $a$ e $b$, respectivamente.
- A segunda linha contém $n$ inteiros — os elementos do vetor $a$ ($-10^9 \le a_i \le 10^9$).
- A terceira linha contém $m$ inteiros — os elementos do vetor $b$ ($-10^9 \le b_j \le 10^9$).

---

## Saída

Imprima $m$ inteiros separados por espaços, onde o $j$-ésimo número é a quantidade de elementos no vetor $a$ que são menores ou iguais ao valor $b_j$.

---

## Exemplos

### Exemplo 1

**Entrada:**
```text
5 4
1 3 5 7 9
6 4 2 8
```

**Saída:**
```text
3 2 1 4
```

---

### Exemplo 2

**Entrada:**
```text
5 5
1 2 1 2 5
3 1 4 1 5
```

**Saída:**
```text
4 2 4 2 5
```
