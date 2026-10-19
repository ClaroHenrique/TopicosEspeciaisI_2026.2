#include <bits/stdc++.h>
using namespace std;

int menorRecursivo(const vector<int>& v, int i) {
    if (i == v.size() - 1) return v[i];
    int menorDoResto = menorRecursivo(v, i + 1);
    return min(v[i], menorDoResto);
}

int main() {
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];

    cout << menorRecursivo(v, 0) << '\n';
    return 0;
}
