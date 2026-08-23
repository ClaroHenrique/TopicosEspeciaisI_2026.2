# Bora Bora
Fonte: Maratona de programação 2008 fase 2: [https://maratona.sbc.org.br/hist/2008/contest2008_v2.pdf](https://maratona.sbc.org.br/hist/2008/contest2008_v2.pdf)

Observação: Esse é um problema mais chato que a média.

Bora Bora é um jogo de cartas simples para crianças, inventado na Ilha do Pacífico Sul de mesmo nome. Dois ou mais jogadores podem jogar, usando um baralho de cartas padrão. As cartas têm os valores usuais: Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete, Dama e Rei. Cada carta também tem um de quatro naipes: Paus , Ouros , Copas e Espadas .

Os jogadores sentam-se em círculo ao redor da mesa e jogam por turnos. O próximo jogador a jogar pode ser o da esquerda (sentido horário) ou o da direita (sentido anti-horário) do jogador atual, dependendo das cartas jogadas, como veremos. No início, a direção do jogo é no sentido horário.

O baralho é embaralhado e cada jogador recebe uma mão de cartas. O restante do baralho é colocado virado para baixo na mesa; esta é chamada de pilha de saque. Então, a primeira (a mais de cima) carta é removida da pilha de saque e colocada na mesa, virada para cima, iniciando outra pilha, chamada de pilha de descarte.

O objetivo do jogo é que um jogador descarte todas as suas cartas. A cada turno, um jogador descarta no máximo uma carta. Uma carta só pode ser descartada se tiver o mesmo valor ou o mesmo naipe que a carta do topo da pilha de descarte. Um jogador descarta uma carta colocando-a, virada para cima, na pilha de descarte (esta carta torna-se a do topo). Se um jogador não tiver uma carta adequada para descartar no seu turno, ele deve puxar uma carta da pilha de saque e adicioná-la à sua mão; se ele puder descartar essa carta, ele o faz, caso contrário, ele não faz mais nada e seu turno termina. Um jogador sempre descarta a carta de maior valor que puder. O valor de uma carta é determinado primeiro pelo seu valor da carta e depois pelo seu naipe. A ordem de valor é o próprio valor em si (Ás é o menor e o Rei é o maior), e a ordem dos naipes é, do menor para o maior, Paus, Ouros, Copas e Espadas. Portanto, a carta de maior valor é o Rei de Espadas e a de menor valor é o Ás de Paus. Como exemplo, uma Dama de Ouros tem um valor maior do que um Valete (qualquer naipe), mas tem um valor menor que uma Dama de Copas.

Algumas das cartas descartadas afetam o jogo da seguinte maneira:

* quando uma Dama é descartada, a direção do jogo é invertida: se a direção for horária, muda para anti-horária, e vice-versa;
* quando um Sete é descartado, o próximo jogador a jogar deve comprar duas cartas do monte de compra (o número de cartas na sua mão aumenta em duas), e perde a sua vez (não descarta nenhuma carta);
* quando um Ás é descartado, o próximo jogador a jogar deve comprar uma carta do monte de compra (o número de cartas na sua mão aumenta em uma), e perde a sua vez (não descarta nenhuma carta);
* quando um Valete é descartado, o próximo jogador a jogar perde a sua vez (não descarta nenhuma carta).

Note que a penalidade para a primeira carta no monte de descarte (a carta tirada do monte no início) é aplicada ao primeiro jogador a jogar. Por exemplo, se o primeiro jogador a jogar for $p$ e a primeira carta no monte de descarte for um Ás, o jogador $p$ compra uma carta do monte de compra e não descarta nenhuma carta no seu primeiro turno. Note também que se a primeira carta for uma Dama, a direção do jogo é invertida para anti-horária, mas o primeiro jogador a jogar continua sendo o mesmo.

O vencedor é o jogador que primeiro descarta todas as suas cartas (o jogo termina após o vencedor descartar sua última carta).

Dada a descrição do baralho embaralhado e o número de jogadores, escreva um programa para determinar quem vencerá o jogo.

### Entrada

A entrada contém vários casos de teste. A primeira linha de um caso de teste contém três inteiros **P**, **M** e **N**, separados por espaços simples, indicando respectivamente o número de jogadores ($2 \leq P \leq 10$), o número de cartas distribuídas para cada um dos jogadores no início do jogo ($1 \leq M \leq 11$) e o número total de cartas no baralho embaralhado ($3 \leq N \leq 300$). Cada uma das próximas N linhas contém a descrição de uma carta. Uma carta é descrita por um inteiro X e um caractere S, separados por um espaço, representando respectivamente o valor da carta e o naipe da carta. Os valores das cartas são mapeados para inteiros de 1 a 13 (Ás é 1, Valete é 11, Dama é 12 e Rei é 13). Os naipes das cartas são designados pela primeira letra do naipe (em inglês): 'C' (Clubs - Paus), 'D' (Diamonds / Ouros), 'H' (Hearts / Copas) ou 'S' (Spades / Espadas).

Os jogadores são identificados por números de 1 a P, e sentam-se em um círculo, no sentido horário, $1, 2 ... P, 1$. As primeiras P * M cartas do baralho são distribuídas aos jogadores: as primeiras M cartas para o primeiro jogador (jogador 1), as próximas M para o segundo jogador (jogador 2), e assim por diante. Após distribuir as cartas aos jogadores, a próxima carta no baralho — a (P * M + 1)-ésima carta — é usada para iniciar o monte de descarte, e as cartas restantes formam o monte de compra. A (P * M + 2)-ésima carta a aparecer na entrada é a carta do topo do monte de compra, e a última carta a aparecer na entrada (a N-ésima carta) é a carta de baixo do monte de compra (a última carta que pode ser comprada). O Jogador 1 é sempre o primeiro a jogar (mesmo quando a carta usada para iniciar o monte de descarte é uma Dama). Todos os casos de teste têm um vencedor, e em todos os casos de teste o número de cartas no baralho é suficiente para jogar até o final do jogo.

O final da entrada é indicado por uma linha contendo apenas três zeros, separados por espaços simples.
A entrada deve ser lida a partir da entrada padrão.

### Saída

Para cada caso de teste na entrada, seu programa deve imprimir uma única linha, contendo o número do jogador que vence o jogo.
A saída deve ser escrita na saída padrão.

### Exemplo de Entrada
```text
2 2 10
1 D
7 D
1 S
3 C
13 D
1 S
5 H
12 D
7 S
2 C
3 2 11
1 S
7 D
11 D
3 D
7 D
3 S
11 C
8 C
9 H
6 H
9 S
3 3 16
1 H
10 C
13 D
7 C
10 H
2 S
2 C
10 S
8 S
12 H
11 C
1 C
1 C
4 S
5 D
6 S
0 0 0
```

### Exemplo de Saída
```text
1
3
2
```