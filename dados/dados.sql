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
