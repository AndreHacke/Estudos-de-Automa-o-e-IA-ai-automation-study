"""
Dia 3 - Listas / Loops
Projeto 2: Jogo de adivinhacao

Ao iniciar, o programa gera um valor aleatorio de 0 a 10 e permite ao
usuario chutar numeros ate acertar o valor gerado. O programa informa
se o chute foi maior ou menor que o valor sorteado.
"""

import random

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteio = random.choice(numeros)
tentativa = ""

while tentativa != sorteio:  # enquanto nao acertar, continua pedindo
    tentativa = int(input("Tenta adivinhar o numero escolhido de 0 a 10: "))

    if tentativa > sorteio:
        print("O numero escolhido e maior que o sorteado")
    elif tentativa < sorteio:
        print("O numero escolhido e menor que o sorteado")
    else:
        print("PARABENS, VOCE ACERTOU O NUMERO!")
