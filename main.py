import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Carrega a chave do arquivo .env
load_dotenv()

# 2. Configura o Modelo (Llama 3 via Groq)
chat = ChatGroq(
    temperature=0.3, # Mais baixo para ser mais preciso/profissional
    model_name="llama-3.1-8b-instant"
)

# 3. O "Persona" da Casas Bahia
# Aqui definimos que ele é um Especialista de Dados da empresa
system_instruction = """
Você é o 'Agente Bahia', o assistente oficial de dados do Grupo Casas Bahia.
Sua missão é auxiliar na análise técnica e explicar conceitos de IA e Dados.
Responda sempre de forma profissional, direta e técnica.
Se perguntarem quem é você, diga que é um agente baseado em LLM orquestrado via LangChain.
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_instruction),
    ("user", "{input}")
])

# 4. A Corrente (Chain) - Onde a mágica acontece
chain = prompt_template | chat | StrOutputParser()

# 5. Loop de Execução
print("--- 🧢 AGENTE BAHIA INICIADO (LangChain Ativo) ---")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("👤 Recrutador/Você: ")
    if pergunta.lower() in ["sair", "exit"]:
        break
    
    print("⏳ Processando no Databricks/LangChain...")
    try:
        resposta = chain.invoke({"input": pergunta})
        print(f"🤖 Agente Bahia: {resposta}\n")
    except Exception as e:
        print(f"❌ Erro: {e}")