# Jogo das inversões

Fonte: Adaptado do Codeforces (casos de testes diferentes) - [https://codeforces.com/problemset/problem/327/A](https://codeforces.com/problemset/problem/327/A)

## Descrição do Problema

Iahub ficou entediado, então inventou um jogo para ser jogado no papel.

Ele escreve $n$ inteiros $a_1, a_2, \dots, a_n$. Cada um desses inteiros pode ser $0$ ou $1$. Ele tem permissão para fazer **exatamente uma jogada**: ele escolhe dois índices $i$ e $j$ ($1 \le i \le j \le n$) e inverte todos os valores $a_k$ cujas posições estão no intervalo $[i, j]$ (isto é, $i \le k \le j$). Inverter o valor de $x$ significa aplicar a operação $x = 1 - x$.

O objetivo do jogo é obter o **número máximo de uns ($1$s)** após exatamente uma jogada.

Escreva um programa para resolver o joguinho de Iahub.

---

## Entrada

A primeira linha da entrada contém um inteiro $n$ ($1 \le n \le 100$).  
A segunda linha da entrada contém $n$ inteiros: $a_1, a_2, \dots, a_n$. É garantido que cada um desses $n$ valores é $0$ ou $1$.

---

## Saída

Imprima um único inteiro: o número máximo de $1$ s que podem ser obtidos após exatamente uma jogada.

---

## Exemplos

### Exemplo 1

**Entrada:**
```text
5
1 0 0 1 0
```

**Saída:**
```text
4
```

---

### Exemplo 2

**Entrada:**
```text
4
1 0 0 1
```

**Saída:**
```text
4
```

---

## Notas

* **No primeiro caso de teste:** invertendo o segmento de $2$ a $5$ ($i = 2, j = 5$), a sequência se torna: `[1, 1, 1, 0, 1]`. Portanto, ela contém quatro uns. Não há como fazer toda a sequência ficar igual a `[1, 1, 1, 1, 1]`.
* **No segundo caso de teste:** invertendo apenas o segundo e o terceiro elemento ($i = 2, j = 3$), todos os números se tornam `1` (`[1, 1, 1, 1]`), resultando em $4$ uns.
