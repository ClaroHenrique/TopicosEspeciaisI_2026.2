#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long ll;

int n;
vector<ll> p;

ll solve(int idx, ll sum1, ll sum2) {
    if (idx == n) {
        return abs(sum1 - sum2);
    }

    // Coloca a maçã atual no grupo 1 ou no grupo 2
    ll op1 = solve(idx + 1, sum1 + p[idx], sum2);
    ll op2 = solve(idx + 1, sum1, sum2 + p[idx]);

    return min(op1, op2);
}

int main() {
    cin >> n;
    p.resize(n);

    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }

    cout << solve(0, 0, 0) << "\n";

    return 0;
}