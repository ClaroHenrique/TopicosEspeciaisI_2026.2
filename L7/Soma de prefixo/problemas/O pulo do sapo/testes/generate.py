import os
import random

MOD = 10**9 + 7

def resolver(n, s):
    """Calcula o número de caminhos em O(N) para gerar a saída correta."""
    if n == 1:
        return 1
    
    dp = [0] * (n + 1)
    diff = [0] * (n + 2)
    
    dp[1] = 1
    current_active = 0
    
    for i in range(1, n + 1):
        if i > 1:
            current_active = (current_active + diff[i]) % MOD
            dp[i] = current_active
        else:
            dp[1] = 1
            current_active = 0
            
        if dp[i] == 0 and i > 1:
            continue
            
        jump = s[i-1]
        if jump > 0 and i < n:
            left = i + 1
            right = min(n, i + jump)
            if left <= right:
                val = dp[i]
                diff[left] = (diff[left] + val) % MOD
                diff[right + 1] = (diff[right + 1] - val + MOD) % MOD
                
    return dp[n]

def criar_caso(indice, n, s):
    """Salva os arquivos indice.in e indice.out"""
    # Cria o conteúdo de entrada
    conteudo_in = f"{n}\n" + " ".join(map(str, s)) + "\n"
    
    # Calcula a resposta
    resposta = resolver(n, s)
    conteudo_out = f"{resposta}\n"
    
    # Escreve nos arquivos
    with open(f"{indice}.in", "w") as f:
        f.write(conteudo_in)
        
    with open(f"{indice}.out", "w") as f:
        f.write(conteudo_out)
    
    print(f"Caso {indice} gerado com sucesso! (N={n}, Resposta={resposta})")

def main():
    # Definindo os Casos de Teste (Edge Cases + Aleatórios)
    casos = []
    
    # 1. Edge Case: Menor N possível (N = 2)
    casos.append((2, [1, 1]))
    
    # 2. Edge Case: Impossível chegar ao fim (Sapo travado logo no início)
    casos.append((5, [3, 2, 1, 0, 5]))
    
    # 3. Edge Case: Salto gigante logo na primeira pedra (chega direto ao fim)
    casos.append((5, [5, 1, 1, 1, 0]))
    
    # 4. Caso maior (N = 100) com saltos moderados
    random.seed(42) # Para reprodutibilidade
    n_medio = 100
    s_medio = [random.randint(1, 10) for _ in range(n_medio)]
    s_medio[-1] = 0
    casos.append((n_medio, s_medio))

    # 5. Caso maior (N = 1000) com saltos aleatórios
    random.seed(42) # Para reprodutibilidade
    n_medio = 1000
    s_medio = [random.randint(0, n_medio) for _ in range(n_medio)]
    casos.append((n_medio, s_medio))


    # 6. Caso maior (N = 10000) com saltos aleatórios
    random.seed(42) # Para reprodutibilidade
    n_medio = 10000
    s_medio = [random.randint(0, n_medio) for _ in range(n_medio)]
    casos.append((n_medio, s_medio))


    # 7. Caso maior (N = 80000) com saltos aleatórios
    random.seed(42) # Para reprodutibilidade
    n_medio = 80000
    s_medio = [random.randint(n_medio//2, n_medio) for _ in range(n_medio)]
    casos.append((n_medio, s_medio))
    
    # 8. Caso grande (N = 200.000 - Limite máximo do problema)
    n_grande = 200000
    s_grande = [random.randint(1, n_grande) for _ in range(n_grande)]
    casos.append((n_grande, s_grande))

    # Gerando os arquivos físicos
    for idx, (n, s) in enumerate(casos, start=1):
        criar_caso(idx, n, s)

if __name__ == "__main__":
    main()