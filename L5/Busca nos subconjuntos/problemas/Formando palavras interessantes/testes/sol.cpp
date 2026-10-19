#include <bits/stdc++.h>

using namespace std;

vector<string> palavras;

// Gera todas as subsequências recursivamente testando incluir ou não cada caractere
void gerarSubsequencias(int i, string &p, string atual) {
    if (i == p.size()) {
        if (atual != "" && atual != p) {
            palavras.push_back(atual);
        }
        return;
    }

    // Opção 1: não incluir o caractere atual (remover caractere)
    gerarSubsequencias(i + 1, p, atual);

    // Opção 2: incluir o caractere atual
    gerarSubsequencias(i + 1, p, atual + p[i]);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string p;
    cin >> p;

    gerarSubsequencias(0, p, "");

    // Ordena
    sort(palavras.begin(), palavras.end());

    cout << palavras[0] << endl;
    for(int i = 1; i < palavras.size(); i++){
        if(palavras[i] != palavras[i-1]) cout << palavras[i] << endl;
    }

    return 0;
}