# Número Desaparecido
Fonte: [https://cses.fi/problemset/task/1083](https://cses.fi/problemset/task/1083)

Você recebe todos os números de $1, 2, \dots, n$, exceto um. Sua tarefa é encontrar o número que está faltando.

### Entrada
A primeira linha de entrada contém um inteiro $n$.
A segunda linha contém $n - 1$ números. Cada número é distinto e está entre $1$ e $n$ (inclusive).

### Saída
Imprima o número que está faltando.

### Restrições
* $2 \le n \le 2 \cdot 10^5$

### Exemplo

**Entrada:**
```text
5
2 3 1 5
```
**Saída:**
```text
4
```

### Dica:

Você pode resolver essa usando a fórmula da soma dos primeiros $n$ números inteiros: $\frac{n(n + 1)}{2}$.

Alternativamente, você pode usar ordenação. Se você ordenar, pode utilizar a função `sort` do C++: `sort(V, V + n)`, onde V é o vetor e $n$ é a quantidade de elementos. Essa função é muito mais eficiente do que o BubbleSort ou SelectionSort por exemplo.

