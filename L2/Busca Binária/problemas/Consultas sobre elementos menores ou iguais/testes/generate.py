import bisect
import random


def generate_test_case(
    n: int,
    m: int,
    min_val: int = -10**9,
    max_val: int = 10**9,
    sorted_a: bool = False,
) -> tuple[str, str]:
    """Gera a entrada e a saída esperada para o problema 600B."""
    # Gera os vetores a e b com valores aleatórios dentro dos limites
    a = [random.randint(min_val, max_val) for _ in range(n)]
    b = [random.randint(min_val, max_val) for _ in range(m)]

    if sorted_a:
        a.sort()

    # Formatação da entrada
    input_data = f"{n} {m}\n"
    input_data += " ".join(map(str, a)) + "\n"
    input_data += " ".join(map(str, b)) + "\n"

    # Cálculo da saída esperada usando Busca Binária (bisect_right)
    # bisect_right encontra quantos elementos em 'a_sorted' são <= bj
    a_sorted = sorted(a)
    result = [bisect.bisect_right(a_sorted, x) for x in b]
    output_data = " ".join(map(str, result)) + "\n"

    return input_data, output_data


def save_test_file(
    filename_prefix: str,
    n: int,
    m: int,
    min_val: int = -10**9,
    max_val: int = 10**9,
):
    inp, out = generate_test_case(n, m, min_val, max_val)

    with open(f"{filename_prefix}.in", "w", encoding="utf-8") as f_in:
        f_in.write(inp)

    with open(f"{filename_prefix}.out", "w", encoding="utf-8") as f_out:
        f_out.write(out)

    print(f"Gerado: {filename_prefix}.in e {filename_prefix}.out")


if __name__ == "__main__":
    # # 1. Caso Pequeno (depuração visual)
    # save_test_file("test_small", n=5, m=4, min_val=1, max_val=10)

    # # 2. Caso com números negativos e positivos variados
    # save_test_file("test_mixed", n=100, m=100, min_val=-1000, max_val=1000)

    # 3. Caso Máximo / Stress Test (limite do problema: n, m = 200.000)
    save_test_file(
        "moodle_stress",
        n=1000,
        m=1000,
        min_val=-1_000_000_000,
        max_val=1_000_000_000,
    )