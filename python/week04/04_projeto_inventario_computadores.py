"""
Dia 4 - Estruturas de Dados
Projeto: Inventario de Computadores

Cria um inventario usando um dicionario de dicionarios, onde cada
computador tem host, RAM e armazenamento. Percorre todos e exibe um
relatorio, alem de demonstrar a busca segura com .get().
"""

computadores = {
    "computador_1": {"host": "DSK01", "RAM": "8GB", "armazenamento": "128GB"},
    "computador_2": {"host": "DSK02", "RAM": "16GB", "armazenamento": "228GB"},
    "computador_3": {"host": "DSK03", "RAM": "12GB", "armazenamento": "512GB"},
}

# Relatorio de todos os computadores
for key, value in computadores.items():
    print(
        f"O {key} é o host: {value['host']} com RAM: {value['RAM']} "
        f"e armazenamento: {value['armazenamento']}"
    )

print("---")

# Busca direta por uma chave que existe
print(computadores.get("computador_1"))

# Busca por uma chave que NAO existe, com valor padrao
# (isso evita um KeyError, que aconteceria usando computadores['computador_9'])
print(computadores.get("computador_9", "Computador não encontrado no inventário"))
