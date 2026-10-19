# O pulo do sapo

![Figura de um sapo em um caminho de pedras da esquerda para direita. Na primeira pedra se encontra um sapo, na ultima se encontra uma mosca](midia/sapo_lagoa.png)

Giribe é um sapo que vive faminto, mas sempre encontra tempo para planejar sua próxima refeição com muito cuidado. Agora ele está em um pequeno lado em um caminho de pedras numeradas de 1 até N da esquerda para direita. O objetivo de Giribe é partir da pedra 1 e chegar na pedra N pulando de pedra em pedra. Como ele é muito meticuloso, ele precisa considerar todos os caminhos possíveis.

Porém essa tarefa não é tão simples, pois o sapo pode ser capaz de pular múltiplas pedras em um único salto, dependendo das condições da pedra atual (se ela está escorregadia, ele não consegue ir longe). Giribe sabe que, para cada pedra no caminho, há um valor $S_i$ que indica quantas pedras a frente ele consegue saltar a partir da posição $i$.

Por exemplo, se ele está na pedra número 2 e $S_2 = 3$ ele é capaz de alcançar as pedras 3, 4 e 5 em um único salto. Outro exemplo: se ele está na posição 5 e $S_5 = 0$, ele não consegue saltar para nenhuma pedra.

Ajude Giribe calculando o número de caminhos possíveis da pedra 1 até a pedra N. Como essa resposta pode ser muito grande, imprima esse número módulo $10^9+7$. 


## Entrada

A primeira linha consiste em um inteiro N ($2 \le N \le 2 \cdot 10^5$), indicando o número de pedras no caminho do sapo.

Na segunda linha, há N inteiros $S_1, S_2, \dots, S_N$, onde $S_i$ ($0 \le S_i \le N$) indica quantas pedras à frente o sapo consegue saltar a partir da pedra $i$.


## Saída

Imprima o número de caminhos possíveis que o sapo Giribe pode seguir da pedra 1 até a pedra N.


## Exemplo

### Entrada:
```text
5
2 3 2 0 0
```

### Saída:
```text
3
```