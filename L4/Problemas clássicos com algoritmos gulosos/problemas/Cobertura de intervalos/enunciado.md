

Versão mais difícil: Online Judge (N maior e requer também imprimir os intervalos da solução) - [https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=961](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=961)


# Cobertura de intervalos

Temos uma faixa linear de comprimento $M$ e um conjunto de $N$ intervalos, onde cada intervalo $i$ cobre a faixa no intervalo de $[L_i, R_i]$. Selecione um conjunto de intervalos de forma que cada ponto entre $[0, M]$ deve estar contido em pelo menos um dos intervalos escolhidos.

Calcule a menor quantidade de intervalos necessários para cobrir toda a faixa de comprimento $M$.

---

## Entrada

A primeira linha da entrada contém dois inteiros $N$ ($1 \leq N \leq 10^4$) e $M$ ($1 \leq M \leq 10^9$) indicando, respectivamente, o número de intervalos e o comprimento da faixa.

Nas próximas $N$ linhas, cada linha contém dois inteiros $L_i$ e $R_i$ ($0 \leq L_i <= R_i \leq M$) indicando os limites do intervalo $i$.


---

## Saída

Imprima um único inteiro, indicando a menor quantidade de intervalos necessários para cobrir toda a faixa de comprimento $M$. Caso não seja possível cobrir toda a faixa, imprima -1.

---

## Exemplos

### Exemplo 1

**Entrada:**
```text
4 10
0 5
3 10
2 6
1 3
```

**Saída:**
```text
2
```

---

### Exemplo 2

**Entrada:**
```text
3 10
0 2
4 6
6 10
```

**Saída:**
```text
-1
```

---
