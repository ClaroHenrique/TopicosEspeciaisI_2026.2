#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> a;
vector<int> estagiarios;

// Função recursiva que constrói a hierarquia e identifica as folhas
// Retorna o índice do líder do intervalo [l, r]
int solve(int l, int r) {
    if (l > r) return -1;

    // Encontra o funcionário de maior poder no intervalo atual
    int max_idx = l;
    for (int i = l + 1; i <= r; ++i) {
        if (a[i] > a[max_idx]) {
            max_idx = i;
        }
    }

    // Subgrupos à esquerda e à direita
    int left_leader = solve(l, max_idx - 1);
    int right_leader = solve(max_idx + 1, r);

    // Se não gerou nenhum líder subordinado, é um estagiário (folha)
    if (left_leader == -1 && right_leader == -1) {
        estagiarios.push_back(a[max_idx]);
    }

    return max_idx;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N) || N == 0) {
        return 0;
    }

    a.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> a[i];
    }

    solve(0, N - 1);

    // Ordena os identificadores dos estagiários em ordem crescente
    sort(estagiarios.begin(), estagiarios.end());

    for (size_t i = 0; i < estagiarios.size(); ++i) {
        cout << estagiarios[i] << (i + 1 == estagiarios.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}