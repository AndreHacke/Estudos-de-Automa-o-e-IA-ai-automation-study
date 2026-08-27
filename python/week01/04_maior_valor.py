"""
Dia 1 - Fundamentos de Python
Problema: receber dois valores e exibir qual e o maior entre eles.

Metodologia 5Q's:
1. Dados de entrada: valor A e valor B
2. O que fazer: comparar qual dos dois e maior
3. Restricoes: precisa de um valor A e de um valor B
4. Resultado esperado: o maior valor entre os dois
5. Pseudocodigo:
   - inserir valor A
   - inserir valor B
   - comparar qual dos dois e maior
   - exibir o maior valor
"""

valor_a = int(input("Insira o seu primeiro valor: "))
valor_b = int(input("Insira o seu segundo valor: "))

if valor_a == valor_b:
    print("Os valores sao iguais")
elif valor_a > valor_b:
    print("O maior valor e:", valor_a)
else:
    print("O maior valor e:", valor_b)
