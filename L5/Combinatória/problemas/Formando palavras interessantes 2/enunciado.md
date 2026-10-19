# Formando palavras interessantes 2

## Descrição

Jãozinho é uma criança muito agitada e adora inventar brincadeiras com palavras. Ele percebeu que, se ele pegar uma palavra e reordenar suas letras (trocar zero, uma ou mais letras de posição), ele consegue gerar novas palavras interessantes.

Por exemplo, ao reordenar algumas letras da palavra "galo", temos:

"galo" -> "galo"
"galo" -> "gola"
"galo" -> "algo"
"galo" -> "aolg"

No entanto ele está aprendendo outro conceito que achou muito confuso: palavras no plural. Para simplificar, ele considera que uma palavra é plural se ela termina com a letra "s". Note que nem sempre isso é verdade no português (ex: ônibus, quaisquer).

Agora, Jãozinho quer contar a quantidade de palavras no **plural** que ele consegue formar reordenando uma palavra P.


## Entrada

Uma palavra P de no máximo 20 caracteres, constituída apenas de caracteres minúsculos do alfabeto.

## Saída

Imprima um único inteiro, indicando o número de palavras no plural distintas possíveis que podem ser geradas através da reordenação de P.


## Exemplos

### Exemplo 1

**Entrada:**
```text
asa
```

**Saída:**
```text
1
```

Explicação: a única palavra no plural que pode ser formada é "aas".


### Exemplo 2

**Entrada:**
```text
araras
```

**Saída:**
```text
10
```

Explicação: temos as palavras "aaarrs", "aarars", "aarras", "araars", "araras", "arraas", "raaars", "raaras", "raraas" e "rraaas".


### Exemplo 3

**Entrada:**
```text
mississippi
```

**Saída:**
```text
12600
```

