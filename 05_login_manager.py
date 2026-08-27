"""
Dia 2 - Loops
Projeto: Gerenciador de login simples, com maximo de 3 tentativas

Regras:
- Usuario e senha permitidos: andre / teste123
- Apos 3 tentativas erradas: "Aguarde 30 minutos e tente novamente!"
- Se acertar usuario e senha: "Login feito com sucesso"

Metodologia 5Q's:
1. Dados de entrada: usuario e senha
2. O que fazer: comparar com o usuario e senha permitidos
3. Restricoes: precisa ter usuario e senha; ambos devem bater com o
   permitido; apenas 3 chances
4. Resultado esperado: login aceito OU mensagem de espera de 30 min
5. Pseudocodigo:
   - definir user e senha corretos
   - solicitar usuario e senha
   - comparar
   - limitar por 3 tentativas
   - exibir mensagem final
"""

tentativas = 0
user = ""
senha = ""

while (user != "andre" or senha != "teste123") and tentativas < 3:
    user = input("Digite seu user: ")
    senha = input("Digite sua senha: ")
    tentativas = tentativas + 1

if user == "andre" and senha == "teste123":
    print("Login feito com sucesso")
else:
    print("Aguarde 30 minutos")
