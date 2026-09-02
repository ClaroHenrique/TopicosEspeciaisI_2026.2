# USB vs. PS/2

Fonte: Codeforces - [https://codeforces.com/problemset/problem/762/B](https://codeforces.com/problemset/problem/762/B)

## Descrição do Problema

Devido ao aumento no número de estudantes da Universidade Estadual de Berland, foi decidido equipar uma nova sala de informática. Você recebeu a tarefa de comprar mouses e deve gastar o mínimo possível. Afinal de contas, o país está em crise!

Os computadores comprados para a sala eram diferentes. Alguns deles tinham apenas portas USB, alguns apenas portas PS/2, e alguns tinham ambas as opções.

Você encontrou uma lista de preços de uma determinada loja de informática. Nela, para $m$ mouses, é especificado o custo e o tipo de porta necessária para conectar o mouse (USB ou PS/2). Cada mouse da lista pode ser comprado no máximo uma vez.

Você quer comprar um conjunto de mouses da lista de preços fornecida de forma a maximizar o número de computadores equipados com mouses (não é garantido que você conseguirá equipar todos os computadores) e, em caso de igualdade deste valor, você quer minimizar o custo total dos mouses que irá comprar.

## Entrada

A primeira linha contém três inteiros $a$, $b$ e $c$ ($0 \le a, b, c \le 10^5$) — o número de computadores que possuem apenas portas USB, o número de computadores que possuem apenas portas PS/2 e o número de computadores que possuem ambas as opções, respectivamente.

A linha seguinte contém um inteiro $m$ ($0 \le m \le 3 \cdot 10^5$) — o número de mouses na lista de preços.

As próximas $m$ linhas descrevem, cada uma, um mouse. A $i$-ésima linha contém primeiro um inteiro $val_i$ ($1 \le val_i \le 10^9$) — o custo do $i$-ésimo mouse, seguido pelo tipo de porta (USB ou PS/2) necessária para conectar o mouse.

## Saída

Imprima dois inteiros separados por espaço — o número de computadores equipados e o custo total dos mouses que você comprará.

## Exemplo

### Entrada
```text
2 1 1
4
5 USB
6 PS/2
3 PS/2
7 PS/2
```

### Saída
```text
3 14
```

## Nota

No primeiro exemplo, você pode comprar os três primeiros mouses. Dessa forma, você equipará um dos computadores que tem apenas uma porta USB com um mouse USB, e conectará os dois mouses PS/2 no computador com porta PS/2 e no computador com ambas as portas.
