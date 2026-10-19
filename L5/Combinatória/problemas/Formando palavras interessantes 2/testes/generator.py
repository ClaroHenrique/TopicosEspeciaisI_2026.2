import os
import random
import string


# 1. Função própria para calcular o fatorial
def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# 2. Solução oficial do problema sem usar bibliotecas externas
def resolver(palavra):
    # Se a palavra não contém a letra 's', é impossível formar uma palavra terminada em 's'
    if 's' not in palavra:
        return 0

    # Contagem da frequência de cada caractere utilizando dicionário puro (Dict)
    frequencias = {}
    for char in palavra:
        if char in frequencias:
            frequencias[char] += 1
        else:
            frequencias[char] = 1

    # Removemos um 's' que será fixado na última posição da palavra
    frequencias['s'] -= 1
    if frequencias['s'] == 0:
        del frequencias['s']

    # O total de letras restantes para permutar é N - 1
    total_letras_restantes = len(palavra) - 1

    # Fórmula da Permutação com Repetição:
    # (N - 1)! / (f1! * f2! * ... * fk!)
    numerador = fatorial(total_letras_restantes)

    denominador = 1
    for char, freq in frequencias.items():
        denominador *= fatorial(freq)

    return numerador // denominador


# 3. Gerador dos casos de teste
def gerar_testes():
    pasta_saida = "testes"
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Lista com as entradas de teste
    casos = [
        # Exemplos do enunciado
        "mississippi",
        # Edge cases de pegadinha (Sem a letra 's')
        "galo",
        "s",
        # Tamanhos limites (até 20 caracteres)
        "abcdefghijklmnopqrst",  # 20 letras distintas com 1 's' (Resultado: 19! -> Estoura 32-bit INT)
        "ssssssssssssssssssss",  # 20 letras 's'
        "paralelepipedos",  # Palavra grande com repetições e 's'
        "anticonstitucionalis",  # 20 caracteres terminando em 's'
    ]


    # Escrevendo os arquivos N.in e N.out
    for idx, palavra in enumerate(casos, start=1):
        resposta = resolver(palavra)

        arquivo_in = os.path.join("", f"{idx}.in")
        arquivo_out = os.path.join("", f"{idx}.out")

        with open(arquivo_in, "w", encoding="utf-8") as f_in:
            f_in.write(f"{palavra}\n")

        with open(arquivo_out, "w", encoding="utf-8") as f_out:
            f_out.write(f"{resposta}\n")

        print(f"Gerado: {idx}.in / {idx}.out -> Entrada: '{palavra}' | Saida: {resposta}")

    print(f"\nSucesso! {len(casos)} pares de testes gerados na pasta '{pasta_saida}'.")


if __name__ == "__main__":
    gerar_testes()