# Fila

A estrutura de dados `queue` representa uma fila, como as que vemos no dia a dia em bancos. Nessas filas, a pessoa que chega mais cedo é também a primeira a ser atendida e sair da fila, enquanto novas pessoas entram no final da fila.

Curiosamente, a fila é uma estrutura mais limitada que um vetor: ela permite apenas o acesso ao elemento que está no seu início. No entanto, graças a essa limitação ela permite realizar essas operações de forma bem eficiente.

A fila é uma coleção de elementos que tem a ideia de FIFO (First In, First Out). Ela possui três operações principais:

* `front()`: retorna o valor do elemento que está na frente da fila (foi inserido mais cedo).
* `push()`: insere um elemento no final da fila.
* `pop()`: remove o elemento que está na frente da fila.

Além dessas operações fundamentais, ela também dispõe do:
* `size()`: retorna a quantidade de elementos na fila.
* `empty()`: retorna `true` se a fila está vazia ou `false` caso contrário.
* `q = {}`: permite esvaziar a fila q.

Todas essas operações são realizadas em tempo constante $O(1)$, exceto esvaziar a fila.

## Declaração

Para declarar uma fila vazia, com zero elementos:

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    // fila vazia
    queue<int> q;
}
```

## Inserção

Você pode adicionar um elemento `x` no final da fila usando o método `push(x)`:

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    // Fila vazio
    queue<int> q;
    q.push(8);
    q.push(5);
    q.push(10);
}
```

Após a execução do código acima, a fila possui os elementos `[8, 5, 10]` (onde a frente da fila começa da esquerda). Você pode usar o método `empty()` para percorrer os elementos da fila e imprimi-los:

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    // Fila vazio
    queue<int> q;
    q.push(8);
    q.push(5);
    q.push(10);
    
    while(!q.empty()){
        cout << q.front() << endl;
        q.pop();
    }
    // Imprime os elementos na ordem: 8, 5, 10
}
```



