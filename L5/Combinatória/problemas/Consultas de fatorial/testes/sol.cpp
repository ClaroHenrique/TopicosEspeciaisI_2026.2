#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
const int MOD = 1000000007;

int fat[MAXN + 1];

// Pré-computação dos fatoriais de 0 a 10^6 modulo 10^9 + 7
void precomputar() {
    fat[0] = 1; // 0! = 1
    for (int i = 1; i <= MAXN; i++) {
        fat[i] = (1LL * fat[i - 1] * i) % MOD;
    }
}

int main() {
    // Otimização de entrada e saída em C++
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precomputar();

    int Q;
    if (cin >> Q) {
        while (Q--) {
            int N;
            cin >> N;
            cout << fat[N] << "\n";
        }
    }

    return 0;
}