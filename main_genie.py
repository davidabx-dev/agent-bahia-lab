import os
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents.agent_types import AgentType

load_dotenv()

print("⏳ Conectando ao Banco de Dados de Vendas...")

# 1. Conecta no Banco
db = SQLDatabase.from_uri("sqlite:///vendas_casas_bahia.db")

# 2. Configura o Cérebro (Llama 8B)
llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")

# 3. Cria o Agente SQL (Modo REATIVO - Mais compatível com Groq)
# Mudamos o agent_type para ZERO_SHOT_REACT_DESCRIPTION
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True # Se ele errar a formatação, ele tenta se corrigir
)

print("--- 🧞 GENIE BAHIA ONLINE (Modo Compatível) ---")
print("Pergunte sobre as vendas. Ex: 'Qual o total vendido de iPhones?'")

while True:
    pergunta = input("\nPergunte ao Diretor: ")
    if pergunta.lower() in ["sair", "exit"]:
        break
    
    try:
        agent_executor.invoke({"input": pergunta})
    except Exception as e:
        print(f"Erro: {e}")