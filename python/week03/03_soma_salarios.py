"""
Dia 3 - Listas
Problema: gastos totais com pagamento de salarios da empresa.

Dada uma lista de salarios, calcular o total pago a todos os funcionarios.

Metodologia 5Q's:
1. Dados de entrada: uma lista de salarios
2. O que fazer: somar todos ate o final da lista
3. Restricoes: precisa ter uma lista
4. Resultado esperado: a soma de todos os salarios
5. Pseudocodigo:
   - receber a lista de salarios
   - somar todos os salarios ate obter o total
   - exibir o total gasto com pagamentos
"""

salarios = [2500, 900, 5000, 7500]
total = 0

for salario in salarios:  # percorre todos os valores da lista
    total = total + salario  # soma acumulada ate acabar a lista

print(total)
