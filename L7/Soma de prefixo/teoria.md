## Soma de prefixo 

A soma de prefixo (prefix sum) é uma estrutura de dados relativamente simples, mas muito poderosa comum na programação competitiva. Dado um vetor, essa estrutura calcula a soma dos elementos de qualquer intervalo em $O(1)$.

Dado um vetor original $A$, criamos um outro vetor auxiliar $P$ de mesmo tamanho onde $P[i]$ armazena a soma de todos os elementos do início do vetor até a posição $i$. Ou seja: $P[i] = A[0] + A[1] + ... + A[i]$.

Por exemplo:

$A = [2, 5, -3, 8, 0]$

$P = [2, 7, 4, 12, 12]$.

Agora a pergunta é: dado o vetor $A$ e seu prefix sum $P$, como calcular a soma dos elementos no intervalo de $L$ até $R$ em $O(1)$?

A resposta é simples quando $L = 0$, pois a soma é o próprio valor de $P[R]$. Para qualquer outro caso, temos que utilizar $P[R]$ e descartar a soma dos elementos que estão à esquerda desse intervalo, ou seja, removemos $P[L-1]$. Enfim, temos a seguinte definição:

$$
\text{soma}(A, L, R) = 
\begin{cases} 
P[R], & \text{se } L = 0 \\ 
P[R] - P[L-1], & \text{caso contrário}
\end{cases}
$$

## Implementação

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAXN = 100005;
int A[MAXN];
ll psum[MAXN];
int n;

// build O(n)
void build() {
    psum[0] = A[0];
    for (int i = 1; i < n; i++) {
        psum[i] = psum[i-1] + A[i];
    }
}

// consulta O(1)
ll soma(int l, int r) {
    if (l == 0) return psum[r];
    return psum[r] - psum[l-1];
}

int main() {
    
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }                                                 
    build();

    // A = [2, 5, -3, 8, 0]
    cout << soma(0, 2) << endl; // 4
    cout << soma(1, 4) << endl; // 10
}
```

## Observações

- A principal desvantagem dessa estrutura é que ela funciona para vetores estáticos, modificar um elemento pode requerer recalcular todo o prefix sum com complexidade O(n). 
- Há estruturas como a árvore de segmentos que são mais para atualizações.
- Alguns problemas podem ser resolvidos mais facilmente diretamente na prefix sum ao invés de utilizar o vetor original. Por exemplo, encontrar um intervalo cujo a soma é X.
- A ideia de prefix sum também pode ser estendida para matrizes com duas ou mais dimensões.
- Provavelmente você deve utilizar o long long para prefix sum.

