titulo = "1. Selecionando colunas"

enunciado = "Liste o nome e a cidade de todos os clientes."

imagem_esquema = "schema.jpg"

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

titulo = "2. Produtos que valem mais de 50 reais"
enunciado = "Liste nome e preço dos produtos com preço maior que 50."
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT nome, preco
FROM Produtos
WHERE preco > 50
"""
dic2 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

titulo = "3. Clientes nascidos no século 21"
enunciado = "Liste o nome dos clientes que nasceram no século 21."
imagem_esquema = "schema.jpg"
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

titulo = "4. Filtre por estoque e preço"
enunciado = "Liste o nome, preço e estoque dos produtos com preço maior que 30 e estoque maior que 5."
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT nome, preco, estoque
FROM Produtos
WHERE preco > 30 AND estoque > 5
"""
dic4 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

titulo = "5. Ordem alfabética"
enunciado = "Liste o nome dos clientes em ordem alfabética."
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT nome
FROM Clientes
ORDER BY nome ASC
"""
dic5 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": True
}

titulo = "6. Primeiros pedidos"
enunciado = "Retorne os status dos 5 primeiros pedidos feitos na livraria."
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT status
FROM Pedidos
ORDER BY data_pedido
LIMIT 5
"""
dic6 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": True
}

dics = [dic1, dic2, dic3, dic4, dic5, dic6]