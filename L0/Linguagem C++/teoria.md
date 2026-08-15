# Linguagem C++

As linguagem C e C++ são as mais rápidas disponíveis para maratona. Soluções implementadas nas linguagens como Java e Python correm o risco de obter TLE apenas por causa da lentidão da linguagem.

Utilizamos a linguagem C++ pois além de ser rápida, também oferece uma biblioteca rica para programação competitiva. 

A biblioteca padrão, a STL contém implementações de:

* **Alocação dinâmica** (vetores que crescem de tamanho sozinhos);
* **Árvores balanceadas** (geralmente rubro-negras);
* **Filas de prioridade**;
* **Ordenação rápida**;
* **Pares** (ordenação já embutida);
* **Números complexos** (pontos 2D);
* **Geração de permutações**;
* **Geração de números aleatórios**;
* **Expressões regulares**;
* **Manipulação de strings** de forma dinâmica;
* **Entrada/Saída** mais concisa;



## Nosso cabeçalho

Nosso código normalmente vai começar da seguinte forma:

```cpp
#include <bits/stdc++> // importa tudo da STL
using namespace std; // evita ter que usar namespaces

int main(){
    //código
}
```

Se precisarmos de algo mais robusto, podemos adicionar:

```cpp
#include <bits/stdc++> // importa tudo da STL
using namespace std; // evita ter que usar namespaces

typedef long long ll; // apelidos para tipos de variáveis
const int INF = 1e9; // constantes
const int MAXN = 100010; // limites de tamanhos

// apelidos para tipos complexos
typedef pair<int,int> ii;
typedef vector<int> vi;

int main(){
    // entrada e saída mais rápidas
    ios_base::sync_with_stdio(0); cin.tie(0);

}
```
## Entrada e saída

Na maioria dos juízes online (ICPC, Codeforces, CSES, Beecrown, USACO, etc) utilizam a entrada e a saída que seguem o padrão (standard I/O).


A forma mais direta e simples é usar as funções `cin` e `cout` da biblioteca `<iostream>`:

* **Leitura com `cin`:** Chamar o operador de extração (`operator>>`) no `cin` lê dados da entrada padrão separados por espaços em branco (espaços, tabulações ou quebras de linha).
* **Escrita com `cout`:** Da mesma forma, chamar o operador de inserção (`operator<<`) no `cout` escreve os dados na saída padrão.
* **Quebra de linha:** O caractere `\n` ou comando `endl` representam uma nova linha.


Exemplo:

```cpp
#include <iostream>
using namespace std;

int main() {
	int a, b, c;
	cin >> a >> b >> c;
	cout << "Soma: " << a + b + c << "\n";
}
```

## Demais linguagens

Em alguns casos, podemos utilizar outras linguagens como Python e Java se precisarmos de um recurso bem específico. Algumas vezes eu utitilizo Python quando vejo que o problema é "simples" e envolve manipulação de inteiros grandes ou strings.