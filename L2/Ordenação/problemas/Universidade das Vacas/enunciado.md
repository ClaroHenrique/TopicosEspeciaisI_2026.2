# Universidade das Vacas

Fonte: USACO [https://usaco.org/index.php?page=viewproblem2&cpid=1251](https://usaco.org/index.php?page=viewproblem2&cpid=1251)


## Descrição

O Fazendeiro John está planejando abrir uma nova universidade para vacas!

![Vaca estudante](midia/cow.png)

Existem $N$ ($1 \le N \le 10^5$) vacas que potencialmente poderiam frequentar esta universidade. Cada vaca está disposta a pagar uma mensalidade máxima de $c_i$ ($1 \le c_i \le 10^6$). O Fazendeiro John pode definir um valor único de mensalidade que todas as vacas devem pagar para se matricular. Se essa mensalidade for estritamente maior do que o valor máximo que uma vaca está disposta a pagar, a vaca não se matriculará na universidade. 

O Fazendeiro John deseja arrecadar a maior quantidade possível de dinheiro para poder pagar um salário justo aos seus instrutores. Por favor, determine quanto dinheiro ele pode arrecadar e qual o valor da mensalidade que ele deve cobrar.


## Formato de Entrada

- A primeira linha contém um único número inteiro $N$.
- A segunda linha contém $N$ números inteiros $c_1, c_2, \dots, c_N$, onde $c_i$ representa a mensalidade máxima que a vaca $i$ está disposta a pagar.

---

## Formato de Saída

Imprima a quantidade máxima de dinheiro que o Fazendeiro John pode arrecadar e o valor ótimo da mensalidade que ele deve cobrar, separados por um espaço em branco. Se houver múltiplas soluções com a mesma arrecadação máxima, imprima a solução com a **menor** mensalidade ótima.

> **Nota:** O tamanho dos valores envolvidos neste problema pode exigir o uso de tipos de dados inteiros de 64 bits (por exemplo, `long` em Java ou `long long` em C/C++).

---

## Exemplo

### Entrada

```text
4
1 6 4 6
```

### Saída

```text
12 4
```

### Explicação

Se o Fazendeiro John cobrar uma mensalidade de $4$, então $3$ vacas irão se matricular (aquelas com valores máximos $6$, $4$ e $6$), permitindo que ele arrecade um total de $3 \cdot 4 = 12$.
