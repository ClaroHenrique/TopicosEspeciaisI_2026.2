import random
from pathlib import Path


def gerar_caso(n=100000, q=100000):
    """Cria um caso de teste aleatório válido para o problema."""

    arr = [random.choice([-1, 1, 1]) for _ in range(n)]
    consultas = []

    for i in range(q):
        if(q>= 100 and i % (q//10) == 1):
            l = 0
        else:
            l = random.randint(0, n - 1)
        r = random.randint(l, n - 1)
        consultas.append((l, r))

    return arr, consultas


def resolver(arr, consultas):
    """Calcula a resposta de cada consulta em O(1) por meio de prefix sum."""
    prefix = [0] * (len(arr) + 1)
    for i, valor in enumerate(arr, start=1):
        prefix[i] = prefix[i - 1] + (1 if valor == -1 else 0)

    respostas = []
    for l, r in consultas:
        negativos = prefix[r + 1] - prefix[l]
        respostas.append("-1" if negativos % 2 == 1 else "1")
    return respostas


def formatar_entrada(n, arr, consultas):
    linhas = [f"{n} {len(consultas)}"]
    linhas.append(" ".join(map(str, arr)))
    for l, r in consultas:
        linhas.append(f"{l} {r}")
    return "\n".join(linhas) + "\n"


def formatar_saida(respostas):
    return "\n".join(respostas) + "\n"


def gerar_arquivos(num_arquivos=5, max_n=100000, max_q=100000, seed=None):
    """Gera arquivos 1.in, 1.out, 2.in, 2.out, ..."""
    if seed is not None:
        random.seed(seed)

    pasta = Path(__file__).resolve().parent

    casos_n_q = [
        (5, 3),
        (10, 5),
        (100, 20),
        (1000, 300),
        (10000, 3000),
        (100000, 10000),
        (100000, 10000),
    ]
    for i, (n,q) in enumerate(casos_n_q, start=1):
        arr, consultas = gerar_caso(n, q)
        respostas = resolver(arr, consultas)

        with (pasta / f"{i}.in").open("w", encoding="utf-8") as f_in:
            f_in.write(formatar_entrada(len(arr), arr, consultas))

        with (pasta / f"{i}.out").open("w", encoding="utf-8") as f_out:
            f_out.write(formatar_saida(respostas))

        print(f"Gerado: {i}.in e {i}.out (n={len(arr)}, q={len(consultas)})")


if __name__ == "__main__":
    import sys

    num_arquivos = 5
    if len(sys.argv) > 1:
        try:
            num_arquivos = int(sys.argv[1])
        except ValueError:
            print("Uso: python generate.py [quantidade_de_arquivos]")
            sys.exit(1)

    gerar_arquivos(num_arquivos=num_arquivos, max_n=100000, max_q=100000)
