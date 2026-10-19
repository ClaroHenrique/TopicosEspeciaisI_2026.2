# Tribonacci

A sequência de Tribonacci não é tão famosa 😞.


Cada termo dessa sequência é definido da seguinte forma:

$F_0 = 0$

$F_1 = 1$

$F_2 = 1$


$F_n = F_{n-1} + F_{n-2} + F_{n-3}, \quad \text{para } n \geq 3$


Por exemplo, os 10 primeiros termos são: 0, 1, 1, 2, 4, 7, 13, 24, 44, 81.

Sua tarefa é implementar uma **função recursiva** que calcule o n-ésimo ($F_n$) número da sequência de Tribonacci.

---

## Entrada

A primeira linha da entrada contém um inteiro $N$ ($0 \leq N \leq 20$), indicando qual o termo da sequência deve ser calculado.

---

## Saída

Imprima um único inteiro, o n-ésimo número da sequência de Tribonacci.

---

## Exemplos

### Exemplo 1

**Entrada:**
```text
1
```

**Saída:**
```text
1
```

---

### Exemplo 2

**Entrada:**
```text
8
```

**Saída:**
```text
44
```

---
