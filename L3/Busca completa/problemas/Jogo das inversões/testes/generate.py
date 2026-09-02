import random

def solve(n: int, a: list[int]) -> int:
    """Calcula a resposta ótima usando o algoritmo de Kadane em O(n)."""
    total_ones = sum(a)
    max_gain = -float('inf')
    current_gain = 0
    
    # Cada 0 dá ganho de +1, cada 1 dá perda de -1 (ganho de -1)
    for x in a:
        gain = 1 if x == 0 else -1
        current_gain = max(gain, current_gain + gain)
        max_gain = max(max_gain, current_gain)
        
    return total_ones + max_gain

def generate_test_case(n: int = None, pattern: str = "random") -> tuple[str, str]:
    """
    Gera um caso de teste e sua respectiva saída esperada.
    """
    if n is None:
        n = random.randint(1, 100)
    
    if pattern == "all_ones":
        a = [1] * n
    elif pattern == "all_zeros":
        a = [0] * n
    elif pattern == "alternating":
        a = [i % 2 for i in range(n)]
    else:  # random
        a = [random.choice([0, 1, 0,0,0]) for _ in range(n)]
        
    ans = solve(n, a)
    
    input_str = f"{n}\n" + " ".join(map(str, a))
    output_str = str(ans)
    
    return input_str, output_str

def main():
    # Exemplos de casos de teste gerados
    print("--- Exemplos de Casos de Teste Gerados ---\n")
    
    test_types = [
        ("Caso Aleatório Pequeno", 5, "random"),
        ("Caso Todos Uns (Edge Case)", 4, "all_ones"),
        ("Caso Todos Zeros (Edge Case)", 6, "all_zeros"),
        ("Caso Alternado", 7, "alternating"),
        ("Caso Limite Máximo (n=100)", 100, "random"),
    ]
    
    for title, n, pattern in test_types:
        inp, out = generate_test_case(n=n, pattern=pattern)
        print(f"=== {title} ===")
        print("[Entrada]")
        print(inp)
        print("[Saída Esperada]")
        print(out)
        print()

if __name__ == "__main__":
    main()