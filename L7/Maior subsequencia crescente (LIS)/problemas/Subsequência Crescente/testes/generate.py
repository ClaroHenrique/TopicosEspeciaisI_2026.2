import os
import random

MOD = 10**9 + 7

def resolver(n, s):
    # calcula maior subsequência crescente
    if n == 1:
        return 1
    
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if s[i] > s[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

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
    
    casos.append((6, [100, 30, 50, 40, 60, 80]))
    
    casos.append((10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    
    casos.append((10, [13, 8, 3, 8, 1, 5, 10, 5, 8, 10]))
    
    # 4. Caso maior (N = 100) com saltos moderados
    random.seed(42) # Para reprodutibilidade
    n_medio = 100
    s_medio = [random.randint(1, 10) for _ in range(n_medio)]
    s_medio[-1] = 0
    casos.append((n_medio, s_medio))

    # 5. Caso maior (N = 1000) com saltos aleatórios
    random.seed(42) # Para reprodutibilidade
    n_medio = 1000
    s_medio = [random.randint(0, 10**9) for _ in range(n_medio)]
    casos.append((n_medio, s_medio))


    # 6. Caso maior (N = 5000) com saltos aleatórios
    random.seed(42) # Para reprodutibilidade
    n_medio = 5000
    s_medio = [random.randint(0, 10**9) for _ in range(n_medio)]
    casos.append((n_medio, s_medio))


    # Gerando os arquivos físicos
    for idx, (n, s) in enumerate(casos, start=1):
        criar_caso(idx, n, s)

if __name__ == "__main__":
    main()