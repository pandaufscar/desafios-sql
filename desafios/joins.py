titulo = "1. Produtos e quantidades nos pedidos"
enunciado = "Liste o nome dos produtos e suas respectivas quantidades nos pedidos."
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT Produtos.nome, ItensPedidos.quantidade
FROM ItensPedidos
INNER JOIN Produtos
ON ItensPedidos.id_produto = Produtos.id_produto;
"""
dic1 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

titulo = "2. Produtos da categoria Escolar"
enunciado = "Liste o nome dos produtos que pertencem à categoria Escolar."
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT p.nome
FROM produtos p
JOIN categorias c ON p.id_categoria = c.id_categoria
WHERE c.nome = 'Escolar'
"""
dic2 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

titulo = "3. Pedidos e seus clientes"
enunciado = "Liste os clientes e o ID dos seus pedidos, liste até os clientes sem pedidos"
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT Pedidos.id_pedido, Clientes.nome
FROM Pedidos
INNER JOIN Clientes
ON Pedidos.id_cliente = Clientes.id_cliente;
"""
dic3 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

titulo = "4. Todas as categorias e seus produtos"
enunciado = "Liste o nome de todas as categorias e os nomes dos produtos associados a elas, incluindo categorias sem produtos."
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT Categorias.nome, Produtos.nome
FROM Categorias
LEFT JOIN Produtos
ON Categorias.id_categoria = Produtos.id_categoria;
"""
dic4 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

titulo = "5. Produtos, quantidades e pedidos"
enunciado = "Liste o nome dos produtos, a quantidade pedida e o ID dos pedidos correspondentes."
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT Produtos.nome, ItensPedidos.quantidade, Pedidos.id_pedido
FROM ItensPedidos
INNER JOIN Produtos
ON ItensPedidos.id_produto = Produtos.id_produto
INNER JOIN Pedidos
ON ItensPedidos.id_pedido = Pedidos.id_pedido;
"""
dic5 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

titulo = "6. Produtos cadastrados vs produtos vendidos"
enunciado = "Liste todos os produtos cadastrados e os produtos que aparecem em pedidos, incluindo aqueles que nunca foram vendidos e aqueles que aparecem em pedidos mas não estão cadastrados."
imagem_esquema = "schema.jpg"
resposta_sql = """
SELECT 
    Produtos.nome AS produto_cadastrado,
    ItensPedidos.id_produto AS produto_vendido
FROM Produtos
FULL OUTER JOIN ItensPedidos
ON Produtos.id_produto = ItensPedidos.id_produto;
"""
dic6 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

dics = [dic1, dic2, dic3, dic4, dic5, dic6]