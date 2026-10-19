## Consultas em intervalos

Muitos problemas da maratona envolvem diretamente ou indiretamente responder um grande número de certos tipos de consultas dentro de intervalos.


Dado um vetor e uma série de consultas, onde cada consulta corresponde a um intervalo (dois índices L,R), queremos saber informações do tipo: qual a soma dos elementos nesse intervalo? qual o maior ou menor elemento desse intervalo? quantos elementos distintos temos no intervalo?

Estamos interessados em resolver consultas de forma muito eficiente usando uma estrutura de dados apropriada para cada tipo de operação.

Em geral, temos dois tipos de operação: 
* **query**: queremos coletar a informação.
* **update**: queremos atualizar elementos.
* **build**: pré-processamento antes que a estrutura possa ser utilizada.

Na próxima lição, veremos o prefix sum, uma estrutura capaz de responder qual a soma dos elementos dentro de um intervalo de um vetor em $O(1)$, mas possui complexidade do build de $O(n)$ e alterar um elemento dessa estrutura tem complexidade $O(n)$. 









