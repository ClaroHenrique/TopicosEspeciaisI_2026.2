from collections import Counter
import math


def contar_anagramas_distintos(palavra: str) -> int:
    # Ignora diferenças entre maiúsculas/minúsculas e remove espaços
    palavra = palavra.lower().replace(" ", "")

    if not palavra:
        return 0

    # Contagem total de letras (n)
    total_letras = len(palavra)

    # Frequência de cada caractere
    frequencias = Counter(palavra)

    # Cálculo do numerador: n!
    numerador = math.factorial(total_letras)

    # Cálculo do denominador: n1! * n2! * ... * nk!
    denominador = 1
    for qtd in frequencias.values():
        denominador *= math.factorial(qtd)

    return numerador // denominador


# --- Exemplo de Uso ---
if __name__ == "__main__":
    palavras_teste = ["MISSISIPPI"]

    for p in palavras_teste:
        qtd = contar_anagramas_distintos(p)
        print(f"A palavra '{p}' possui {qtd} anagramas distintos.")
