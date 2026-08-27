# Semana 1 (Dia 2) — Loops

Parte do plano de estudos **IA + Automação** (24/08/2026 a 31/12/2026).

## O que estudei

`for`, `range()` (com início, fim e passo), iteração de listas combinada
com condicionais, `while`, uso de contadores em laços, e como usar `len()`
para validar tamanho de dados. Segui usando a metodologia **5Q's** pra
estruturar os dois problemas práticos do dia.

### Exercícios

| Arquivo | O que faz |
|---|---|
| `01_for_e_range.py` | `for` + `range()` — sequência simples, com início/fim e com passo |
| `02_listas_com_for.py` | Percorre listas de nomes e idades, combinando `for` + `if` |
| `03_validador_senha.py` | Valida se senhas de uma lista têm pelo menos 6 caracteres (`len()`) |
| `04_while_basico.py` | Contador de tentativas, loop até condição satisfeita, contador de horário |
| `05_login_manager.py` | **Projeto do dia**: gerenciador de login com limite de 3 tentativas |

### Como rodar

```bash
python3 01_for_e_range.py
python3 02_listas_com_for.py
python3 03_validador_senha.py
python3 04_while_basico.py   # pede input no terminal
python3 05_login_manager.py  # pede input no terminal (usuário: andre / senha: teste123)
```

### Aprendizados

- `range()` nunca inclui o último número: `range(1, 11)` vai de 1 a 10.
- `for` é ideal quando já sabemos a coleção a percorrer; `while` é ideal
  quando não sabemos quantas repetições serão necessárias (depende de
  uma condição).
- Dá pra combinar lista + loop + condicional no mesmo bloco de código,
  sem precisar de estruturas separadas.
- No gerenciador de login, a condição do `while` combina duas coisas ao
  mesmo tempo — `(credenciais erradas) and (tentativas < 3)` — o loop só
  continua enquanto as duas forem verdadeiras.

---
*Próximo passo: Dia 3 — mais estruturas (ou revisão + projeto da semana).*
