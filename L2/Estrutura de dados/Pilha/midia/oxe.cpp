
#include <bits/stdc++.h>
using namespace std;

int main() {
    stack<int> pilha; // pilha: []>

    pilha.push(1); // pilha: [1]>
    pilha.push(2); // pilha: [1, 2]>
    pilha.push(3); // pilha: [1, 2, 3]>

    cout << "Topo da pilha: " << pilha.top() << endl;
    // Saída: Topo da pilha: 3

    pilha.pop(); // pilha: [1, 2]>

    cout << "Topo da pilha" << pilha.top() << endl;
    // Saída: Topo da pilha: 2

    pilha.push(4); // pilha: [1, 2, 4]>
    pilha.push(5); // pilha: [1, 2, 4, 5]>

    cout << "Topo da pilha: " << pilha.top() << endl;
    // Saída: Topo da pilha: 5

    cout << "Tamanho da pilha: " << pilha.size() << endl;
    // Saída: Tamanho da pilha: 4

    if(pilha.empty()) {
        cout << "A pilha está vazia" << endl;
    } else {
        cout << "A pilha não está vazia" << endl;
    }
    // Saída: A pilha não está vazia

    // Vamos esvaziar a pilha
    while(!pilha.empty()){
        pilha.pop();
    }
    // pilha: []>
    
    cout << "Tamanho da pilha: " << pilha.size() << endl;
    // Saída: Tamanho da pilha: 0
}