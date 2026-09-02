import random

def solve(n, x, a):
    """Função ótima (gulosa/greedy) para encontrar a resposta correta."""
    a_sorted = sorted(a)
    count = 0
    total_time = 0
    for time in a_sorted:
        if total_time + time <= x:
            total_time += time
            count += 1
        else:
            break
    return count

def generate_test_cases(num_tests=10):
    """Gera casos de teste variados cobrindo casos de borda e aleatórios."""
    test_cases = []
    
    # Caso 1: Exemplo do enunciado
    test_cases.append((6, 15, [4, 3, 8, 4, 7, 3]))
    
    # Caso 2: Menores valores possíveis (N=1, X=1, a_1=1) -> Consegue aprender
    test_cases.append((1, 1, [1]))
    
    # Caso 3: N=1, mas o algoritmo custa mais que o tempo disponível -> 0
    test_cases.append((1, 5, [10]))
    
    # Caso 4: Tempo suficiente para aprender TODOS os algoritmos
    test_cases.append((5, 100, [10, 20, 15, 5, 25]))
    
    # Caso 5: Tempo insuficiente para aprender QUALQUER algoritmo
    test_cases.append((4, 2, [5, 10, 3, 8]))
    
    # Caso 6: Todos os elementos iguais
    test_cases.append((10, 30, [10] * 10))
    
    # Caso 7: Limite máximo de N (100) e valores altos de X
    n = 100
    x = 10000
    a = [random.randint(1, 100) for _ in range(n)]
    test_cases.append((n, x, a))
    
    # Caso 8: Limite máximo de N (100) e X pequeno
    n = 100
    x = 50
    a = [random.randint(1, 100) for _ in range(n)]
    test_cases.append((n, x, a))

    # Casos aleatórios adicionais
    while len(test_cases) < num_tests:
        n = random.randint(1, 100)
        x = random.randint(1, 1000)
        a = [random.randint(1, 100) for _ in range(n)]
        test_cases.append((n, x, a))
        
    return test_cases

if __name__ == "__main__":
    tests = generate_test_cases(10)
    
    print(f"=== GERADOR DE CASOS DE TESTE (Total: {len(tests)}) ===\n")
    for idx, (n, x, a) in enumerate(tests, 1):
        ans = solve(n, x, a)
        print(f"--- Caso de Teste #{idx} ---")
        print("Entrada (Input):")
        print(f"{n} {x}")
        print(" ".join(map(str, a)))
        print("Saída Esperada (Output):")
        print(f"{ans}\n")