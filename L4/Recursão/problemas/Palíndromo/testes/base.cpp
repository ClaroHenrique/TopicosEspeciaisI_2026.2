#include <bits/stdc++.h>
using namespace std;

// Nota: a string s é passada por referência,
// pois, por padrão strings e vectors são passados por cópia (O(n)).
// Dessa forma, evitamos um algoritmo O(n²) e conseguimos um O(n).
bool ehPalindromo(int i, int j, string &s) {
    // Implemente aqui
}

int main() {
    string s;
    cin >> s;

    if (ehPalindromo(0, s.size() - 1, s)) {
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }

    return 0;
}
