"""
Dia 2 - Loops
Tema: iterando listas com for (combinando com condicionais)

Uma lista pode conter qualquer tipo de dado: string, bool, int, etc.
"""

nomes = ["andre", "felipe", "joao", "paulo"]

for nome in nomes:
    print(nome)

print("---")

# Combinando lista + for + condicional em um unico codigo
idades = [13, 15, 18, 30, 50, 75]

for idade in idades:
    if idade >= 18:
        print(f"{idade} e maior de idade")
    else:
        print(f"{idade} e menor de idade")
