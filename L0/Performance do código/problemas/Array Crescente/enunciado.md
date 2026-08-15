# Array Crescente
Fonte: [https://cses.fi/problemset/task/1094](https://cses.fi/problemset/task/1094)

Você recebe um *array* de $n$ inteiros. Seu objetivo é modificar o *array* para que ele se torne não decrescente, isto é, cada elemento seja pelo menos tão grande quanto o elemento anterior.

Em cada movimento, você pode aumentar o valor de qualquer elemento em um. Qual é o número mínimo de movimentos necessários?

### Entrada
A primeira linha de entrada contém um inteiro $n$: o tamanho do *array*.
A segunda linha contém $n$ inteiros $x_1, x_2, \dots, x_n$: os elementos do *array*.

### Saída
Imprima o número mínimo de movimentos necessários.

### Restrições
* $1 \le n \le 2 \cdot 10^5$
* $1 \le x_i \le 10^9$

### Exemplo

**Entrada:**
```text
5
3 2 5 1 7
```
**Saída:**
```text
5
``` 