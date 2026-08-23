# Pair

O pair é uma estrutura de dados que permite armazenar dois valores em uma variável apenas, podendo ser de tipos diferentes. Podemos dessa forma armazenar um par de valores.

## Declaração

Para declarar um par, você pode usar o tipo `pair<T1, T2>` onde `T1` e `T2` são os tipos dos dois valores:

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    // Par com dois inteiros
    pair<int, int> p1 = {5, 10};
    // Par com um inteiro e uma string
    pair<int, string> p2 = {5, "hello"};
}
```

## Acesso

Você pode acessar os elementos do par utilizando os membros `first` e `second`:

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    pair<int, int> p = make_pair(5, 10);
    cout << p.first << endl;  // Imprime 5
    cout << p.second << endl; // Imprime 10
}
```

Também é muito comum se usar um macro (comando para substituir texto no código antes de compilar) para facilitar o acesso aos elementos do par, como por exemplo:

```cpp
#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second

int main(){
    pair<int, int> p = {5, 10};
    cout << p.F << endl;  // Imprime 5
    cout << p.S << endl; // Imprime 10
}
```


## Modificação

Você pode modificar os elementos do par diretamente:

```cpp
#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second

int main(){
    pair<int, int> p = {5,10};
    p.F = 7;
    p.S = 15;
}
```

## Ordenação

A ordenação do `vector` também funciona para elementos do tipo `pair`. Nesse caso, os elementos são primeiro ordenados pelo `first` e, em caso de empate, o `second` é utilizado para ordenar:


```cpp
#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second

int main(){
    vector<pair<int,int>> V(4);
    V[0] = {1, 42};
    V[1] = {2, 32};
    V[2] = {1, 16};
    V[3] = {2, 80};
    // V = [{1,42}, {2,32}, {1,16}, {2,80}]

    sort(V.begin(), V.end());
    // V = [{1,16}, {1,42}, {2,32}, {2,80}]

    for(int i = 0; i < V.size(); i++){
        cout << "(" << V[i].F << ", " << V[i].S << ")" << endl;
    }
}
```
