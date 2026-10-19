# Consultas de Fibonacci

## Descrição do Problema

Para esse problema, você deve responder a uma série de Q consultas. Cada consulta i consiste em receber um número inteiro N_i e calcular o valor de F(N_i), onde F é a sequência de Fibonacci.

A sequência de Fibonacci é definida da seguinte forma:

- F(0) = 0
- F(1) = 1
- F(n) = F(n - 1) + F(n - 2) para n >= 2

Assim, os primeiros termos são:

0, 1, 1, 2, 3, 5, 8, 13, ...

Como esse valor pode crescer muito rapidamente, imprima o resultado modulo 1000000007.

---

## Entrada

A primeira linha da entrada contém um inteiro Q (1 <= Q <= 1000).
As próximas Q linhas contêm um inteiro cada: N_1, N_2, ..., N_Q (0 <= N_i <= 10^6).

---

## Saída

Para cada consulta, imprima uma linha contendo o valor de F(N_i) mod 1000000007.

---

## Exemplos

### Exemplo 1

**Entrada:**
```text
5
0
1
2
3
5
```

**Saída:**
```text
0
1
1
2
5
```

### Exemplo 2

**Entrada:**
```text
4
10
20
50
100
```

**Saída:**
```text
55
6765
586268941
687995182
```
