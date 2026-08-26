"""
Dia 1 - Fundamentos de Python
Problema: calcular o valor da hora de um funcionario com base no salario mensal.

Metodologia 5Q's para montar o algoritmo:
1. Quais sao os dados de entrada necessarios?
   - Salario mensal
   - Horas trabalhadas
2. O que devo fazer com estes dados?
   - Calcular o valor por hora trabalhada
3. Quais sao as restricoes do problema?
   - Precisa de um valor mensal
   - Precisa de uma quantidade de horas trabalhadas
4. Qual o resultado esperado?
   - O valor/hora da pessoa
5. Sequencia de passos (pseudocodigo):
   - receber valor mensal
   - receber quantidade de horas
   - dividir o valor mensal pela quantidade de horas = valor_hora
   - exibir valor_hora
"""

salario_mensal = input("Qual e o seu salario mensal: ")
horas_trabalhadas = input("Quantas horas voce trabalhou esse mes: ")

valor_hora = float(salario_mensal) / int(horas_trabalhadas)

print(f"Seu valor/hora e: R$ {valor_hora:.2f}")
