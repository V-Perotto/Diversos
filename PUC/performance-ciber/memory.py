# Alunos:
# - Marianna Bove de Mello
# - Tiago Yukio Izumi
# - Vittorio Perotto

def calcular_taxa_de_acertos(total_hit, total_pos_memory):
    taxa = total_hit / total_pos_memory * 100
    formated_tax = "{:.2f}".format(taxa)
    return f"{formated_tax}%"

def inicializar_cache(tamanho_cache):
    cache = []
    for i in range(tamanho_cache):
        address = {}
        address["pos_cache"] = i
        address["pos_memory"] = -1
        cache.append(address)
    return cache

def imprimir_cache(cache):
    print("Cache Inicial")
    print(f"Tamanho Cache: \t{len(cache)}")
    print("Pos. Cache | Pos. Memory")
    for addresses in cache:
        # print(addresses.items())
        print(f"""\t{addresses["pos_cache"]}  |\t{addresses["pos_memory"]}""")

def is_hit(hit):
    if hit:
        print(f"Status: HIT")
    else:
        print(f"Status: MISS")

def imprimir_enderecos(cache):
    print(f"Tamanho Cache: \t{len(cache)}")
    print("Pos. Cache | Pos. Memory")
    for addresses in cache:
        print(f"""\t{addresses["pos_cache"]}  |\t{addresses["pos_memory"]}""")

def imprimir_resultado(pos_memory, total_hit, total_miss):
    print("\n Conectividade em Sistemas Ciberfisicos - Mapeamento Direto")
    print(f"*{25*'-'}*")
    print(f"- Total de posições de memórias acessadas: {len(pos_memory)}")
    print(f"- Total de hits: {total_hit}")
    print(f"- Total de misses: {total_miss}")
    print(f"- Taxa de cache hit: {calcular_taxa_de_acertos(total_hit, len(pos_memory))}")

def mapeamento_direto(tamanho_cache, pos_memory: list):
    cache = inicializar_cache(tamanho_cache)
    imprimir_cache(cache)

    total_miss = 0
    total_hit = 0

    for i in range(len(pos_memory)):
        hit = False

        pos_cache = pos_memory[i] % tamanho_cache

        print(f"\nLinha {i} | Posição de memória desejada: {pos_memory[i]}")
        for addresses in cache:
            if addresses["pos_cache"] == pos_cache:
                if addresses["pos_memory"] == pos_memory[i]:
                    total_hit += 1
                    hit = True
                else:
                    addresses["pos_memory"] = pos_memory[i]
                    total_miss += 1
                    hit = False
        is_hit(hit)
        imprimir_enderecos(cache)
    imprimir_resultado(pos_memory, total_hit, total_miss)

# Exemplo
mapeamento_direto(5, [33,3,11,5])

# 5 - a
mapeamento_direto(5, [0,1,2,3,1,4,5,6])

# 5 - a
mapeamento_direto(5, [0,1,2,2,22,32,42,20,1,10,11,12,13])

# 5 - b
mapeamento_direto(5, [1,6,1,11,1,16,1,21,1,26])

# 5 - c
mapeamento_direto(5, [2,7,2,12,2,17])