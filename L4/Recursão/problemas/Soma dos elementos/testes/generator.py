import random
from pathlib import Path

base_dir = Path(__file__).resolve().parent
cases_dir = base_dir / ""
cases_dir.mkdir(exist_ok=True)


# Gera um caso aleatório grande
# Observação: os valores podem ser negativos, positivos e repetidos.
def generate_case(size: int, min_value: int = -10**9, max_value: int = 10**9):
    arr = [random.randint(min_value, max_value) for _ in range(size)]
    answer = sum(arr)
    return arr, answer


def write_case(idx: int, arr, answer):
    in_path = cases_dir / f"{idx}.in"
    out_path = cases_dir / f"{idx}.out"

    with in_path.open("w", encoding="utf-8") as f:
        f.write(f"{len(arr)}\n")
        f.write(" ".join(map(str, arr)) + "\n")

    with out_path.open("w", encoding="utf-8") as f:
        f.write(f"{answer}\n")


# Gerar casos grandes e aleatórios
large_cases = [
    (5, 1, 10),
    (10, -10, 10),
    (1000, 0, 10**9),
    (100000, -10**6, 10**6),
]

# Gera casos de teste em sequência a partir do número 3, preservando 1 e 2 como exemplos.
for idx, (size, low, high) in enumerate(large_cases, start=1):
    arr, answer = generate_case(size, low, high)
    write_case(idx, arr, answer)

print(f"Casos gerados em: {cases_dir}")
