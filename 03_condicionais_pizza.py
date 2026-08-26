"""
Dia 1 - Fundamentos de Python
Tema: condicionais (if / elif / else)

Regra: "posso comer mais uma fatia de pizza?"
- Se ja comeu 3 ou mais: nao
- Se comeu 2: pode, mas so mais uma
- Se comeu 1: pode tranquilo
- Se nao comeu nenhuma: vai que e sua

Obs: o caso mais comum fica primeiro na cadeia de if/elif
por questao de performance (economiza comparacoes).
"""

fatias_de_pizza = int(input("Quantas fatias de pizza voce comeu: "))

if fatias_de_pizza >= 3:
    print("Melhor nao comer mais, pensa nos amigos")
elif fatias_de_pizza == 2:
    print("Pode, mas so mais uma")
elif fatias_de_pizza == 1:
    print("Vai nessa, tem mais 2 fatias pra voce ainda")
else:
    print("Vai que e sua")


# Segundo exemplo de condicional (versao corrigida do rascunho original,
# que tinha um bug: um "else" sem "if" correspondente)
trabalho_terminado = True

if trabalho_terminado:
    print("Bora la, que eu ja terminei aqui")
else:
    print("Nao terminei a tempo, peca ajuda pro meu irmao")
