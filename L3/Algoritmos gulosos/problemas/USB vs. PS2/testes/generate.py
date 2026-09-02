import random
import sys

def solve(a, b, c, mouses):
    """
    Função de referência para calcular o output esperado de um caso de teste.
    """
    usb = sorted([cost for cost, p_type in mouses if p_type == "USB"])
    ps2 = sorted([cost for cost, p_type in mouses if p_type == "PS/2"])
    
    count = 0
    total_cost = 0
    
    # 1. Atender computadores apenas USB
    take_usb = min(a, len(usb))
    count += take_usb
    total_cost += sum(usb[:take_usb])
    rem_usb = usb[take_usb:]
    
    # 2. Atender computadores apenas PS/2
    take_ps2 = min(b, len(ps2))
    count += take_ps2
    total_cost += sum(ps2[:take_ps2])
    rem_ps2 = ps2[take_ps2:]
    
    # 3. Atender computadores com ambas as portas com os mais baratos restantes
    rem_all = sorted(rem_usb + rem_ps2)
    take_both = min(c, len(rem_all))
    count += take_both
    total_cost += sum(rem_all[:take_both])
    
    return count, total_cost

def generate_test_case(max_a=100, max_b=100, max_c=100, max_m=200, max_val=10**6):
    """
    Gera um caso de teste respeitando os limites passados.
    """
    a = random.randint(0, max_a)
    b = random.randint(0, max_a//2)
    c = random.randint(0, max_a//4)
    m = random.randint(0, (a+b+c)*2)
    
    mouses = []
    types = ["USB", "USB", "USB", "PS/2"]
    for _ in range(m):
        val = random.randint(1, max_val)
        t = random.choice(types)
        mouses.append((val, t))
        
    return a, b, c, m, mouses

def format_input(a, b, c, m, mouses):
    lines = [f"{a} {b} {c}", str(m)]
    for val, t in mouses:
        lines.append(f"{val} {t}")
    return "\n".join(lines)

if __name__ == "__main__":
    # Exemplo 1: Gerar e exibir um caso de teste aleatório pequeno
    print("=== CASO DE TESTE PEQUENO ALEATÓRIO ===")
    a, b, c, m, mouses = [2,2,2,8,[
        (1, "USB"),
        (402, "USB"),
        (2, "USB"),
        (406, "USB"),
        (3, "PS/2"),
        (5, "PS/2"),
        (8, "PS/2"),
        (2, "PS/2"),
    ]]
    #generate_test_case(max_a=5, max_b=5, max_c=5, max_m=8, max_val=50)
    input_str = format_input(a, b, c, m, mouses)
    ans_count, ans_cost = solve(a, b, c, mouses)
    
    print("--- ENTRADA (.in) ---")
    print(input_str)
    print("--- SAÍDA ESPERADA (.out) ---")
    print(f"{ans_count} {ans_cost}\n")

    # Exemplo 2: Gerar múltiplos arquivos de teste (ex: test_01.in, test_01.out)
    num_files = 4
    print(f"=== GERANDO {num_files} ARQUIVOS DE TESTE ===")
    for i in range(1, num_files + 1):
        a, b, c, m, mouses = generate_test_case(max_a=1000, max_b=1000, max_c=1000, max_m=2000, max_val=10**9)
        ans_count, ans_cost = solve(a, b, c, mouses)
        
        with open(f"{i:01d}.in", "w", encoding="utf-8") as f_in:
            f_in.write(format_input(a, b, c, m, mouses) + "\n")
            
        with open(f"{i:01d}.out", "w", encoding="utf-8") as f_out:
            f_out.write(f"{ans_count} {ans_cost}\n")
            
        print(f"Gerado: test_{i:02d}.in e test_{i:02d}.out (m = {m})")
