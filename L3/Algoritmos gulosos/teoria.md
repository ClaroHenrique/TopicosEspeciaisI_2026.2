# Algoritmos gulosos

Em muitos problemas, não precisamos buscar todas as soluções possíveis para resolver o problema. Até mesmo por que uma busca completa pode ser muito custosa computacionalmente.

A abordagem do algoritmo guloso consiste em construir de forma incremental uma única solução escolhendo a cada passo a opção que parece ser a melhor no momento

Algumas definições:

* **Problema de otimização**: é um problema que envolve encontrar a melhor solução entre várias possíveis. É preciso minimizar ou maximizar uma função objetivo.

* **Solução viável**: é uma solução que satisfaz todas as restrições do problema.

* **Solução vizinha**: é uma solução que pode ser obtida a partir de outra solução aplicando uma pequena modificação (Ex: trocar um elemento).

* **Solução ótima global**: é uma solução viável que é a melhor de todas de acordo com a função objetivo.

* **Solução ótima local**: é uma solução melhor que todas as suas soluções vizinhas.

O algoritmo guloso funciona quando a solução ótima local é também a solução ótima global. Nesse caso podemos construir uma solução aos poucos, tomando apenas decisões que são melhores no momento e sem precisar voltar atrás.  


## Cuidado!

Em muitos casos o algoritmo guloso não garante que a solução encontrada seja ótima e realizar uma prova formal que mostre a sua otimalidade é difícil. Na maratona, geralmente usamos a intuição para identificar se o problema é guloso. 

Algoritmos gulosos aparecem bastante como parte da solução de problemas maiores. Então é um tópico muito frequente.



## Problema do troco

Dado um valor $X$ centavos que precisa ser trocado em várias moedas e uma lista de tipos de moedas disponíveis com os seguintes valores: 1, 5, 10, 25, 50 e 100 centavos. Determine a quantidade mínima de moedas necessárias para pagar o valor $X$.

Por exemplo, o troco de 74 centavos é feito com 6 moedas: uma moeda de 50 centavos, duas moedas de 10 centavos e 4 moedas de 1 centavo. Já o troco de 250 centavos pode ser feito com 3 moedas (100, 100, 50).

Nesse caso, a ideia gulosa consiste em a cada passo, escolher a maior moeda disponível que seja menor ou igual ao que o troco. Após a escolha, subtraia o valor da moeda do valor e repita o processo.

Por exemplo, para o troco de 74 centavos e moedas de 1, 5, 10, 25, 50 e 100 centavos, temos:

* 74 - 50 = 24 (1 moeda de 50 centavos)
* 24 - 10 = 14 (1 moeda de 10 centavos)
* 14 - 10 = 4 (1 moeda de 10 centavos)
* 4 - 1 = 3 (1 moeda de 1 centavo)
* 3 - 1 = 2 (1 moeda de 1 centavo)
* 2 - 1 = 1 (1 moeda de 1 centavo)
* 1 - 1 = 0 (1 moeda de 1 centavo)

Essa solução é ótima para todos os valores de $X$. No entanto, não funciona para qualquer conjunto de moedas. Por exemplo, considere $X=6$ e as moedas do tipo 1, 3 e 4. Como veremos em um próximo assunto, há outra solução para qualquer conjunto de moedas.




