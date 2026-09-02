import os
import random

# Valores das moedas: 5, 10, 25, 50, 100
COINS = [5, 10, 25, 50, 100]

def solve(V: int, P: int, counts: list[int]):
    """
    Resolve o problema retornando a menor quantidade de moedas
    [c5, c10, c25, c50, c100] ou 'impossivel'.
    """
    target = V - P
    if target < 0:
        return "impossivel"
    if target == 0:
        return "0 0 0 0 0"
    if target % 5 != 0:
        return "impossivel"

    c5, c10, c25, c50, c100 = counts
    best_solution = None
    min_total_coins = float("inf")

    # Como moedas de 25 centavos são a única anomalia do sistema canônico,
    # testamos usar k moedas de 25 (k de 0 a 3 é suficiente para cobrir qualquer paridade/resto).
    for k25 in range(min(c25, 3) + 1):
        rem = target - k25 * 25
        if rem < 0:
            break

        # Guloso para as outras moedas (100, 50, 10, 5) que formam base canônica
        u100 = min(rem // 100, c100)
        rem -= u100 * 100

        u50 = min(rem // 50, c50)
        rem -= u50 * 50

        u10 = min(rem // 10, c10)
        rem -= u10 * 10

        u5 = min(rem // 5, c5)
        rem -= u5 * 5

        if rem == 0:
            total_coins = u5 + u10 + k25 + u50 + u100
            if total_coins < min_total_coins:
                min_total_coins = total_coins
                best_solution = (u5, u10, k25, u50, u100)

    if best_solution is None:
        return "impossivel"
    return " ".join(map(str, best_solution))


def generate_test_cases(output_dir="test_cases", num_random_cases=6):
    os.makedirs(output_dir, exist_ok=True)
    test_id = 1

    def save_case(v, p, counts):
        nonlocal test_id
        in_path = os.path.join(output_dir, f"{test_id:01d}.in")
        sol_path = os.path.join(output_dir, f"{test_id:01d}.out")

        with open(in_path, "w") as f:
            f.write(f"{v}\n{p}\n{' '.join(map(str, counts))}\n")

        sol = solve(v, p, counts)
        with open(sol_path, "w") as f:
            f.write(f"{sol}\n")

        test_id += 1

    # --- Casos de Borda e Especiais ---
    
    # 1. Sem troco (V == P)
    save_case(100, 100, [1, 1, 2, 1, 3])
    save_case(500, 500, [0, 0, 0, 0, 0])

    # 2. Impossível por falta de moedas
    save_case(200, 100, [0, 0, 0, 0, 0])
    save_case(100, 50, [0, 0, 1, 0, 0])  # Precisa de 50, só tem 25

    # 3. Troco não múltiplo de 5 (impossível no sistema real)
    save_case(103, 100, [10, 10, 10, 10, 10])

    # 4. Caso clássico da moeda de 25 centavos (guloso ingênuo falha)
    # Troco = 40. Guloso pegaria 25 + 10 + 5 (3 moedas) se tivesse.
    # Mas se só tiver 4 de 10 e 1 de 25:
    save_case(140, 100, [0, 4, 1, 0, 0])  # Esperado: 0 4 0 0 0

    # 5. Limites Máximos (10^9)
    save_case(10**9, 0, [10**9, 10**9, 10**9, 10**9, 10**9])
    save_case(10**9, 10**9 - 75, [2, 2, 3, 2, 1])

    # --- Casos Aleatórios Diversificados ---
    
    # Casos Pequenos (V, P <= 1.000)
    for _ in range(num_random_cases // 3):
        p = random.randint(1, 1000)
        v = p + random.choice([0, 5, 10, 15, 25, 40, 50, 75, 100, 250, 500])
        counts = [random.randint(0, 10) for _ in range(5)]
        save_case(v, p, counts)

    # Casos Médios (V, P <= 1.000.000)
    for _ in range(num_random_cases // 3):
        p = random.randint(1, 10**6)
        v = p + random.randint(0, 50000) * 5
        counts = [random.randint(0, 1000) for _ in range(5)]
        save_case(v, p, counts)

    # Casos Grandes (V, P <= 10^9)
    for _ in range(num_random_cases // 3):
        p = random.randint(1, 5 * 10**8)
        v = p + random.randint(0, 10**8) * 5
        counts = [random.randint(0, 10**8) for _ in range(5)]
        save_case(v, p, counts)

    print(f"Sucesso! {test_id - 1} casos de teste gerados na pasta '{output_dir}/'.")

if __name__ == "__main__":
    generate_test_cases()