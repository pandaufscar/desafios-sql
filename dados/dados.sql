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
(3, 'Pedro Santos', '2000-01-01', 'Belo Horizonte', '2022-01-05'),
(4, 'Ana Costa', '1992-07-30', 'Salvador', '2020-11-18'),
(5, 'Carlos Pereira', '1988-03-12', 'Curitiba', '2023-04-09'),
(6, 'Luiza Fernandes', '1995-09-22', 'Porto Alegre', '2021-02-14'),
(7, 'Rafael Almeida', '1982-12-05', 'Fortaleza', '2022-06-30'),
(8, 'Sofia Rodrigues', '1998-04-17', 'Brasília', '2020-08-21'),
(9, 'Thiago Martins', '1987-06-08', 'Recife', '2023-10-03'),
(10, 'Beatriz Lima', '1993-11-29', 'Manaus', '2021-05-16'),
(11, 'Gabriel Souza', '2002-02-10', 'Goiânia', '2022-09-27'),
(12, 'Isabela Gomes', '1984-08-03', 'Campinas', '2020-12-19'),
(13, 'Lucas Barbosa', '1991-01-25', 'Florianópolis', '2023-03-08'),
(14, 'Julia Mendes', '1996-07-11', 'Natal', '2021-10-22'),
(15, 'Matheus Carvalho', '1989-04-19', 'Santos', '2022-04-15');
