# Time dos poderosos - Versão fácil

Essa versão "fácil" difere da original apenas no tamanho dos números de entrada N e K, que são menores.

## Descrição do Problema

O sr Jurandilson é o treinador de futebol de uma escola municipal e esse ano ele pretende fazer de tudo para vencer a competição de sua cidade. Para montar o melhor time, ele anotou o nível de habilidade de cada um de seus N estudantes. Jurandilson pretende montar um time com exatamente K jogadores, de forma que a soma dos níveis de habilidade dos jogadores desse time seja a maior possível.

Além disso, ele quer se planejar para possíveis substituições durante o campeonato. Ele precisa ter o número de formas distintas que ele pode formar um time com a soma máxima de habilidade.


## Entrada

A primeira linha contém dois inteiros $N$ e $K$ ($1 \le K \le N \le 20$), representando o número de estudantes e o tamanho do time, respectivamente.

A segunda linha contém $N$ inteiros $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$), representando o nível de habilidade de cada estudante.

## Saída

Imprima duas linhas, a primeira com a soma máxima de habilidade do time e a segunda com o número de formas distintas de formar um time com essa soma máxima. É garantido que a resposta cabe em um inteiro de 64 bits.            

## Exemplo de Entrada 1

```text
5 3
10 20 30 40 50
```

## Exemplo de Saída 1

```text
120
1
```

*Explicação:* Há apenas uma forma de formar um time com soma máxima de habilidade: $(A_3, A_4, A_5)$, que tem soma de habilidade igual a 120.


## Exemplo de Entrada 2

```text
5 3
10 50 30 30 50

```

## Exemplo de Saída 2

```text
130
2
```

*Explicação:* Há duas formas de formar um time com soma máxima de habilidade: $(A_2, A_3, A_5)$ e $(A_2, A_4, A_5)$, ambos os times têm soma de habilidade igual a 130.
