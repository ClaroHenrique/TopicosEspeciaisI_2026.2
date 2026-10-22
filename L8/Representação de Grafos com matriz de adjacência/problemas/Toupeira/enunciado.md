# Toupeira

Fonte: Adaptado da OBI 2023 fase 1 nível júnior - [https://olimpiada.ic.unicamp.br/passadas/OBI2023/fase1/programacao/](https://olimpiada.ic.unicamp.br/passadas/OBI2023/fase1/programacao/).

## Descrição
---

Senhor Toupeira é o prefeito de Morro Seco e ao longo dos anos mandou construir muitos túneis embaixo da terra, conectando salões de convivência que ele também mandou construir, para alegria de sua comunidade de toupeiras. Cada túnel conecta exatamente dois salões de convivência distintos e não há dois túneis conectando o mesmo par de salões. Túneis podem ser usados em ambas direções, ou seja, o túnel que conecta os salões $A$ e $B$ pode ser usado para ir de $A$ para $B$ ou de $B$ para $A$. Salões de convivência possuem identificadores únicos.

Senhor Toupeira agora quer incentivar que as toupeiras de Morro Seco façam caminhadas, para melhorar a saúde da comunidade. Para isso preparou um caderno com várias sugestões de passeio pelos túneis e salões de convivência, em que cada sugestão de passeio é descrita como uma sequência de salões de convivência, que devem ser visitados estritamente na ordem dada. No entanto, Senhor Toupeira foi alertado de que algumas das sugestões de passeio estão incorretas, pois não são possíveis.

A figura abaixo mostra um exemplo de salões de convivência e túneis, em que salões têm identificadores 1, 2, 3, 4 e 5.

*(Insira a imagem aqui)*

Um passeio composto pela sequência de salões $\{5, 3, 4, 3, 2\}$ é possível. Mas o passeio composto pela sequência de salões $\{2, 3, 5, 4\}$ não é possível, pois não existe túnel entre os salões 5 e 4.

Dados o mapa de túneis e salões de convivência, e uma lista de sugestões de passeio, escreva um programa que determine quantas sugestões de passeio são possíveis.

---

## Entrada

A primeira linha da entrada contém dois inteiros $S$ e $T$, indicando respectivamente o número de salões de convivência e o número de túneis. Salões são identificados por inteiros de $1$ a $S$. Cada uma das $T$ linhas seguintes descreve um túnel e contém um par de inteiros $X$ e $Y$, que indicam que o túnel conecta os salões $X$ e $Y$. A próxima linha da entrada contém um inteiro $P$ que indica o número de sugestões de passeio. Cada uma das $P$ linhas seguintes descreve uma sugestão de passeio e inicia com um inteiro $N$ que indica o número de salões do passeio, seguido de $N$ inteiros $C_i$, indicando a sequência de salões do passeio.

---

## Saída

Seu programa deve produzir uma única linha, contendo um único inteiro, o número de sugestões de passeio que são possíveis.

---

## Restrições

* $2 \le S \le 1\,000$
* $1 \le T \le \frac{S(S-1)}{2}$
* $1 \le X \le S$
* $1 \le Y \le S$
* $1 \le P \le 1\,000$
* $1 \le N \le 1\,000$
* $1 \le C_i \le S$, para $1 \le i \le N$
* $C_i \neq C_{i+1}$, para $1 \le i \le N-1$, ou seja, salões consecutivos em uma sugestão de passeio são distintos.


---

## Exemplos

### Exemplo de Entrada 1
```text
5 6
2 3
3 4
4 2
3 5
1 5
1 2
2
5 5 3 4 3 2
6 1 2 3 5 4 2
```

### Exemplo de Saída 1
```text
1
```

---

### Exemplo de Entrada 2
```text
4 2
1 2
3 4
3
4 1 2 1 2
5 4 3 4 3 4
2 1 4
```

### Exemplo de Saída 2
```text
2
```

---

### Exemplo de Entrada 3
```text
4 3
1 2
2 3
3 4
4
4 1 2 1 2
3 4 3 5
3 2 1 8
2 1 3
```

### Exemplo de Saída 3
```text
1
```