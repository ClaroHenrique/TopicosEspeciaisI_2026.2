# Consultas de fatorial

## Descrição do Problema

Para esse problema, você deve responder a uma série de Q consultas. Cada consulta $i$ consiste em receber um número inteiro $N_i$ e calcular o valor de $N_i!$ (fatorial de $N_i$).

Você já deve estar careca de saber o que é o fatorial, mas é uma boa prática do problema explicar. O fatorial de um número inteiro $n$ é definido como o produto de todos os inteiros positivos menores ou iguais a $n$. Por exemplo, $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$. Como esse número pode ser muito grande, imprima o resultado resto 1000000007.

---

## Entrada

A primeira linha da entrada contém um inteiro $Q$ ($1 \le Q \le 1000$).  
As próximas $Q$ linhas contêm um inteiro cada: $N_1, N_2, \dots, N_Q$ ($0 \le N_i \le 10^6$).

---

## Saída

Para cada consulta, imprima uma linha contendo o valor de $N_i! \mod 1000000007$.

---

## Exemplos

### Exemplo 1

**Entrada:**
```text
4
1
2
3
4
```

**Saída:**
```text
1
2
6
24
```
