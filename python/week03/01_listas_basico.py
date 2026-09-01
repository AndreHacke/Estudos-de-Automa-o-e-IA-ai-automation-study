"""
Dia 3 - Listas
Tema: fundamentos de listas

Uma lista guarda itens em posicoes numeradas (indices), comecando do 0.
"""

precos = [20, 50, 100]
# indices:  0   1   2

print(precos[2])  # acessa pelo indice -> 100

# Como encontrar o indice de um item automaticamente, sem contar na mao:
nomes = ["andre", "joao", "lucas"]

print(nomes.index("joao"))  # retorna a posicao onde 'joao' esta -> 1
