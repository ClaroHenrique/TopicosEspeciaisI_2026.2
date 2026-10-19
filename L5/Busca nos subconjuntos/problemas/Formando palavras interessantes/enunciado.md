# Formando palavras interessantes


## Descrição

Jãozinho é uma criança muito nova mas também muito sabida, ele já aprendeu a ler e escrever e agora está brincando com as palavras. Ele percebeu que, se ele pegar uma palavra e remover alguns caracteres sem alterar a ordem dos caracteres restantes, ele consegue gerar novas palavras interessantes.

Por exemplo, ao remover alguns caracteres da palavra "casamentos", temos:

"casa~~mentos~~" -> "casa"

"~~casa~~mentos" -> "mentos"

"c~~asam~~ent~~o~~s" -> "cents"

"~~c~~a~~s~~a~~m~~e~~nt~~o~~s~~" -> "aaeo"


Após essa descoberta, ele quer encontrar todas encontrar todas as palavras interessantes que ele consegue formar usando uma palavra P. Sua tarefa é ajudar Jãozinho construindo um programa que gera todas as palavras distintas que podem ser geradas seguindo esse processo através de uma palavra inicial P. Note que não se deve considerar remover todos os caracteres ou remover nenhum.


## Entrada

Uma palavra P de no máximo 12 caracteres, constituída apenas de caracteres minúsculos do alfabeto. 

## Saída

Imprima, em ordem alfabética, todas as palavras distintas possíveis que podem ser geradas através de P.


## Exemplos

### Exemplo 1

**Entrada:**
```text
abc
```

**Saída:**
```text
a
ab
ac
b
bc
c
```


### Exemplo 2

**Entrada:**
```text
aaaa
```

**Saída:**
```text
a
aa
aaa
```