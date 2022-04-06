CREATE DATABASE IF NOT EXISTS powerm;

CREATE TABLE IF NOT EXISTS powerm.tb_loja (
	id_loja VARCHAR(20) PRIMARY KEY UNIQUE,
    cidade VARCHAR(20),
    estado VARCHAR(20));
    
CREATE TABLE IF NOT EXISTS powerm.tb_data (
	data_completa DATETIME PRIMARY KEY UNIQUE,
    dia VARCHAR(10),
    mes VARCHAR(10),
    ano VARCHAR(10));
    
CREATE TABLE IF NOT EXISTS powerm.tb_produto (
	id_produto VARCHAR(20) PRIMARY KEY UNIQUE,
    nome_produto VARCHAR(50),
    categoria VARCHAR(20),
    segmento VARCHAR(20),
    marca VARCHAR(20));
    
CREATE TABLE IF NOT EXISTS powerm.tb_vendedor (
	id_vendedor VARCHAR(20) PRIMARY KEY UNIQUE,
    nome VARCHAR(20),
    sobrenome VARCHAR(20));
    
CREATE TABLE IF NOT EXISTS powerm.tb_vendas (
	id_venda INT AUTO_INCREMENT PRIMARY KEY,
	id_produto VARCHAR(20),
    id_loja VARCHAR(20),
    id_vendedor VARCHAR(20),
    data_completa DATETIME,
    valor_venda FLOAT(20),
    FOREIGN KEY (id_produto) REFERENCES powerm.tb_produto(id_produto),
    FOREIGN KEY (id_loja) REFERENCES powerm.tb_loja(id_loja),
    FOREIGN KEY (id_vendedor) REFERENCES powerm.tb_vendedor(id_vendedor),
    FOREIGN KEY (data_completa) REFERENCES powerm.tb_data(data_completa)
    );
