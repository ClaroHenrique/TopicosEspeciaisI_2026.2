#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100100;

int v[MAXN];
int n;

int menor_rec(int i) {
    // Implemente aqui (use o vetor global)
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) cin >> v[i];

    cout << menor_rec(n-1) << '\n';
    return 0;
}
