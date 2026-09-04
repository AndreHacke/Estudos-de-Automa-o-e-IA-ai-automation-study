# Semana 1 (Dia 4) — Estruturas de Dados

Parte do plano de estudos **IA + Automação** (24/08/2026 a 31/12/2026).

## O que estudei

As 4 estruturas de dados fundamentais do Python — `list`, `tuple`, `dict` e
`set` — quando usar cada uma, seus métodos principais (`.get()`, `.items()`,
`.add()`, `.remove()`), desempacotamento de tupla, e como usar `set()` pra
remover duplicados de uma lista. Fechei com um projeto prático: um
inventário de computadores usando dicionário de dicionários.

### Quando usar cada estrutura

| Estrutura | Característica | Quando usar |
|---|---|---|
| `list` | Mutável, tamanho dinâmico, permite duplicados | Coleção que muda com frequência |
| `tuple` | Tamanho fixo, sem append/remove | Dados que não devem mudar (coordenadas, datas) |
| `dict` | Pares chave-valor | Busca rápida por identificador (nome, ID, host) |
| `set` | Só valores únicos, não ordenado | Eliminar duplicados, checar existência rápido |

### Exercícios

| Arquivo | O que faz |
|---|---|
| `01_estruturas_dados.py` | Visão geral das 4 estruturas + métodos de dict e set |
| `02_tupla_desempacotamento.py` | Desempacota uma tupla em variáveis separadas |
| `03_set_remove_duplicados.py` | Remove duplicados de uma lista convertendo pra `set` |
| `04_projeto_inventario_computadores.py` | **Projeto do dia**: inventário de computadores com busca segura via `.get()` |

### Como rodar

```bash
python3 01_estruturas_dados.py
python3 02_tupla_desempacotamento.py
python3 03_set_remove_duplicados.py
python3 04_projeto_inventario_computadores.py
```

### Aprendizados

- `dict.get(chave, valor_padrao)` evita `KeyError` quando a chave não existe
  — muito mais seguro que `dicionario[chave]` direto em código de produção.
- `.items()` é a forma mais usada de percorrer um dicionário na prática,
  porque já entrega chave e valor juntos, sem precisar buscar o valor
  separadamente dentro do loop.
- Um `set` vazio precisa ser criado com `set()`, nunca com `{}` — isso cria
  um dicionário vazio, não um conjunto.
- Converter `list(set(lista))` é o jeito mais rápido de remover duplicados,
  mas perde a ordem original dos itens (set não é ordenado).

---
*Próximo passo: Dia 5 — funções (`def`, `return`, parâmetros e argumentos).*
