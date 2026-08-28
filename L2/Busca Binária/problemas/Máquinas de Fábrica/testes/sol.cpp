#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Função que verifica se é possível produzir pelo menos 't' produtos no tempo 'm'
bool check(long long m, const vector<long long>& k, long long t) {
    long long total_products = 0;
    for (long long time_per_item : k) {
        total_products += m / time_per_item;
        // Evita overflow desnecessário se já atingimos a meta
        if (total_products >= t) {
            return true;
        }
    }
    return total_products >= t;
}

int main() {
    // Otimização de I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long t;
    if (!(cin >> n >> t)) return 0;

    vector<long long> k(n);
    long long min_k = 1e18;
    for (int i = 0; i < n; ++i) {
        cin >> k[i];
        min_k = min(min_k, k[i]);
    }

    long long low = 1;
    long long high = min_k * t;
    long long ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;

        if (check(mid, k, t)) {
            ans = mid;         // Tenta encontrar um tempo menor
            high = mid - 1;
        } else {
            low = mid + 1;     // Precisa de mais tempo
        }
    }

    cout << ans << "\n";

    return 0;
}
