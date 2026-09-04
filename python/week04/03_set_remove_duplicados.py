"""
Dia 4 - Estruturas de Dados
Tema: removendo duplicados de uma lista com set()

Truque comum no dia a dia: converter a lista pra set (que so aceita
valores unicos) e depois converter de volta pra lista.
"""

numeros = [1, 2, 2, 3, 3, 3, 4]

sem_duplicados = list(set(numeros))

print(sem_duplicados)
