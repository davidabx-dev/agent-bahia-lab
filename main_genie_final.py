import os
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

load_dotenv()

print("⏳ Conectando ao Banco de Dados (Modo Chain)...")

# 1. Conecta no Banco
db = SQLDatabase.from_uri("sqlite:///vendas_casas_bahia.db")

# 2. Configura o Cérebro
llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")

# 3. Cria a Corrente SQL (Direto ao ponto: Texto -> SQL -> Resposta)
# Isso evita que ele fique rodando em círculos tentando "adivinhar" ferramentas
db_chain = SQLDatabaseChain.from_llm(
    llm,
    db,
    verbose=True, # Mostra o SQL sendo criado
    use_query_checker=True # Ajuda a corrigir erros de SQL
)

print("--- 🧞 GENIE BAHIA (Versão Final) ONLINE ---")
print("Exemplo: 'Qual o faturamento total com iPhones?'")

while True:
    pergunta = input("\nPergunte ao Diretor: ")
    if pergunta.lower() in ["sair", "exit"]:
        break
    
    try:
        # A corrente roda direto
        db_chain.invoke(pergunta)
    except Exception as e:
        print(f"Erro: {e}")