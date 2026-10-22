import random


def resolver(usuarios, amizades):
    amigos = {u: set() for u in usuarios}
    for u, v in amizades:
        amigos[u].add(v)
        amigos[v].add(u)

    melhor = None
    melhor_qtd = -1
    for u in sorted(usuarios):
        qtd = len(amigos[u])
        if qtd > melhor_qtd:
            melhor = u
            melhor_qtd = qtd
    return melhor


def salvar_caso(numero, usuarios, amizades):
    nome_in = f"{numero}.in"
    nome_out = f"{numero}.out"

    with open(nome_in, "w") as f_in:
        f_in.write(f"{len(usuarios)} {len(amizades)}\n")
        # for u in usuarios:
        #     f_in.write(f"{u}\n")
        # f_in.write(f"{len(amizades)}\n")
        for u, v in amizades:
            f_in.write(f"{u} {v}\n")

    resposta = resolver(usuarios, amizades)
    with open(nome_out, "w") as f_out:
        f_out.write(f"{resposta}\n")

    print(f"Gerado {nome_in} e {nome_out}: {resposta}")


def main():
    random.seed(42)

    casos = []

    casos.append({
        "usuarios": ["ana", "bia", "carlos", "duda", "joao"],
        "amizades": [
            ("ana", "bia"),
            ("ana", "carlos"),
            ("bia", "carlos"),
            ("bia", "duda"),
            ("carlos", "joao"),
            ("duda", "joao"),
        ],
    })

    casos.append({
        "usuarios": ["alice", "bob", "carol", "dan", "erin"],
        "amizades": [
            ("dan", "erin"),
            ("alice", "bob"),
            ("bob", "alice"),
            ("erin", "dan"),
            ("alice", "carol"),
            ("bob", "carol"),
            ("dan", "erin"),
            ("erin", "dan"),
        ],
    })

    casos.append({
        "usuarios": ["u1", "u2", "u3", "u4", "u5"],
        "amizades": [
            ("u3", "u4"),
            ("u2", "u3"),
            ("u4", "u5"),
            ("u1", "u2"),
            ("u4", "u5"),
            ("u5", "u1"),
            ("u1", "u2"),
            ("u3", "u4"),
        ],
    })

    for i in [50, 500, 100000]:
        usuarios = [f"user{j}" for j in range(1, i + 1)]
        amizades = []
        for _ in range(min(i*4, 100000)):
            u, v = random.sample(usuarios, 2)
            amizades.append((u, v))
        casos.append({"usuarios": usuarios, "amizades": amizades})

    for idx, caso in enumerate(casos, start=1):
        salvar_caso(idx, caso["usuarios"], caso["amizades"])


if __name__ == "__main__":
    main()
