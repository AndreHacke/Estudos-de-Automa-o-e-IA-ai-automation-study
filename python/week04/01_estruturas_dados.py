"""
Dia 4 - Estruturas de Dados
Tema: list, tuple, dict, set - quando usar cada uma

list  -> mutavel, tamanho dinamico, permite duplicados, ordenada
tuple -> tamanho fixo, ordenada, SEM append/remove (imutavel)
dict  -> pares chave-valor, otima pra busca por chave
set   -> so guarda valores unicos (sem duplicados), NAO e ordenado
"""

minha_lista = ["lista", "a", "b"]
minha_tupla = ("andre", "carlos", "neco")
meu_dicionario = {"nome": "guilherme", "idade": 27}
meu_conjunto = {"andre", "joao", "carlos"}

# ---------- Dicionario ----------

print(meu_dicionario["nome"])  # busca direto pela chave
print(len(meu_dicionario))     # quantidade de pares chave-valor

if "guilherme" in meu_dicionario.values():
    print("Guilherme ta aqui")

for valor in meu_dicionario.values():
    print(valor)

for chave in meu_dicionario.keys():
    print(chave)

# .items() percorre chave E valor ao mesmo tempo (mais usado na pratica)
for chave, valor in meu_dicionario.items():
    print(chave, "->", valor)

meu_dicionario["nome"] = "andre"                  # altera o valor de uma chave existente
meu_dicionario["endereco"] = "rua x da silva, 23"  # adiciona uma chave nova

print(meu_dicionario)

# .get() evita erro quando a chave nao existe - permite um valor padrao
print(meu_dicionario.get("telefone", "nao cadastrado"))

print("---")

# ---------- Conjunto (set) ----------

conjunto_vazio = set()  # forma correta de abrir um set vazio ({} cria um dict!)

meu_conjunto.add("felipe")
meu_conjunto.add("felipe")  # nao adiciona de novo, set nao aceita duplicado

if "felipe" in meu_conjunto:
    print("felipe foi encontrado")

meu_conjunto.remove("joao")

print(meu_conjunto)
# a pesquisa em um set e mais rapida que em uma lista: por baixo dos panos
# ele usa uma tabela hash, entao nao precisa percorrer item por item.
