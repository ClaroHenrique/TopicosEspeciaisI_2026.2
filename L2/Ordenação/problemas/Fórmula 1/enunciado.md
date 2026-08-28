# Fórmula 1

Fonte: Maratona de Programação da SBC [https://maratona.sbc.org.br/hist/2010/primeira-fase/](https://maratona.sbc.org.br/hist/2010/primeira-fase/)

## Descrição

A temporada de Fórmula 1 consiste de uma série de corridas, conhecidas como Grandes Prêmios, organizados pela Federação Internacional de Automobilismo (FIA). Os resultados de cada Grande Prêmio são combinados para determinar o Campeonato Mundial de Pilotos. Mais especificamente, a cada Grande Prêmio são distribuídos pontos para os pilotos, dependendo da classificação na corrida. Ao final da temporada, o piloto que tiver somado o maior número de pontos é declarado Campeão Mundial de Pilotos.

Os organizadores da Fórmula 1 mudam constantemente as regras da competição, com o objetivo de dar mais emoção às disputas. Uma regra modificada para a temporada de 2010 foi justamente a distribuição de pontos em cada Grande Prêmio. Desde 2003 a regra de pontuação premiava os oito primeiros colocados, obedecendo a seguinte tabela:

| Colocação | 1º | 2º | 3º | 4º | 5º | 6º | 7º | 8º |
|:---------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Pontos** | 10 | 8 | 6 | 5 | 4 | 3 | 2 | 1 |

Ou seja, o piloto vencedor ganhava 10 pontos, o segundo colocado ganhava 8 pontos, e assim por diante.

Na temporada de 2010 os dez primeiros colocados receberão pontos, obedecendo a seguinte tabela:

| Colocação | 1º | 2º | 3º | 4º | 5º | 6º | 7º | 8º | 9º | 10º |
|:---------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
| **Pontos** | 25 | 18 | 15 | 12 | 10 | 8 | 6 | 4 | 2 | 1 |

A mudança no sistema de pontuação provocou muita especulação sobre qual teria sido o efeito nos Campeonatos Mundiais passados se a nova pontuação tivesse sido utilizada nas temporadas anteriores. Por exemplo, teria Lewis Hamilton sido campeão em 2008, já que a diferença de sua pontuação total para Felipe Massa foi de apenas um ponto? Para acabar com as especulações, a FIA contratou você para escrever um programa que, dados os resultados de cada corrida de uma temporada, determine o Campeão Mundial de Pilotos para sistemas de pontuações diferentes.

---

## Entrada

A entrada contém vários casos de teste.

- A primeira linha de um caso de teste contém dois números inteiros $G$ e $P$ separados por um espaço em branco, indicando respectivamente o número de Grandes Prêmios ($1 \le G \le 100$) e o número de pilotos ($1 \le P \le 100$). Os pilotos são identificados por inteiros de $1$ a $P$.
- Cada uma das $G$ linhas seguintes indica o resultado de uma corrida, e contém $P$ inteiros separados por espaços em branco. Em cada linha, o $i$-ésimo número indica a ordem de chegada do piloto $i$ naquela corrida (o primeiro número indica a ordem de chegada do piloto 1 naquela corrida, o segundo número indica a ordem de chegada do piloto 2 na corrida, e assim por diante).
- A linha seguinte contém um único número inteiro $S$ indicando o número de sistemas de pontuação ($1 \le S \le 10$).
- Cada uma das $S$ linhas seguintes contém a descrição de um sistema de pontuação. A descrição de um sistema de pontuação inicia com um inteiro $K$ ($1 \le K \le P$), indicando a última ordem de chegada que receberá pontos, seguido de um espaço em branco, seguido de $K$ inteiros $k_0, k_1, \dots, k_{K-1}$ ($1 \le k_i \le 100$) separados por espaços em branco, indicando os pontos a serem atribuídos (o primeiro inteiro indica os pontos do primeiro colocado, o segundo inteiro indica os pontos do segundo colocado, e assim por diante).

O final da entrada é indicado por uma linha contendo dois zeros separados por um espaço (`0 0`).

---

## Saída

Para cada sistema de pontuação da entrada, seu programa deve imprimir uma linha contendo o identificador do Campeão Mundial de Pilotos. Se houver mais de um Campeão Mundial de Pilotos (ou seja, se houver empate), a linha deve conter todos os Campeões Mundiais de Pilotos, em ordem crescente de identificador, separados por um espaço em branco.

---

## Exemplo

### Exemplo de Entrada

```text
1 3
3 2 1
3
3 5 3 2
3 5 3 1
3 1 1 1
3 10
1 2 3 4 5 6 7 8 9 10
10 4 3 1 2 5 8 7 6 9
9 10 1 2 3 4 5 6 7 8
2
5 5 4 3 2 1
3 10 5 1
2 4
1 3 4 2
4 1 3 2
2
1 3
3 5 4 2
0 0
```

### Exemplo de Saída

```text
3
3
1 2 3
3
3
2 4
4
```