# Contando mentirosos

Fonte: USACO - [https://usaco.org/index.php?page=viewproblem2&cpid=1228](https://usaco.org/index.php?page=viewproblem2&cpid=1228)

### Descrição do Problema

A vaca Bessie está escondida em algum lugar ao longo da reta numérica. Cada uma das outras $N$ vacas do Fazendeiro John ($1 \le N \le 1000$) tem uma informação a compartilhar: a $i$-ésima vaca diz que Bessie está escondida em uma posição menor ou igual a $p_i$, ou que Bessie está escondida em uma posição maior ou igual a $p_i$ ($0 \le p_i \le 10^9$).

Infelizmente, é possível que nenhuma posição de esconderijo seja consistente com as respostas de todas as vacas, o que significa que nem todas as vacas estão dizendo a verdade. Conte o número mínimo de vacas que precisam estar mentindo.

---

### Formato de Entrada (stdin)

- A primeira linha contém o inteiro $N$.
- As próximas $N$ linhas contêm um caractere (`L` ou `G`), seguido por um número inteiro $p_i$.
  - `L` (*Less*) indica que a $i$-ésima vaca diz que a localização de Bessie é menor ou igual a $p_i$.
  - `G` (*Greater*) indica que a $i$-ésima vaca diz que a localização de Bessie é maior ou igual a $p_i$.

---

### Formato de Saída (stdout)

- Imprima o número mínimo de vacas que precisam estar mentindo.

---

### Exemplo de Entrada 1

```text
2
G 3
L 5
```

### Exemplo de Saída 1

```text
0
```

*Explicação:* É possível que nenhuma vaca esteja mentindo (por exemplo, se Bessie estiver na posição 3, 4 ou 5).

---

### Exemplo de Entrada 2

```text
2
G 3
L 2
```

### Exemplo de Saída 2

```text
1
```

*Explicação:* Pelo menos uma das vacas precisa estar mentindo (pois não existe posição que seja simultaneamente $\ge 3$ e $\le 2$).
