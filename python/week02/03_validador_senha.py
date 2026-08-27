"""
Dia 2 - Loops
Problema: Validador de senhas

Um sistema precisa verificar se todas as senhas digitadas pelos usuarios
sao validas. Para ser valida, a senha precisa ter pelo menos 6 caracteres.

Metodologia 5Q's:
1. Dados de entrada: a senha
2. O que fazer: verificar a quantidade de caracteres
3. Restricoes: precisa ter uma senha; precisa ter >= 6 caracteres
4. Resultado esperado: senha aprovada ou recusada
5. Pseudocodigo:
   - input de senha
   - analisar o tamanho
   - se >= 6 caracteres: aprovar
   - se < 6 caracteres: recusar

len(variavel) retorna a quantidade de caracteres de uma string.
"""

senhas = ["abc", "segura123", "12345", "teste123", "oi", "python13"]

for senha in senhas:
    if len(senha) >= 6:
        print(f"A senha '{senha}' possui a quantidade aceita de caracteres")
    else:
        print(f"A senha '{senha}' NAO possui a quantidade aceita de caracteres")
