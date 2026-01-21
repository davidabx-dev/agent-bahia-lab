import sqlite3

# 1. Conecta (cria) o banco de dados
conn = sqlite3.connect("vendas_casas_bahia.db")
cursor = conn.cursor()

# 2. Cria a tabela de Vendas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY,
    produto TEXT,
    categoria TEXT,
    preco REAL,
    quantidade INTEGER,
    data_venda TEXT
)
""")

# 3. Insere dados de exemplo (As "Vendas" de ontem e hoje)
# Vamos colocar iPhone, Geladeira, Air Fryer...
dados = [
    ("iPhone 15", "Celulares", 5000.00, 10, "2026-01-20"),
    ("Geladeira Brastemp", "Eletrodomesticos", 3500.00, 5, "2026-01-20"),
    ("Air Fryer Mondial", "Eletroportateis", 400.00, 50, "2026-01-19"),
    ("Smart TV Samsung 55", "Eletronicos", 2800.00, 8, "2026-01-20"),
    ("Notebook Galaxy Book", "Informatica", 4500.00, 3, "2026-01-21")
]

cursor.executemany("INSERT INTO vendas (produto, categoria, preco, quantidade, data_venda) VALUES (?, ?, ?, ?, ?)", dados)
conn.commit()
print("✅ Banco de dados 'vendas_casas_bahia.db' criado com sucesso!")
print(f"{len(dados)} vendas registradas.")
conn.close()