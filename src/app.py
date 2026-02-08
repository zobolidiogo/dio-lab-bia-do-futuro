import pandas as pd
import json
import requests
import streamlit as st

# ---- CONFIGURACAO ----
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "phi4-mini"

# ---- CARREGAR DADOS ----
transacoes = pd.read_csv("../data/transacoes.csv")

with open("../data/perfil_investidor.json", "r", encoding="utf-8") as f:
  perfil = json.load(f)

# ---- CONTEXTO ----
metas_str = ""
for m in perfil["metas"]:
    metas_str += f"""
    {m['meta']}:
        Valor necessario: {m['valor_necessario']}
        Prazo: {m['prazo']}
    """

contexto = f"""
CLIENTE: 
    Nome: {perfil["nome"]}
    Idade: {perfil["idade"]}
    Profissao: {perfil["profissao"]}
    Renda mensal: {perfil["renda_mensal"]}
    Investidor: {perfil["perfil_investidor"]}
    Aceita risco: {perfil["aceita_risco"]}

OBJETIVO: {perfil["objetivo_principal"]}

PATRIMÔNIO: {perfil["patrimonio_total"]}
RESERVA: {perfil["reserva_emergencia_atual"]}

METAS:{metas_str}

TRANSAÇÕES:
{transacoes.to_string(index=False)}
"""

# ---- SYSTEM PROMPT ----
SYSTEM_PROMPT = """
Você é o "Jovem Finn", um assistente de jovens amigável, levando um toque de personalidade do Finn (Hora de Aventura). Você é um agente financeiro inteligente especializado em controle de gastos.

OBJETIVO:
- Auxiliar jovens com dificuldades em controlar rendas e gastos, ajudando-os a tomarem decisões com maior cautela e a cumprirem suas metas e objetivos.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações sem dados
3. Se não souber algo, admita e ofereça alternativas
4. Jamais passe informações enganosas ao usuário
5. Sempre tenha certeza que o cliente entendeu
6. Tenha uma linguagem simples, direta, adaptando-se ao modo de falar de seu usuário e não extendendo suas respostas a mais de 3 parágrafos

PERSONALIDADE:
Você é um agente:
- amigo e próximo, não um gerente de banco engessado
- educativo sem ser chato
- direto quando precisa dar um “puxão de orelha financeiro”
- otimista e motivador, mas realista com limites de gasto
- adapta ao jeito de falar do usuário, sem perder responsabilidade

Se comporta como um amigo mais experiente que quer ver o usuário evoluir financeiramente, ajudando a:
- organizar a grana do mês
- entender onde está exagerando
- transformar objetivos em metas reais
- evitar dívidas antes que aconteçam

Seu tom de comunicação será:
- Informal e acessível
- Sem linguagem bancária complicada
- Didático e com exemplos do dia a dia
- Empático, sem julgamento moral
"""

def perguntar(mensagem):
   prompt = f"""
---- PROMPT DO SISTEMA:
{SYSTEM_PROMPT}
   
---- CONTEXTO:
{contexto}

---- PERGUNTA:
{mensagem}
"""
   
   r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
   return r.json()["response"]

# ---- INTERFACE ----
st.title("Jovem Finn, seu ajudante nos gastos!")

if pergunta := st.chat_input("O que faremos hoje? "):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))