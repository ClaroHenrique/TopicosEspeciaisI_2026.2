# CSES - Divisão de Maçãs

Fonte: CSES - [https://cses.fi/problemset/task/1623](https://cses.fi/problemset/task/1623)

---

### Descrição do Problema

Existem $n$ maçãs com pesos conhecidos. Sua tarefa é dividir as maçãs em dois grupos de modo que a diferença entre os pesos totais dos dois grupos seja a menor possível (mínima).

---

### Entrada

- A primeira linha da entrada contém um número inteiro $n$: a quantidade de maçãs.
- A linha seguinte contém $n$ inteiros $p_1, p_2, \dots, p_n$: o peso de cada maçã.

---

### Saída

- Imprima um único número inteiro: a diferença mínima entre os pesos dos dois grupos.

---

### Restrições

- $1 \le n \le 20$
- $1 \le p_i \le 10^9$

---

### Exemplo

**Entrada:**
```text
5
3 2 7 4 1
```

**Saída:**
```text
1
```

**Explicação:**  
O Grupo 1 tem pesos $2, 3$ e $4$ (peso total $9$), e o Grupo 2 tem pesos $1$ e $7$ (peso total $8$). A diferença entre eles é $|9 - 8| = 1$.