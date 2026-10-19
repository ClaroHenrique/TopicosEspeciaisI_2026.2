#include <bits/stdc++.h>
using namespace std;

int minimoTrocas(string &s, int i, int j) {
    if (i >= j) return 0;
    if (s[i] == s[j]) return minimoTrocas(s, i + 1, j - 1);
    return 1 + minimoTrocas(s, i + 1, j - 1);
}

int main() {
    string s;
    cin >> s;

    cout << minimoTrocas(s, 0, s.size() - 1) << '\n';
    return 0;
}
