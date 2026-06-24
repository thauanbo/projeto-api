CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Inserindo dados iniciais para teste
INSERT INTO usuarios (nome, email) VALUES ('Albert Einstein', 'albert@email.com');
INSERT INTO usuarios (nome, email) VALUES ('Maria Souza', 'maria@email.com');