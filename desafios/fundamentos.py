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
    "resposta_sql": resposta_sql,
    "ordem": False
}

titulo = "Produtos com estoque baixo"
enunciado = "Liste o nome e o estoque dos produtos com estoque menor que 50."
imagem_esquema = "schema.png"
resposta_sql = """
SELECT nome, estoque
FROM produtos
WHERE estoque < 50
"""
dic2 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

titulo = "Clientes nascidos no século 21"
enunciado = "Liste o nome dos clientes que nasceram no século 21."
imagem_esquema = "schema.png"
resposta_sql = """
SELECT nome
FROM clientes
WHERE data_nascimento >= '2001-01-01'
"""
dic3 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

dics = [dic1, dic2, dic3]