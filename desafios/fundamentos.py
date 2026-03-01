titulo = "Selecionando colunas"

enunciado = "Liste o nome e a cidade de todos os clientes."

imagem_esquema = "schema.png"

resposta_sql = """
SELECT nome, cidade
FROM clientes
"""

dic1 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql
}

dics = [dic1]