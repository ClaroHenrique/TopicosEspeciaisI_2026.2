#include <bits/stdc++.h>
using namespace std;

// Nota: a string s é passada por referência,
// pois, por padrão strings e vectors são passados por cópia, o que é ineficiente. Passando por referência, a função recebe um ponteiro para a string original, evitando cópias desnecessárias.
// Dessa forma, evitamos um algoritmo O(n²) e conseguimos um algoritmo O(n).
bool ehPalindromo(string &s, int i, int j) {
    int tam = j - i + 1;
    if(tam == 0 || tam == 1) return true;
    if(s[i] != s[j]) return false;
    return ehPalindromo(s, i + 1, j - 1);
}

int main() {
    string s;
    cin >> s;

    if (ehPalindromo(s, 0, s.size() - 1)) {
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }

    return 0;
}
