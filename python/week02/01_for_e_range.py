"""
Dia 2 - Loops
Tema: for e range()

Sintaxe:
    for item in colecao:
        # comando

range() gera uma sequencia de numeros automatica.
Importante: o range NUNCA inclui o ultimo numero.
"""

# range(10) -> vai de 0 a 9
for item in range(10):
    print(item)

print("---")

# range com inicio e fim -> range(1, 11) vai de 1 a 10
for item in range(1, 11):
    print(item)

print("---")

# range com passo (terceiro parametro) -> pula de 2 em 2
for item in range(1, 11, 2):
    print(item)
