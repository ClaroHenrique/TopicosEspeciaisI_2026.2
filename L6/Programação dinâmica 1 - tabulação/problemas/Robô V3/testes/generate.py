import os
import random

MOD = 10**9 + 7


def solve(grid):
    """Retorna o maior valor de moedas que o robô pode coletar no caminho para a célula final."""
    n = len(grid)
    m = len(grid[0]) if n else 0


    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]

    for i in range(n):
        for j in range(m):
            from_top = dp[i - 1][j] if i > 0 else 0
            from_left = dp[i][j - 1] if j > 0 else 0
            dp[i][j] = max(from_top, from_left) + grid[i][j]

    return dp[n - 1][m - 1]


def inteiro_com_raridade():
    categorias = ['normal', 'enorme']
    pesos = [0.8, 0.2] 
    
    escolha = random.choices(categorias, weights=pesos, k=1)[0]
    
    if escolha == 'normal':
        return random.randint(20, 200)
    else:
        return random.randint(1_000_000, 1_000_000_000)

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
            [0, 2, 3],
            [2, 1, 0],
            [3, 1, 0],
        ],
        [
            [10, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 10],
        ],
        [
            [0, 0, 1],
            [9, 9, 9],
            [0, 0, 2],
            [0, 0, 0],
            [0, 0, 0],
            [0, 10, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
    ]

    random.seed(42)
    for _ in range(1):
        n = random.randint(50, 100)
        m = random.randint(50, 100)
        grid = [[random.randint(0, 10000) for _ in range(m)] for _ in range(n)]
        test_suite.append(grid)

    
    for _ in range(2):
        n = random.randint(50, 100)
        m = random.randint(50, 100)
        grid = [[inteiro_com_raridade() for _ in range(m)] for _ in range(n)]
        test_suite.append(grid)

    for idx, grid in enumerate(test_suite, start=1):
        filename_base = os.path.join("./", str(idx))
        create_test_case(filename_base, grid)


if __name__ == "__main__":
    main()
