# Palíndromo recursivo

Uma string é chamada de palíndromo quando ela pode ser lida da mesma forma da esquerda para a direita e da direita para a esquerda.

Exemplos de palíndromos:

- `asa`
- `arara`
- `reviver`

Sua tarefa é completar uma função recursiva que verifique se uma string é palíndroma.

Definição recursiva de um palíndromo:

P = "", string vazia é um palíndromo.
P = c, string com um único caractere é um palíndromo.
P = c + P' + c, onde c é um caractere e P' é um palíndromo.

Ou seja, um palíndromo é uma string que começa e termina com o mesmo caractere, e o que está entre eles também é um palíndromo.

---

## Entrada

A primeira e única linha da entrada contém uma string $S$ formada por letras minúsculas do alfabeto, com tamanho entre $1$ e $1000$.

---

## Saída

Imprima:

- `S` se a string for um palíndromo;
- `N` caso contrário.

---

## Exemplos

### Exemplo 1

**Entrada:**
```text
arara
```

**Saída:**
```text
S
```

---

### Exemplo 2

**Entrada:**
```text
casa
```

**Saída:**
```text
N
```

---
