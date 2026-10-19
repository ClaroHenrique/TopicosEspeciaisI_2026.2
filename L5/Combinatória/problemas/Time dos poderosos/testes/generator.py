import random
import os

MOD = 1000000007

def nCr_mod(n, r, mod=MOD):
    """Calcula C(n, r) % mod usando inverso multiplicativo (Fermatt)."""
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
        
    num = 1
    den = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
        
    return (num * pow(den, mod - 2, mod)) % mod

def solve(n, k, a):
    """Solução de referência em O(N log N)."""
    a_sorted = sorted(a, reverse=True)
    
    # 1. Soma máxima dos K maiores elementos
    max_sum = sum(a_sorted[:k])
    
    # 2. Elemento limite de corte
    border_val = a_sorted[k - 1]
    
    # Quantas vezes o valor de borda aparece no array total
    count_total = a.count(border_val)
    
    # Quantos desses valores de borda precisamos pegar nos K primeiros
    count_needed = a_sorted[:k].count(border_val)
    
    # 3. Formas distintas = C(count_total, count_needed)
    ways = nCr_mod(count_total, count_needed)
    
    return max_sum, ways

def create_test_case(filename_base, n, k, a):
    """Escreve as entradas (.in) e saídas (.out) nos arquivos."""
    in_filepath = f"{filename_base}.in"
    out_filepath = f"{filename_base}.out"
    
    with open(in_filepath, "w") as f_in:
        f_in.write(f"{n} {k}\n")
        f_in.write(" ".join(map(str, a)) + "\n")
        
    max_sum, ways = solve(n, k, a)
    with open(out_filepath, "w") as f_out:
        f_out.write(f"{max_sum}\n")
        f_out.write(f"{ways}\n")
        
    print(f"Gerado: {in_filepath} e {out_filepath} (N={n}, K={k} -> Soma={max_sum}, Formas={ways})")

def main():
    os.makedirs("test_cases", exist_ok=True)
    
    test_cases = [
        # Exemplos do enunciado
        (5, 3, [10, 20, 30, 40, 50]),
        (5, 3, [10, 50, 30, 30, 50]),
        
        # Casos de borda
        (1, 1, [1000000000]), # N=1, K=1 com elemento máximo
        (5, 5, [1, 2, 3, 4, 5]), # K = N (escolhe todos) -> 1 forma
        (5, 3, [42, 42, 42, 42, 42]), # Todos os elementos iguais -> C(5, 3) = 10 formas
    ]
    
    random.seed(42) # Garante reprodutibilidade
    
    # Testes com repetições médias
    for _ in range(3):
        n = random.randint(10, 1000)
        k = random.randint(1, n)
        # Poucos valores possíveis para forçar empates
        a = [random.choice([10, 20, 30, 40, 50]) for _ in range(n)]
        test_cases.append((n, k, a))
        
    # Teste de grande escala (N = 10^5)
    N_MAX = 10000
    
    # Grande escala 1: Valores totalmente aleatórios
    n1, k1 = N_MAX, N_MAX // 2
    a1 = [random.randint(1, 10**3) for _ in range(n1)]
    test_cases.append((n1, k1, a1))
    
    # Grande escala 2: Muitas duplicatas do valor limite
    n2, k2 = N_MAX, (N_MAX*3) // 4
    a2 =      [random.randint(10**9-100, 10**9) for _ in range(n2//2)]
    a2 = a2 + [random.randint(10**4-100, 10**4) for _ in range(n2//2)]
    random.shuffle(a2)
    test_cases.append((n2, k2, a2))

    # Escrever arquivos
    for idx, (n, k, a) in enumerate(test_cases, start=1):
        filename_base = os.path.join("./", str(idx))
        create_test_case(filename_base, n, k, a)

if __name__ == "__main__":
    main()