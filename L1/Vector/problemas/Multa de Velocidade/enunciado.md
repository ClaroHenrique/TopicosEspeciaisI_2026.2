# Multa de velocidade
Fonte: USACO [https://usaco.org/index.php?page=viewproblem2&cpid=568](https://usaco.org/index.php?page=viewproblem2&cpid=568)

Sempre uma encrenqueira, a vaca Bessie roubou o trator do Fazendeiro John e saiu em disparada pela estrada!

A estrada tem exatamente 100 milhas de extensão, e Bessie percorre toda a extensão da estrada antes de ser finalmente parada por um policial, que aplica a Bessie uma multa por excesso de velocidade, por estar com a carteira de motorista vencida e por operar um veículo motorizado sendo uma vaca. Embora Bessie admita que as duas últimas multas sejam provavelmente válidas, ela questiona se o policial estava correto ao emitir a multa por excesso de velocidade, e quer determinar por si mesma se ela realmente dirigiu acima do limite de velocidade em algum trecho de sua jornada.

A estrada é dividida em $N$ segmentos, cada um descrito por um comprimento inteiro positivo em milhas, bem como um limite de velocidade inteiro na faixa de $1 \dots 100$ milhas por hora. Como a estrada tem 100 milhas de extensão, a soma dos comprimentos de todos os $N$ segmentos é igual a 100. Por exemplo, a estrada pode começar com um segmento de comprimento 45 milhas, com limite de velocidade de 70, e terminar com um segmento de comprimento 55 milhas, com limite de velocidade de 60.

A jornada de Bessie também pode ser descrita por uma série de segmentos, $M$ deles. Durante cada segmento, ela viaja por um determinado número inteiro positivo de milhas, a uma determinada velocidade inteira. Por exemplo, ela pode começar viajando 50 milhas a uma velocidade de 65, e depois outras 50 milhas a uma velocidade de 55. A soma dos comprimentos de todos os $M$ segmentos é igual a 100 milhas no total. O trator do Fazendeiro John pode atingir no máximo 100 milhas por hora.

Dadas as informações acima, por favor determine a quantidade máxima acima do limite de velocidade que Bessie atinge durante qualquer parte de sua jornada.

### FORMATO DE ENTRADA:

A primeira linha da entrada contém $N$ e $M$, separados por um espaço.

As próximas $N$ linhas contêm, cada uma, dois inteiros descrevendo um segmento de estrada, indicando seu comprimento e limite de velocidade.

As próximas $M$ linhas contêm, cada uma, dois inteiros descrevendo um segmento da jornada de Bessie, indicando o comprimento e também a velocidade na qual Bessie estava dirigindo.

### FORMATO DE SAÍDA:

Por favor, imprima uma única linha contendo a quantidade máxima acima do limite de velocidade que Bessie dirigiu durante qualquer parte de sua jornada. Se ela nunca exceder o limite de velocidade, imprima 0.

### EXEMPLO DE ENTRADA:
```text
3 3
40 75
50 35
10 45
40 76
20 30
40 40
```

### EXEMPLO DE SAÍDA:
```text
5
```

Neste exemplo, a estrada contém três segmentos (40 milhas a 75 milhas por hora, seguidas por 50 milhas a 35 milhas por hora, e depois 10 milhas a 45 milhas por hora). Bessie dirige por três segmentos (40 milhas a 76 milhas por hora, 20 milhas a 30 milhas por hora e 40 milhas a 40 milhas por hora). Durante seu primeiro segmento, ela está ligeiramente acima do limite de velocidade, mas seu último segmento é a pior infração, durante parte da qual ela está 5 milhas por hora acima do limite de velocidade. A resposta correta é, portanto, 5.
