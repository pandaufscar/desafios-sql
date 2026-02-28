import sqlite3

# Cria o banco e cursor
conn = sqlite3.connect("dados.db")
cursor = conn.cursor()

# Lê, executa e fecha
with open("dados.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()
cursor.executescript(sql_script)
conn.commit()
conn.close()