import random
import os

MOD = 1000000007


def solve(queries):
    """Calcula F(N) % MOD para cada N em queries."""
    max_n = max(queries, default=0)
    fib = [0] * (max_n + 1)

    if max_n >= 0:
        fib[0] = 0
    if max_n >= 1:
        fib[1] = 1

    for i in range(2, max_n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD

    return [fib[n] for n in queries]


def create_test_case(filename_base, queries):
    in_filepath = f"{filename_base}.in"
    out_filepath = f"{filename_base}.out"

    with open(in_filepath, "w") as f_in:
        f_in.write(f"{len(queries)}\n")
        for q in queries:
            f_in.write(f"{q}\n")

    answers = solve(queries)
    with open(out_filepath, "w") as f_out:
        for ans in answers:
            f_out.write(f"{ans}\n")

    print(f"Gerado: {in_filepath} e {out_filepath} (Q={len(queries)}, Max N={max(queries) if queries else 0})")


def main():
    os.makedirs("test_cases", exist_ok=True)

    test_suite = [
        [0, 1, 2, 3, 5],
        [10, 20, 50, 100],
        [0, 1, 1, 2, 3, 5, 8, 13],
    ]

    random.seed(42)
    test_suite.append([random.randint(0, 1000) for _ in range(100)])
    test_suite.append([random.randint(0, 1000000) for _ in range(1000)])

    for idx, queries in enumerate(test_suite, start=1):
        filename_base = os.path.join("./", str(idx))
        create_test_case(filename_base, queries)


if __name__ == "__main__":
    main()
