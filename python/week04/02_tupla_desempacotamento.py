"""
Dia 4 - Estruturas de Dados
Tema: desempacotamento de tupla

Permite atribuir cada valor de uma tupla a uma variavel de uma vez so,
sem precisar acessar por indice (pessoa[0], pessoa[1]...).
"""

pessoa = ("andre", 28, "Curitiba")

nome, idade, cidade = pessoa

print(nome, idade, cidade)
