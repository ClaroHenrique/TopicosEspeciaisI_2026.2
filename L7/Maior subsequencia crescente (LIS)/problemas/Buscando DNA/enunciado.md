# Estudando DNA

O famoso pesquisador em genética dr. Gen Omio está estudando sequências de DNA e quer formar padrões específicos nelas.

Uma sequência de DNA é composta por nucleotídeos representados pelas letras A, C, G e T. Dado uma sequência S de DNA, ele quer remover o menor número de letras sem alterar a ordem das lestras restantes, tal que a sequência resultante esteja ordenada alfabeticamente.

Por exemplo, a sequência de DNA "GATCGATT" pode ser transformada na subsequência crescente "ACGTT" removendo somente 3 letras. Ajude o dr. encontrando o menor número de letras necessárias para serem removidas.


## Entrada
* A primeira linha contém uma string $S$ representando a sequência de DNA.

## Saída
Imprima um único inteiro: o menor número de letras que precisam ser removidas para que a sequência de DNA esteja em ordem crescente.

## Restrições
* Tamanho de S é no máximo $2 \cdot 10^5$.
* S consiste apenas nas letras A, C, G e T.

## Exemplo 1

### Entrada:
```text
GATCGATT
```

### Saída:
```text
3
```
## Exemplo 2

### Entrada:
```text
AACCGGTT
```

### Saída:
```text
0
```