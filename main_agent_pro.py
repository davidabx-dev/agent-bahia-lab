import os
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

# 1. Configurações
load_dotenv()
print("⏳ Iniciando Agente Especialista (Modelo Llama 8B)...")

# 2. Ferramentas
search = TavilySearchResults(max_results=1)
tools = [search]

# 3. Cérebro (Voltamos para o Llama 8B, que é rápido e grátis)
llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")

# 4. Prompt REFORÇADO (Para evitar loops)
template = '''
Responda à pergunta do usuário. Você tem acesso às seguintes ferramentas:

{tools}

Para usar uma ferramenta, você DEVE usar os nomes exatos das ferramentas: [{tool_names}].

Use o seguinte formato:

Question: a pergunta de entrada
Thought: o que devo fazer
Action: o nome da ferramenta (ex: tavily_search_results_json)
Action Input: o termo de busca
Observation: o resultado da ferramenta
... (repita se necessário)
Final Answer: a resposta final

IMPORTANTE:
- NÃO coloque colchetes no nome da Action.
- SE VOCÊ JÁ TEM A INFORMAÇÃO NA "OBSERVATION", PARE E DÊ O "FINAL ANSWER". NÃO BUSQUE DUAS VEZES A MESMA COISA.

Question: {input}
Thought:{agent_scratchpad}
'''

prompt = PromptTemplate.from_template(template)

# 5. Execução com Freio de Mão
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True,
    max_iterations=5 # <--- O FREIO: Se ele tentar mais que 5 vezes, o sistema para ele.
)

print("--- 🕵️ AGENTE LLAMA 8B ONLINE ---")
pergunta = input("O que você quer saber? (Ex: Cotação do Dólar): ")

try:
    agent_executor.invoke({"input": pergunta})
except Exception as e:
    # Se ele estourar o limite de passos, ele cai aqui, mas a gente vê o resultado no terminal antes
    print(f"O agente parou (limite de segurança atingido). Verifique o terminal acima.")