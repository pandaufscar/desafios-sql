titulo = "Produtos da categoria Escolar"
enunciado = "Liste o nome dos produtos que pertencem à categoria Escolar."
imagem_esquema = "schema.png"
resposta_sql = """
SELECT p.nome
FROM produtos p
JOIN categorias c ON p.id_categoria = c.id_categoria
WHERE c.nome = 'Escolar'
"""
dic1 = {
    "titulo": titulo,
    "enunciado": enunciado,
    "imagem_esquema": imagem_esquema,
    "resposta_sql": resposta_sql,
    "ordem": False
}

dics = [dic1]