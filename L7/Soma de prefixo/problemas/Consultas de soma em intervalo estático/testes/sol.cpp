#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Otimização de I/O para maior velocidade
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n >> q;

    // Utilizar long long para evitar overflow nas somas
    vector<long long> prefix(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        prefix[i] = prefix[i - 1] + x;
    }

    // Processamento de cada consulta em O(1)
    while (q--) {
        int a, b;
        cin >> a >> b;
        // A soma no intervalo [a, b] é prefix[b] - prefix[a - 1]
        long long ans = prefix[b] - prefix[a - 1];
        cout << ans << "\n";
    }

    return 0;
}