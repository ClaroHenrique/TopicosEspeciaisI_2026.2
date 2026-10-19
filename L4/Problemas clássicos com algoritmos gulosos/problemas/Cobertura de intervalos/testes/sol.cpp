#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Estrutura para representar um intervalo
struct Interval {
    int l, r;
};

// Função de comparação para ordenar os intervalos
// Ordena pelo início (crescente). Em caso de empate, pelo fim (decrescente).
bool compareIntervals(const Interval& a, const Interval& b) {
    if (a.l != b.l) {
        return a.l < b.l;
    }
    return a.r > b.r;
}

int main() {
    // Otimização para acelerar a entrada e saída no C++
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    // Lê a quantidade de intervalos e o tamanho da faixa
    if (!(cin >> N >> M)) return 0;

    vector<Interval> intervals(N);
    for (int i = 0; i < N; ++i) {
        cin >> intervals[i].l >> intervals[i].r;
    }

    // Ordena os intervalos
    sort(intervals.begin(), intervals.end(), compareIntervals);

    int current_end = 0;
    int max_reach = 0;
    int count = 0;
    int i = 0;

    while (current_end < M) {
        bool found = false;
        
        while (i < N && intervals[i].l <= current_end) {
            if (intervals[i].r > max_reach) {
                max_reach = intervals[i].r;
                found = true;
            }
            i++;
        }

        if (!found) {
            break;
        }

        current_end = max_reach;
        count++;
    }

    if (current_end >= M) {
        cout << count << "\n";
    } else {
        cout << -1 << "\n";
    }

    return 0;
}