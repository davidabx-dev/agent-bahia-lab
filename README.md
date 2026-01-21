# 🧞‍♂️ Agent Bahia Lab: RAG, Web Search & SQL Agents

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-Orchestration-green)
![Groq](https://img.shields.io/badge/Groq-Llama3-orange)
![SQL](https://img.shields.io/badge/SQL-Database-lightgrey)

Este repositório documenta a implementação de uma arquitetura completa de **Agentes Autônomos de IA**, focada em casos de uso Enterprise (como o Databricks Genie), utilizando **LangChain, Groq (Llama 3) e SQL**.

O projeto foi desenvolvido como uma Prova de Conceito (PoC) para demonstrar habilidades em Engenharia de IA Generativa.

---

## 🧠 O Que Foi Construído

O projeto consiste em um ecossistema com 3 agentes especializados que rodam localmente:

### 1. 📚 Agente RAG (Retrieval-Augmented Generation)
- **Arquivo:** `main_rag.py`
- **Função:** O agente ingere documentos de política interna (`regras_internas.txt`), cria embeddings vetoriais e responde perguntas com **Grounding** (ancoragem), garantindo conformidade com as regras da empresa e evitando alucinações.

### 2. 🌐 Agente Autônomo Web (ReAct Pattern)
- **Arquivo:** `main_agent_pro.py`
- **Função:** Um agente capaz de raciocinar (**Reason + Act**). Se o usuário pergunta algo que ele não sabe (ex: "Qual a cotação do Dólar agora?"), ele decide autonomamente consultar a web via API do **Tavily**, processar a resposta e entregar o dado atualizado.
- **Engenharia:** Implementação de travas de segurança (`max_iterations`) para controle de loop e custos.

### 3. 📊 Agente de Dados SQL (Genie Architecture)
- **Arquivo:** `main_genie_final.py`
- **Função:** Simulação de **Generative BI**. O agente conecta em um banco de dados SQL (SQLite), interpreta perguntas de negócio em linguagem natural e as converte em queries SQL complexas.
- **Exemplo Real:**
    - *Pergunta:* "Qual o valor total vendido (preço vezes quantidade) de iPhones?"
    - *Ação da IA:* Gera `SELECT SUM(preco * quantidade) FROM vendas WHERE produto = 'iPhone 15'`
    - *Resultado:* R$ 50.000,00 (Extraído diretamente do DB).

---

## 🛠️ Stack Tecnológico

- **LLM Engine:** Groq (Modelos Llama-3.3-70b & Llama-3.1-8b) - Foco em ultra-baixa latência.
- **Orquestração:** LangChain (Core, Community, Experimental).
- **Text-to-SQL:** `SQLDatabaseChain`.
- **Ferramentas:** Tavily (Search API), SQLite (Banco de Dados Relacional).
- **Ambiente:** Python, Virtualenv (`venv`), Git.

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone [https://github.com/davidabx-dev/agent-bahia-lab.git](https://github.com/davidabx-dev/agent-bahia-lab.git)
cd agent-bahia-lab
