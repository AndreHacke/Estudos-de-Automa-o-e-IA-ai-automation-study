# Semana 1 (Dia 3) — Listas

Parte do plano de estudos **IA + Automação** (24/08/2026 a 31/12/2026).

## O que estudei

Fundamentos de listas em Python: indexação, `.index()`, `.append()`, e como
combinar listas com `for`/`while` para resolver problemas reais. Segui usando
a metodologia **5Q's** nos dois projetos maiores do dia.

### Exercícios

| Arquivo | O que faz |
|---|---|
| `01_listas_basico.py` | Indexação de listas e busca de posição com `.index()` |
| `02_manipulando_listas.py` | Adiciona um novo item a uma lista com `.append()` |
| `03_soma_salarios.py` | Soma o total de uma lista de salários com `for` |
| `04_projeto_fatorial.py` | **Projeto 1**: calcula o fatorial de um número usando `range()` decrescente |
| `05_jogo_adivinhacao.py` | **Projeto 2**: jogo de adivinhação (0–10) usando o módulo `random` |

### Como rodar

```bash
python3 01_listas_basico.py
python3 02_manipulando_listas.py   # pede input no terminal
python3 03_soma_salarios.py
python3 04_projeto_fatorial.py     # pede input no terminal
python3 05_jogo_adivinhacao.py     # pede input no terminal (chutes até acertar)
```

### Aprendizados

- Listas em Python começam no índice **0**, não no 1.
- `.index('valor')` evita precisar contar posição na mão.
- `.append()` adiciona item ao final da lista, sem precisar recriar ela.
- O fatorial ficou elegante com `range(valor, 0, -1)` — percorre do número
  escolhido até 1, decrescendo, sem precisar de lógica extra.
- `random.choice(lista)` sorteia um item de uma lista existente — alternativa
  ao `random.randint()`, útil quando os valores possíveis não são um range
  simples de inteiros.

---
*Próximo passo: Dia 4 — dicionários, tuplas e conjuntos.*
