# Juiz Online

Resolver problemas de programação competitiva geralmente envolve os seguintes passos:

1. Ler e entender o enunciado do problema;
2. Pensar em uma solução;
3. Implementar a solução em código;
4. Testar o código localmente com alguns exemplos;
5. Submeter o código para avaliação do juiz online.

O juiz online é um sistema que recebe o código enviado, compila e o executa com uma série de casos de teste. Cada caso de teste é composto por uma entrada e uma saída esperada (semelhante às questões de FUP no Moodle).

Ao enviar uma submissão, o juiz online sua solução pode receber um dos seguintes vereditos:

* **Accepted (AC)**: sua solução passou em todos os casos de teste;
* **Wrong Answer (WA)**: sua solução gerou uma saída incorreta em pelo menos um caso de teste;
* **Time Limit Exceeded (TLE)**: sua solução está lenta e demorou mais do que o tempo limite;
* **Runtime Error (RE)**: Seu código possui um erro que gera problemas durante a execução dos testes. Erros comuns incluem divisão por 0, ultrapassar o limite de memória e acesso indevido à memória;
* **Compilation Error (CE)**: Seu código não compilou. É raro, mas já aconteceu comigo de  enviar o arquivo errado ou escolher a linguagem errada.

Note que não basta seu programa dar a resposta correta, é preciso também que seja uma solução rápida o suficiente para passar nos testes no tempo limite. Geralmente deixar a solução rápida é a parte mais difícil da maratona.

Na Maratona de Programação, a equipe que conseguir resolver o maior número de problemas com AC vence. Em caso de empate no número de questões, o menor tempo de resolução é utilizado como critério de desempate. Cuidado! Submissões com veredito WA, TLE e RE geram uma penalidade de 20 minutos.


