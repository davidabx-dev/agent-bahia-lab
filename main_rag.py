import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# Carrega chaves
load_dotenv()
print("⏳ Carregando cérebro do Agente Bahia...")

# 1. Carrega o documento
loader = TextLoader("regras_internas.txt", encoding="utf-8")
documentos = loader.load()

# 2. Quebra o texto
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs_processados = text_splitter.split_documents(documentos)

# 3. Cria a Memória Vetorial (A parte que demorou pra instalar faz isso aqui)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs_processados, embeddings)
retriever = vectorstore.as_retriever()

# 4. Configura o Modelo
llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")

# 5. Prompt de RAG (Grounding)
prompt_template = ChatPromptTemplate.from_template("""
Você é o assistente técnico da Casas Bahia.
Responda com base APENAS no contexto abaixo.
<contexto>
{context}
</contexto>
Pergunta: {input}
""")

# 6. Cria a Chain
document_chain = create_stuff_documents_chain(llm, prompt_template)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

print("--- 🧠 SISTEMA RAG ONLINE ---")
while True:
    pergunta = input("\nSua Pergunta: ")
    if pergunta.lower() in ["sair", "exit"]:
        break
    response = retrieval_chain.invoke({"input": pergunta})
    print(f"🤖 Agente Bahia: {response['answer']}")