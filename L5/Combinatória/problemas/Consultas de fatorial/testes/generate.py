import random
import os

MOD = 1000000007

def solve(queries):
    """
    Calcula N! % MOD para cada consulta N em queries.
    Utiliza pré-computação para calcular consultas ordenadas eficientemente.
    """
    # Ordena mantendo os índices originais para responder na ordem correta
    indexed_queries = sorted(enumerate(queries), key=lambda x: x[1])
    results = [0] * len(queries)
    
    current_val = 1
    current_n = 0
    
    for orig_idx, n in indexed_queries:
        # Avança o fatorial do ponto atual até n
        while current_n < n:
            current_n += 1
            current_val = (current_val * current_n) % MOD
        results[orig_idx] = current_val
        
    return results

def create_test_case(filename_base, queries):
    """Escreve as entradas (.in) e saídas (.out) nos respectivos arquivos."""
    in_filepath = f"{filename_base}.in"
    out_filepath = f"{filename_base}.out"
    
    # 1. Gera o arquivo de entrada (.in)
    with open(in_filepath, "w") as f_in:
        f_in.write(f"{len(queries)}\n")
        for q in queries:
            f_in.write(f"{q}\n")
            
    # 2. Calcula e gera o arquivo de saída (.out)
    answers = solve(queries)
    with open(out_filepath, "w") as f_out:
        for ans in answers:
            f_out.write(f"{ans}\n")
            
    print(f"Gerado: {in_filepath} e {out_filepath} (Q={len(queries)}, Max N={max(queries) if queries else 0})")

def main():
    os.makedirs("test_cases", exist_ok=True)
    
    # Conjunto de testes variados
    test_suite = [
        # 1. Exemplo do enunciado
        [1, 2, 3, 4],
        # 2. Casos de borda simples
        [11, 1, 20, 1, 1000000],
    ]
    
    random.seed(42) # Garante reprodutibilidade
    
    # 5. Caso com consultas pequenas/médias aleatórias (N até 10^5)
    test_suite.append([random.randint(0, 1000) for _ in range(100)])
    
    # 7. Caso limite total: N máximo próximo do limite (10^8) e Q = 1000
    test_suite.append([random.randint(0, 1000000) for _ in range(1000)])

    # Gerar os arquivos .in e .out
    for idx, queries in enumerate(test_suite, start=1):
        filename_base = os.path.join("./", str(idx))
        create_test_case(filename_base, queries)

if __name__ == "__main__":
    main()