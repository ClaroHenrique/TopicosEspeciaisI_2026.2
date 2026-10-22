import random
import os

def resolver(n, matriz, m, percurso):
    """
    Resolve o problema dado N, a matriz de distâncias (1-indexed),
    M e a lista de percurso (1-indexed).
    """
    distancia_total = 0
    for i in range(m - 1):
        u = percurso[i] - 1  # Ajustando para índice 0
        v = percurso[i + 1] - 1
        distancia_total += matriz[u][v]
    return distancia_total


def gerar_matriz(n, min_d=0, max_d=10**9, simetrica=True):
    """Gera uma matriz de distâncias N x N."""
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matriz[i][j] = 0
            elif simetrica:
                if i < j:
                    val = random.randint(min_d, max_d)
                    matriz[i][j] = val
                    matriz[j][i] = val
            else:
                matriz[i][j] = random.randint(min_d, max_d)
    return matriz


def salvar_caso_de_teste(numero_teste, n, matriz, m, percurso):
    """Salva os arquivos .in e .out."""
    nome_in = f"{numero_teste}.in"
    nome_out = f"{numero_teste}.out"
    
    # Gerar a resposta correta
    resposta = resolver(n, matriz, m, percurso)
    
    # Escrever arquivo .in
    with open(nome_in, "w") as f_in:
        f_in.write(f"{n}\n")
        for linha in matriz:
            f_in.write(" ".join(map(str, linha)) + "\n")
        f_in.write(f"{m}\n")
        f_in.write(" ".join(map(str, percurso)) + "\n")
        
    # Escrever arquivo .out
    with open(nome_out, "w") as f_out:
        f_out.write(f"{resposta}\n")
        
    print(f"Gerado {nome_in} e {nome_out} (N={n}, M={m}, Total={resposta})")


def main():
    # Fixar a semente para garantir reproducibilidade
    random.seed(42)
    
    casos = []
    
    # Caso 1: Exemplo do enunciado
    casos.append({
        'n': 3,
        'matriz': [
            [0, 2, 4],
            [2, 0, 1],
            [4, 1, 0]
        ],
        'm': 4,
        'percurso': [1, 2, 3, 1]
    })
    


    n = 6
    m = 10
    mat = gerar_matriz(n, min_d=1, max_d=10)
    per = [random.randint(1, n) for _ in range(m)]
    casos.append({'n': n, 'matriz': mat, 'm': m, 'percurso': per})

    # Caso 5 a 8: Casos aleatórios médios
    for _ in range(1):
        n = random.randint(10, 50)
        m = random.randint(100, 1000)
        mat = gerar_matriz(n, min_d=1, max_d=10**6)
        per = [random.randint(1, n) for _ in range(m)]
        casos.append({'n': n, 'matriz': mat, 'm': m, 'percurso': per})

    # Caso 9 e 10: Casos no limite máximo (N = 500, M = 100.000, D_ij = 10^9)
    # Testa estouro de inteiro 32-bit (o resultado será ~10^14)
    for _ in range(2):
        n = 500
        m = 100000
        mat = gerar_matriz(n, min_d=10**6, max_d=10**9, simetrica=False)
        per = [random.randint(1, n) for _ in range(m)]
        casos.append({'n': n, 'matriz': mat, 'm': m, 'percurso': per})

    # Salvar todos os casos de teste
    for idx, caso in enumerate(casos, start=1):
        salvar_caso_de_teste(idx, caso['n'], caso['matriz'], caso['m'], caso['percurso'])

if __name__ == "__main__":
    main()