"""
Dia 3 - Listas / Loops
Projeto 1: Fatorial de um numero

Cria um programa que recebe um numero e imprime seu fatorial.
(fatorial de N = N x (N-1) x (N-2) x ... x 1)

Metodologia 5Q's:
1. Dados de entrada: o numero que queremos o fatorial
2. O que fazer: multiplicar pelos numeros inteiros anteriores, ate chegar a 1
3. Restricoes: precisa ter um numero; multiplicar pelos anteriores ate 1
4. Resultado esperado: exibir o resultado da multiplicacao
5. Pseudocodigo:
   - receber o numero
   - multiplicar ele pelos antecessores ate 1
   - exibir o valor
"""

fatorial = 1

valor = int(input("Me de o valor que precisa do fatorial: "))

for casa in range(valor, 0, -1):  # percorre de 'valor' ate 1, decrescendo
    fatorial = fatorial * casa

print(f"O seu valor fatorial e de {fatorial}")
