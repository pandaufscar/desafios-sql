CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    data_cadastro DATE NOT NULL
);

INSERT INTO clientes (id_cliente, nome, data_nascimento, cidade, data_cadastro) VALUES
(1, 'João Silva', '1990-05-15', 'São Paulo', '2020-03-12'),
(2, 'Maria Oliveira', '1985-10-20', 'Rio de Janeiro', '2021-07-25'),
(3, 'Pedro Santos', '2005-01-01', 'Belo Horizonte', '2022-01-05'),
(4, 'Ana Costa', '1992-07-30', 'Salvador', '2020-11-18'),
(5, 'Carlos Pereira', '1988-03-12', 'Curitiba', '2023-04-09'),
(6, 'Luiza Fernandes', '1995-09-22', 'Porto Alegre', '2021-02-14'),
(7, 'Rafael Almeida', '1982-12-05', 'Fortaleza', '2022-06-30'),
(8, 'Sofia Rodrigues', '1998-04-17', 'Brasília', '2020-08-21'),
(9, 'Thiago Martins', '2007-06-08', 'Recife', '2023-10-03'),
(10, 'Beatriz Lima', '1993-11-29', 'Manaus', '2021-05-16'),
(11, 'Gabriel Souza', '2002-02-10', 'Goiânia', '2022-09-27'),
(12, 'Isabela Gomes', '1984-08-03', 'Campinas', '2020-12-19'),
(13, 'Lucas Barbosa', '2001-01-25', 'Florianópolis', '2023-03-08'),
(14, 'Julia Mendes', '1996-07-11', 'Natal', '2021-10-22'),
(15, 'Matheus Carvalho', '1989-04-19', 'Santos', '2022-04-15');

CREATE TABLE categorias (
    id_categoria INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

INSERT INTO categorias (id_categoria, nome) VALUES
(1, 'Escolar'),
(2, 'Escritório'),
(3, 'Organização');


CREATE TABLE produtos (
    id_produto INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_categoria INT NOT NULL,
    preco DECIMAL(10,2) NOT NULL CHECK (preco >= 0),
    estoque INT NOT NULL CHECK (estoque >= 0),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

INSERT INTO produtos 
(id_produto, nome, id_categoria, preco, estoque)
VALUES
(1, 'Caderno', 1, 15.00, 80),
(2, 'Lápis', 1, 1.50, 400),
(3, 'Caneta Azul', 1, 2.50, 300),
(4, 'Borracha', 1, 1.50, 200),
(5, 'Régua', 1, 4.00, 150),
(6, 'Apontador', 1, 2.00, 180),
(7, 'Mochila', 1, 120.00, 40),

(8, 'Grampeador', 2, 26.00, 40),
(9, 'Grampos', 2, 6.50, 90),
(10, 'Post-it', 2, 8.00, 120),
(11, 'Caneta Preta', 2, 2.50, 250),
(12, 'Papel A4', 2, 30.00, 70),
(13, 'Calculadora', 2, 40.00, 35),

(14, 'Pasta', 3, 4.00, 140),
(15, 'Pasta com Elástico', 3, 6.00, 110),
(16, 'Caixa Organizadora', 3, 20.00, 45),
(17, 'Arquivo', 3, 13.00, 60),
(18, 'Envelope', 3, 1.00, 300),
(19, 'Fichário', 3, 50.00, 30),
(20, 'Etiqueta', 3, 3.00, 160);

CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_pedido DATE NOT NULL,
    status VARCHAR(20) NOT NULL,

    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

INSERT INTO pedidos (id_pedido, id_cliente, data_pedido, status) VALUES
(1, 1, '2024-01-10', 'Finalizado'),
(2, 2, '2024-01-12', 'Finalizado'),
(3, 3, '2024-01-15', 'Em processo'),
(4, 4, '2024-01-18', 'Cancelado'),
(5, 5, '2024-01-20', 'Finalizado'),
(6, 1, '2024-02-01', 'Em processo'),
(7, 6, '2024-02-03', 'Finalizado'),
(8, 7, '2024-02-10', 'Em processo'),
(9, 8, '2024-02-12', 'Finalizado'),
(10, 9, '2024-02-15', 'Em processo'),
(11, 10, '2024-02-18', 'Finalizado'),
(12, 11, '2024-02-20', 'Finalizado'),
(13, 12, '2024-02-22', 'Cancelado'),
(14, 13, '2024-02-25', 'Finalizado'),
(15, 14, '2024-02-27', 'Em processo'),
(16, 15, '2024-03-01', 'Finalizado'),
(17, 3, '2024-03-03', 'Finalizado'),
(18, 5, '2024-03-05', 'Em processo'),
(19, 8, '2024-03-08', 'Finalizado'),
(20, 2, '2024-03-10', 'Finalizado');

CREATE TABLE itens_pedidos (
    id_pedido INT,
    id_produto INT,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (id_pedido, id_produto),

    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

INSERT INTO itens_pedidos (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 2, 15.00),
(1, 2, 5, 1.50),
(1, 3, 10, 2.50),
(1, 4, 8, 1.50),
(1, 5, 4, 4.00),

(2, 3, 3, 2.50),
(2, 10, 2, 8.00),

(3, 7, 1, 120.00),

(4, 12, 1, 30.00),

(5, 14, 4, 4.00),
(5, 18, 10, 1.00),
(5, 3, 6, 2.50),
(5, 11, 10, 2.50),
(5, 15, 5, 6.00),

(6, 5, 2, 4.00),
(6, 6, 1, 2.00),

(7, 8, 1, 26.00),
(7, 9, 2, 6.50),

(8, 16, 1, 20.00),
(8, 19, 1, 50.00),
(8, 20, 12, 3.00),

(9, 1, 5, 15.00),
(9, 2, 20, 1.50),

(10, 11, 12, 2.50),
(10, 5, 6, 4.00),

(11, 3, 10, 2.50),
(11, 18, 25, 1.00),

(12, 7, 1, 120.00),
(12, 10, 15, 8.00),

(13, 16, 2, 20.00),
(13, 14, 8, 4.00),

(14, 2, 25, 1.50),
(14, 4, 10, 1.50),

(15, 17, 3, 13.00),
(15, 18, 30, 1.00),

(16, 8, 2, 26.00),
(16, 9, 6, 6.50),

(17, 1, 4, 15.00),
(17, 3, 12, 2.50),

(18, 12, 3, 30.00),
(18, 15, 8, 6.00),

(19, 5, 10, 4.00),
(19, 6, 12, 2.00),

(20, 11, 20, 2.50),
(20, 20, 15, 3.00);
