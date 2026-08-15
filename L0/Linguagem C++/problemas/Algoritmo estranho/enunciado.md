# Algoritmo estranho
Fonte: [https://cses.fi/problemset/task/1068](https://cses.fi/problemset/task/1068)

Considere um algoritmo que recebe como entrada um inteiro positivo $n$. Se $n$ for par, o algoritmo o divide por dois; se $n$ for ímpar, o algoritmo o multiplica por três e adiciona um. O algoritmo repete esse processo até que $n$ seja igual a um. 

Por exemplo, a sequência para $n = 3$ é a seguinte:
$$3 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$$

Sua tarefa é simular a execução do algoritmo para um determinado valor de $n$.

### Entrada
A única linha de entrada contém um inteiro $n$.

### Saída
Imprima uma linha contendo todos os valores de $n$ ao longo da execução do algoritmo.

### Restrições
* $1 \le n \le 10^6$

### Exemplo

**Entrada:**
```text
3
```