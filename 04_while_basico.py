"""
Dia 2 - Loops
Tema: while

Sintaxe:
    while condicao:
        # codigo a ser executado

O while roda enquanto a condicao for verdadeira. Diferente do for
(que percorre uma colecao ja definida), o while e usado quando nao
sabemos de antemao quantas vezes o codigo vai rodar.
"""

# Exemplo 1: permitir 3 tentativas antes de encerrar
tentativas = 0
while tentativas < 3:
    print("Tente novamente")
    tentativas = tentativas + 1

print("---")

# Exemplo 2: repetir ate que um criterio seja satisfeito
# (so sai do loop quando a senha digitada for "teste123")
senha = "0"
while senha != "teste123":
    senha = input("Digite sua senha: ")
print("Bem vindo")

print("---")

# Exemplo 3: garantir que um valor seja preenchido (nao aceita vazio)
nome = ""
while nome == "":
    nome = input("Digite seu nome: ")
print(f"Bem vindo {nome}")

print("---")

# Exemplo 4: contador em um laço while
# Ex.: avisar as 17h que e hora do por do sol, contando hora a hora
horario = 0
while horario <= 17:
    print(horario)
    horario = horario + 1
print("Hora de ver o por do sol")
