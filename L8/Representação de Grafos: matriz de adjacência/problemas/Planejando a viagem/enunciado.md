# Planejando a viagem

![Imagens de pontos turísticos do Ceará](midia/pontos_turisticos.png)

João da Silva e Maria da Silva estão planejando uma viagem juntos por todo o Ceará. Eles planejam passar por várias cidades numeradas de 1 a N durante a viagem e, as vezes, até passar pelo mesmo local mais de uma vez. 

Para ajudar no planejamento, eles anotaram as distâncias entre todas as N cidades que pretendem visitar em uma tabela com N linhas e N colunas. A célula na linha i e  na coluna j indica a distância entre a cidade i e a cidade j.

Eles também anotaram um percurso de tamanho M, com uma sequência de cidades que pretendem visitar nessa ordem. Sua tarefa é calcular a distância total que eles percorrerão seguindo esse percurso.


---

## Entrada

A primeira linha contém um inteiro N, indicando o número de cidades.
Em seguida, há uma matriz de inteiros D de N linhas e N colunas, onde $D[i][j]$ indica a distância entre a cidade i e a cidade j.
Na linha seguinte, há uma linha contendo um inteiro M, indicando o tamanho do percurso.
Na última linha, há uma sequência de M inteiros representando as cidades que serão visitadas na ordem em que aparecem.


## Saída

A saída deve ser um único inteiro indicando distância total do percurso.

## Restrições

- $2 \le N \le 500$
- $1 \le M \le 10^5$
- $0 \le D[i][j] \le 10^9$

## Exemplo

### Entrada:
```text
3
0 2 4
2 0 1
4 1 0
4
1 2 3 1

```

### Saída:
```text
7
```