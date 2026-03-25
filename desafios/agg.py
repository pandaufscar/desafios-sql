titulo = "1. Número de produtos por categoria"
enunciado = "Calcular o número de produtos por categoria."
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT nome, COUNT(*) AS quantidade_produtos
FROM Produtos
GROUP BY id_categoria;
"""
dic1 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

titulo = "2. Clientes recorrentes."
enunciado = "Mostre os cliente que fizeram mais de 1 pedido, retorne o id do cliente e a quantidade de pedidos"
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT id_cliente, COUNT(*) AS quantidade_pedidos
FROM Pedidos
GROUP BY id_cliente
HAVING COUNT(*) > 1;
"""
dic2 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

dics = [dic1, dic2]