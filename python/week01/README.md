# Semana 1 — Python Fundamentos

Parte do plano de estudos **IA + Automação** (24/08/2026 a 31/12/2026), cujo objetivo final é
desenvolver automações com Python, APIs, n8n, IA, bancos de dados e Docker.

## Dia 1 — Fundamentos

**O que estudei:** variáveis, tipos de dados (`int`, `float`, `string`, `bool`), `print()`,
`input()`, condicionais (`if` / `elif` / `else`) e a metodologia **5Q's** para estruturar um
algoritmo antes de escrever código.

### Metodologia 5Q's

Antes de sair escrevendo código, respondo 5 perguntas:

1. Quais são os dados de entrada necessários?
2. O que devo fazer com esses dados?
3. Quais são as restrições do problema?
4. Qual é o resultado esperado?
5. Qual a sequência de passos para chegar nesse resultado (pseudocódigo)?

### Exercícios

| Arquivo | O que faz |
|---|---|
| `01_variaveis_e_tipos.py` | Introdução a variáveis e aos 4 tipos básicos de dado |
| `02_valor_hora.py` | Calcula o valor/hora de um funcionário a partir do salário mensal e horas trabalhadas |
| `03_condicionais_pizza.py` | Cadeia de `if/elif/else` para decidir se "pode comer mais uma fatia" |
| `04_maior_valor.py` | Compara dois valores inseridos pelo usuário e exibe o maior |

### Como rodar

```bash
python3 01_variaveis_e_tipos.py
python3 02_valor_hora.py
python3 03_condicionais_pizza.py
python3 04_maior_valor.py
```

### Aprendizados

- Uma cadeia de `elif` deve ter o caso **mais comum primeiro**, por questão de performance.
- Nomes de variáveis em Python seguem `snake_case` minúsculo (PEP8) — evitar `Nome`, usar `nome`.
- Pensar no problema em 5 perguntas antes de codar evita ficar "codando no escuro".

---
*Próximo passo: Dia 2 — Loops (`for`, `while`, `range()`).*
