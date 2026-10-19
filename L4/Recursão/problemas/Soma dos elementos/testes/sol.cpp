#include <bits/stdc++.h>
using namespace std;

long long somaRecursiva(const vector<int>& v, int i) {
    if (i == v.size() - 1) return v[i];
    return v[i] + somaRecursiva(v, i + 1);
}

int main() {
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];

    cout << somaRecursiva(v, 0) << '\n';
    return 0;
}
