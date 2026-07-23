# Máquina de Escrever

Joseph é um escritor a moda antiga que gosta de escrever seus livros na boa e velha máquina de escrever. Como ele vai viajar e não tem muito espaço na mala, ele lhe contratou para desenvolver um aplicativo de celular que simula a máquina de escrever.

O aplicativo inicia o texto vazio e possui as seguintes funcionalidades:
1. `escrever <caractere>`: insere o caractere no final do texto.
2. `espaco`: insere um espaço no final do texto.
3. `apagar`: remove o último caractere no texto.
4. `fim`: mostra o texto digitado e encerra o programa.

## Entrada

Uma sequência de comandos separados um por linha, que podem ser:
* `escrever <caractere>`
* `espaco`
* `apagar`
* `fim`

É garantido que o comando `fim` será o último comando da entrada.

## Saída

Seu programa deve imprimir o texto digitado após todas as operações.


## Restrições

* O número de operações é menor que 100.

## Exemplo

```
Entrada:
escrever b
escrever o
escrever m
espaco
escrever d
escrever i
escrever a
escrever !
escrever !
apagar
fim

Saída:
bom dia!
```

<!-- TODO: centralizar imagem -->
