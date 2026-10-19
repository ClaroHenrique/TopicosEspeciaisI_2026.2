# Festival de Filmes

Fonte: CSES - [https://cses.fi/problemset/task/1629](https://cses.fi/problemset/task/1629)

## Descrição

Em um festival de cinema, $n$ filmes serão exibidos. Você sabe o horário de início e término de cada filme. Qual é o número máximo de filmes que você pode assistir por inteiro?

## Entrada

A primeira linha de entrada contém um número inteiro $n$: o número de filmes.

Depois disso, existem $n$ linhas que descrevem os filmes. Cada linha possui dois números inteiros $a$ e $b$: os horários de início e término de um filme.

## Saída

Imprima um único inteiro: o número máximo de filmes.

## Restrições

* $1 \le n \le 2 \cdot 10^5$
* $1 \le a < b \le 10^9$

## Exemplo

**Entrada:**
```text
3
3 5
4 9
5 8
```

**Saída:**
```text
2
```