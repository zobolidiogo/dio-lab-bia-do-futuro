# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Cenários de Teste

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de gasto/economia
- **Pergunta:** "Eu quero comprar algo que não irei usar e está fora da curva para minha renda e gastos, devo prosseguir?"
- **Resposta esperada:** Recomendação de não prosseguimento com algo fora da curva para o cliente
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de controle de custos
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto é um carro novo?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente conseguiu interpretar corretamente o histórico de transações e calcular gastos por categoria.
- As respostas seguiram o perfil do cliente, evitando sugestões arriscadas para um usuário conservador.
- O sistema respeitou as regras de segurança, admitindo quando não possuía informação suficiente.
- A linguagem se manteve simples e próxima do público jovem, coerente com a persona “Jovem Finn”.
- O agente demonstrou capacidade de alertar sobre gastos fora do padrão e risco de extrapolar o orçamento mensal.

**O que pode melhorar:**
- O modelo local possui limitações para cálculos mais complexos e pode interpretar valores de forma aproximada.
- Ainda não há autenticação real de usuário, os dados são estáticos e simulados.
- Falta um mecanismo automático para calcular “saldo restante do mês” de forma programática.
- Não existe histórico de conversas para aprendizado contínuo.
- A validação anti-alucinação é baseada apenas em regras de prompt, sem camada técnica robusta.
- Dependendo do modelo e capacidade do computador, as respostas podem demorar muito para serem geradas.

Apesar das limitações de um protótipo acadêmico, o agente demonstrou viabilidade como ferramenta de educação financeira para jovens, cumprindo o objetivo de apoiar decisões de consumo com base em dados reais do usuário e regras de segurança contra alucinações.
