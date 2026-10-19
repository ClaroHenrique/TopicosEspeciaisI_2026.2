import os
import random

MOD = 10**9 + 7


def solve(grid):
    """Retorna o número de caminhos válidos modulo MOD."""
    n = len(grid)
    m = len(grid[0]) if n else 0

    if n == 0 or m == 0:
        return 0
    if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
        return 0

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dp[i][j] = 0
                continue

            if i > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD

    return dp[n - 1][m - 1]


def create_test_case(filename_base, grid):
    in_filepath = f"{filename_base}.in"
    out_filepath = f"{filename_base}.out"

    with open(in_filepath, "w") as f_in:
        f_in.write(f"{len(grid)} {len(grid[0])}\n")
        for row in grid:
            f_in.write(" ".join(map(str, row)) + "\n")

    answer = solve(grid)
    with open(out_filepath, "w") as f_out:
        f_out.write(f"{answer}\n")

    print(f"Gerado: {in_filepath} e {out_filepath}")


def main():
    os.makedirs("test_cases", exist_ok=True)

    test_suite = [
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        [
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 0],
        ],
    ]

    random.seed(42)
    for _ in range(3):
        n = random.randint(1, 100)
        m = random.randint(1, 100)
        grid = [[random.choice([0,0,0,0,0,0,1]) for _ in range(m)] for _ in range(n)]
        # garante que inicia e termina sejam livres para evitar casos triviais demais
        if grid[0][0] == 1:
            grid[0][0] = 0
        if grid[n - 1][m - 1] == 1:
            grid[n - 1][m - 1] = 0
        test_suite.append(grid)

    for idx, grid in enumerate(test_suite, start=1):
        filename_base = os.path.join("./test_cases", str(idx))
        create_test_case(filename_base, grid)


if __name__ == "__main__":
    main()
