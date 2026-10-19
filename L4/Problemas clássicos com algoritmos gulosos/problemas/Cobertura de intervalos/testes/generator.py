import random
import os
import zipfile

def solve(n, m, intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))
    ans = 0
    curr_end = 0
    i = 0
    while curr_end < m:
        max_end = -1
        while i < n and intervals[i][0] <= curr_end:
            max_end = max(max_end, intervals[i][1])
            i += 1
        if max_end <= curr_end:
            return -1
        curr_end = max_end
        ans += 1
    return ans

def generate_test_case(n, m, case_type):
    intervals = []
    
    if case_type == "missing_start":
        # Nenhum intervalo começa em 0
        for _ in range(n):
            l = random.randint(1, m)
            r = random.randint(l, m)
            intervals.append((l, r))
            
    elif case_type == "missing_end":
        # Nenhum intervalo chega em M
        for _ in range(n):
            l = random.randint(0, m - 1)
            r = random.randint(l, m - 1)
            intervals.append((l, r))
            
    elif case_type == "exact_cover":
        # Intervalos adjacentes perfeitos
        step = max(1, m // n)
        curr = 0
        while len(intervals) < n and curr < m:
            proximo = min(m, curr + step)
            intervals.append((curr, proximo))
            curr = proximo
        # Preenche o resto com lixo
        while len(intervals) < n:
            l = random.randint(0, m)
            r = random.randint(l, m)
            intervals.append((l, r))
            
    elif case_type == "single_perfect":
        # Um intervalo salva tudo
        intervals.append((0, m))
        for _ in range(n - 1):
            l = random.randint(0, m)
            r = random.randint(l, m)
            intervals.append((l, r))
            
    elif case_type == "only_points":
        # Apenas intervalos de tamanho 0
        for _ in range(n):
            pt = random.randint(0, m)
            intervals.append((pt, pt))
            
    elif case_type == "guaranteed_random":
        atual = 0
        while atual < m and len(intervals) < n:
            passo = random.randint(1, max(1, (m - atual) // (n // 2 + 1) + 10))
            proximo = min(m, atual + passo)
            intervals.append((atual, proximo))
            sobreposicao = random.randint(0, max(0, (proximo - atual) // 2))
            atual = proximo - sobreposicao
            if proximo == m:
                break
        while len(intervals) < n:
            l = random.randint(0, m)
            r = random.randint(l, m)
            intervals.append((l, r))
            
    else: # "random"
        for _ in range(n):
            l = random.randint(0, m)
            r = random.randint(l, m)
            intervals.append((l, r))

    intervals = intervals[:n]
    ans = solve(n, m, list(intervals))
    random.shuffle(intervals)
    
    in_text = f"{n} {m}\n" + "\n".join(f"{l} {r}" for l, r in intervals)
    out_text = str(ans)
    
    return in_text, out_text

# Configurações dos testes: (N, M, Tipo, Nome/Descricao)
test_configs = [
    (1, 1, "guaranteed_random"),          # 1: Menor caso possivel
    (100, 200, "guaranteed_random"),      # 5: Aleatorio com solucao 
    (100, 200, "guaranteed_random"),      # 5: Aleatorio com solucao 
    (100, 200, "guaranteed_random"),      # 5: Aleatorio com solucao 
    (100, 100, "missing_start"),          # 2: Falta o começo
    (100, 100, "missing_end"),            # 3: Falta o final
    (100, 100, "exact_cover"),            # 4: Cobertura exata sem sobreposicao
    (100, 100, "only_points"),            # 6: Apenas pontos
    (10000, 10**9, "exact_cover"),        # 7: Exato grande
    (10000, 10**9, "missing_start"),      # 8: Falta o comeco grande
    (10000, 10**9, "guaranteed_random"),  # 9: Aleatorio com solucao (Grande)
    (10000, 10**9, "random")              # 10: Aleatorio (Grande)
]

files_to_zip = []
for i, (n, m, t) in enumerate(test_configs, 1):
    in_str, out_str = generate_test_case(n, m, t)
    
    in_name = f"{i}.in"
    out_name = f"{i}.out"
    
    with open(in_name, "w") as f: f.write(in_str)
    with open(out_name, "w") as f: f.write(out_str + "\n")
    
    files_to_zip.extend([in_name, out_name])

# zip_filename = "casos_com_corner_cases.zip"
# with zipfile.ZipFile(zip_filename, 'w') as zipf:
#     for f in files_to_zip:
#         zipf.write(f)

# print(f"Zip generated: {zip_filename}")