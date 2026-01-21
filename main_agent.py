import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

# 1. Configurações
load_dotenv()
print("⏳ Iniciando Agente Autônomo (Modo ReAct)...")

# 2. Ferramentas
search = DuckDuckGoSearchRun()
tools = [search]

# 3. Cérebro (LLM)
llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")

# 4. O Prompt "Manual" (Ensinando a IA a pensar passo-a-passo)
template = '''
Responda às perguntas o melhor que puder. Você tem acesso às seguintes ferramentas:

{tools}

Use o seguinte formato EXATAMENTE:

Question: a pergunta que você deve responder
Thought: você deve sempre pensar sobre o que fazer
Action: a ação a ser tomada, deve ser uma de [{tool_names}]
Action Input: a entrada para a ação (ex: o termo de busca)
Observation: o resultado da ação
... (esse ciclo Thought/Action/Action Input/Observation pode se repetir N vezes)
Thought: agora eu sei a resposta final
Final Answer: a resposta final para a pergunta original (em Português)

Comece!

Question: {input}
Thought:{agent_scratchpad}
'''

prompt = PromptTemplate.from_template(template)

# 5. Criando o Agente
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

print("--- 🕵️ AGENTE 007 ONLINE ---")
print("Pergunte sobre cotações, notícias ou fatos atuais.")

while True:
    pergunta = input("\nSua Pergunta: ")
    if pergunta.lower() in ["sair", "exit"]:
        break
    
    try:
        agent_executor.invoke({"input": pergunta})
    except Exception as e:
        print(f"Erro: {e}")