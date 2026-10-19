import random

def solve(s: str) -> int:
    """
    Resolve o problema para calcular o número mínimo de remoções
    para obter uma subsequência não decrescente (equivalente a N - tamanho_LCS).
    Como o alfabeto é fixo (A, C, G, T), podemos usar programação dinâmica
    ou patience sorting / DP otimizada.
    """
    n = len(s)
    
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    tails = []
    
    import bisect
    for char in s:
        val = mapping[char]
        # Inserção binária para encontrar a posição onde 'val' se encaixa
        idx = bisect.bisect_right(tails, val)
        if idx < len(tails):
            tails[idx] = val
        else:
            tails.append(val)
            
    # O tamanho da maior subsequência não decrescente é len(tails)
    lis_length = len(tails)
    return n - lis_length

def generate_test_case(case_type, length):
    chars = ['A', 'C', 'G', 'T']
    if case_type == 'random':
        return "".join(random.choices(chars, k=length))
    elif case_type == 'sorted':
        # Já ordenado
        return "".join(sorted(random.choices(chars, k=length)))
    elif case_type == 'reverse':
        # Inversamente ordenado (pior caso para LIS)
        return "".join(sorted(random.choices(chars, k=length), reverse=True))
    elif case_type == 'repetitive':
        # Blocos repetitivos
        block = random.choice(chars)
        return "".join([random.choice(chars) if random.random() > 0.3 else block for _ in range(length)])

def main():
    # Definir quantidade de casos de teste que deseja gerar
    num_tests = 5
    
    # Restrição máxima do problema é 2 * 10^6, mas para testes menores podemos variar
    test_configs = [
        ("Exemplo do enunciado", "GATCGATT"),
        ("Outro exemplo", "AACCGGTT"),
        ("Pequeno aleatório", 50),
        ("Médio aleatório", 5000),
        ("Grande (perto do limite)", 100000), # Usar menor para teste rápido, ou até 2*10^6 se tiver tempo
        ("Grande (perto do limite)", 200000), # Usar menor para teste rápido, ou até 2*10^6 se tiver tempo
    ]
    
    for i, (name, config) in enumerate(test_configs, start=1):
        if isinstance(config, str):
            s = config
        else:
            # Gerar aleatório com base no tamanho
            s = generate_test_case('random', config)
            
        ans = solve(s)
        
        # Salvar arquivo .in
        with open(f"{i}.in", "w") as f_in:
            f_in.write(s + "\n")
            
        # Salvar arquivo .out
        with open(f"{i}.out", "w") as f_out:
            f_out.write(str(ans) + "\n")
            
        print(f"Caso {i} gerado com sucesso! ({name}, tamanho: {len(s)})")

if __name__ == "__main__":
    main()