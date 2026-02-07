# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve no Jovem Finn? |
|---------|---------|---------------------|
| `perfil_investidor.json` | JSON | Perfil personalizado com informações e limitações do próprio usuário |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente para melhores sugestões |

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

```python
import pandas as pd
import json

# transacoes.csv
transacoes = pd.read_csv("../data/transacoes.csv")

# perfil_investidor.json
with open("../data/perfil_investidor.json", "r", encoding="utf-8") as f:
  perfil = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados estarão armazenados no prompt do cliente. As informações principais utilizadas para gerar uma resposta adequada são:

```text
PERFIL DO CLIENTE:
  - Detalhes do cliente (renda, perfil, objetivos, patrimônio, riscos)
TRANSAÇÕES RECENTES:
  - Detalhe de transações (receita recebida, gastos já realizados (em categoria de prioridade), saldo restante)
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Abaixo está um exemplo de contexto, com base nos arquivos presentes na pasta `data/` no projeto

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
