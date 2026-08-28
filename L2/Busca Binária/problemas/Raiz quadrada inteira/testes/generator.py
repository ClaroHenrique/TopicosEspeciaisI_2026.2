import math
import random

def generate_test_case(filename_in="teste.in", filename_out="teste.sol", num_queries=10000):
    MAX_A = 10**9
    
    # 1. Casos de borda e valores críticos essenciais
    edge_cases = [
        0, 1, 2, 3, 4, 
        MAX_A, MAX_A - 1, 
        9999800001,  # 99999^2
        1000000000,  # 10^9
    ]
    
    # Quadrados perfeitos e seus vizinhos imediatos
    for r in [10, 100, 1000, 31622]: # 31622^2 ~ 999950884 <= 10^9
        sq = r * r
        if sq <= MAX_A:
            edge_cases.extend([sq - 1, sq, sq + 1])
            
    # Remove duplicatas e valores fora do intervalo [0, 10^9]
    edge_cases = sorted(list(set(x for x in edge_cases if 0 <= x <= MAX_A)))
    
    # 2. Preenche o restante com números aleatórios até atingir num_queries
    queries = edge_cases.copy()
    remaining = num_queries - len(queries)
    if remaining > 0:
        queries.extend([random.randint(0, MAX_A) for _ in range(remaining)])
    else:
        queries = queries[:num_queries]
        
    random.shuffle(queries)
    
    # 3. Gera o arquivo de entrada (.in)
    with open(filename_in, "w") as fin:
        fin.write(f"{len(queries)}\n")
        for q in queries:
            fin.write(f"{q}\n")
            
    # 4. Gera o arquivo de saída esperada (.sol)
    with open(filename_out, "w") as fout:
        for q in queries:
            fout.write(f"{math.isqrt(q)}\n")

    print(f"Gerado {len(queries)} casos de teste com sucesso!")
    print(f"Entrada: {filename_in}")
    print(f"Saída:   {filename_out}")

if __name__ == "__main__":
    generate_test_case()