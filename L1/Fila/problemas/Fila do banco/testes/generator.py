import random
from collections import deque
from pathlib import Path


def resolver_caso(operacoes: list[str]) -> list[str]:
    """Soluciona o problema usando duas filas para produzir o gabarito."""
    fila_pref = deque()
    fila_norm = deque()
    saida = []

    for op in operacoes:
        partes = op.split()
        tipo = partes[0]

        if tipo == "CHEGOU":
            senha = partes[1]
            if senha.startswith("PRE-"):
                fila_pref.append(senha)
            else:
                fila_norm.append(senha)

        elif tipo == "ATENDIDO":
            if fila_pref:
                saida.append(fila_pref.popleft())
            elif fila_norm:
                saida.append(fila_norm.popleft())
            else:
                saida.append("0")

    return saida


def gerar_operacoes(n: int, prob_chegada: float = 0.6) -> list[str]:
    """Gera uma lista de N operações aleatórias no formato do problema."""
    operacoes = []

    for _ in range(n):
        # Decide se o evento é uma chegada ou atendimento
        if random.random() < prob_chegada:
            tipo_senha = random.choice(["PRE", "NOR"])
            numero = random.randint(0, 9999)
            senha = f"{tipo_senha}-{numero:04d}"
            operacoes.append(f"CHEGOU {senha}")
        else:
            operacoes.append("ATENDIDO")

    return operacoes


def gerar_suite(qtd_testes: int = 10, pasta_saida: str = "testes"):
    """Gera os pares de arquivos .in e .sol."""
    caminho = Path(pasta_saida)
    caminho.mkdir(parents=True, exist_ok=True)

    for i in range(1, qtd_testes + 1):
        # Sorteia N dentro das restrições (1 <= N <= 100)
        # O último teste é forçado a ter N = 100 (limite máximo)
        n = 100 if i == qtd_testes else random.randint(1, 100)

        # Varia as probabilidades para simular cenários de alta demanda ou esvaziamento
        prob = random.choice([0.3, 0.5, 0.7, 0.85])
        operacoes = gerar_operacoes(n, prob_chegada=prob)
        saida_esperada = resolver_caso(operacoes)

        # Salva o arquivo de entrada (.in)
        arq_in = caminho / f"teste_{i:02d}.in"
        with open(arq_in, "w", encoding="utf-8") as f:
            f.write(f"{n}\n")
            for op in operacoes:
                f.write(f"{op}\n")

        # Salva o arquivo de saída esperada (.sol)
        arq_sol = caminho / f"teste_{i:02d}.sol"
        with open(arq_sol, "w", encoding="utf-8") as f:
            for linha in saida_esperada:
                f.write(f"{linha}\n")

    print(f"Sucesso: {qtd_testes} casos de teste gerados na pasta '{pasta_saida}'.")


if __name__ == "__main__":
    # Fixa a seed se quiser testes reprodutíveis (opcional)
    # random.seed(42)

    gerar_suite(qtd_testes=2, pasta_saida="casos_de_teste")