import random
import os

def solve(n, digits):
    """
    Calcula a quantidade de números válidos de 3 dígitos.
    - O primeiro dígito (centena) não pode ser 0.
    - Os dígitos podem ser repetidos.
    """
    non_zero_count = sum(1 for d in digits if d != 0)
    # Primeiro dígito: escolhas não nulas (non_zero_count)
    # Segundo dígito: todas as escolhas (n)
    # Terceiro dígito: todas as escolhas (n)
    return non_zero_count * n * n

def create_test_case(filename_base, n, digits):
    """Escreve as entradas (.in) e saídas (.out) nos respectivos arquivos."""
    in_filepath = f"{filename_base}.in"
    out_filepath = f"{filename_base}.out"
    
    # 1. Gera o arquivo de entrada (.in)
    with open(in_filepath, "w") as f_in:
        f_in.write(f"{n}\n")
        f_in.write(" ".join(map(str, digits)) + "\n")
        
    # 2. Calcula e gera o arquivo de saída (.out)
    result = solve(n, digits)
    with open(out_filepath, "w") as f_out:
        f_out.write(f"{result}\n")
        
    print(f"Gerado: {in_filepath} e {out_filepath} (N={n}, Digitos={digits} -> Resposta={result})")

def main():
    # Cria diretório para salvar os testes (opcional)
    os.makedirs("test_cases", exist_ok=True)
    
    # Lista de casos de teste definidos manualmente + aleatórios
    test_cases = [
        # Casos dos exemplos do enunciado
        (3, [1, 2, 3]),
        (2, [0, 1]),
        
        # Casos de borda / especiais
        (1, [0]),           # Apenas 0 -> Resultado deve ser 0
        (1, [5]),           # 1 dígito não-zero -> 555 é o único -> Resultado: 1
        (10, list(range(10))), # Todos os 10 dígitos (0 a 9) -> 9 * 10 * 10 = 900
        
        # Outros casos variados
        (4, [0, 2, 4, 6]),
        (5, [1, 3, 5, 7, 9]),
    ]
    
    # Gerar casos aleatórios adicionais
    random.seed(42) # Garante que os testes sejam reproduzíveis
    for _ in range(5):
        n = random.randint(1, 10)
        digits = sorted(random.sample(range(10), n))
        test_cases.append((n, digits))

    # Escrever todos os arquivos
    for idx, (n, digits) in enumerate(test_cases, start=1):
        filename_base = os.path.join(".", str(idx))
        create_test_case(filename_base, n, digits)

if __name__ == "__main__":
    main()