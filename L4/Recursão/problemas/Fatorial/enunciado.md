# Fatorial recursivo

O fatorial de um número natural $n$ (chamado de n!) é o produto de todos os inteiros de $1$ até $n$.

A definição recursiva do fatorial é:

$n! = n \times (n-1)!$

com base:

$0! = 1$

Por exemplo:

- $0! = 1$
- $1! = 1$
- $5! = 120$
- $7! = 5040$

Sua tarefa é implementar uma função recursiva que calcule o fatorial de um número $N$.

---

## Entrada

A primeira linha da entrada contém um inteiro $N$ ($0 \leq N \leq 100000$), indicando o valor cujo fatorial deve ser calculado.

---

## Saída

Imprima um único inteiro, o valor de $N!$. Como o valor do fatorial pode ser muito alto, você deve calcular esse valor módulo 1000000007.

---

## Exemplos

### Exemplo 1

**Entrada:**
```text
5
```

**Saída:**
```text
120
```

---

### Exemplo 2

**Entrada:**
```text
0
```

**Saída:**
```text
1
```

---
