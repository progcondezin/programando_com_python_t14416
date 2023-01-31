-- Active: 1675130595220@@127.0.0.1@3306
# Criar o banco de dados
CREATE DATABASE tb_kasolution
    DEFAULT CHARACTER SET = 'utf8mb4';

# criar a tabela de tb_enderecos
CREATE TABLE tb_enderecos(  
    cep int NOT NULL PRIMARY KEY COMMENT 'Primary Key',
    logradouro VARCHAR(255),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    uf VARCHAR(2),
    ibge VARCHAR(255)
) COMMENT 'Tabela para armazenar os enderecos';


#Criar a tabela tb_senhas
CREATE TABLE tb_senhas(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    senha VARCHAR(255)
) COMMENT 'Tabela para armazenar as senhas';


# Criar a tabela de usuarios
CREATE TABLE tb_usuarios(  
    id int AUTO_INCREMENT COMMENT 'Primary Key',
    nome VARCHAR(255),
    usuario VARCHAR(255),
    enderecoId INT,
    senhaId INT,
    PRIMARY KEY (id),
    FOREIGN KEY (enderecoId) REFERENCES tb_enderecos(cep),
    FOREIGN KEY (senhaId) REFERENCES tb_senhas(id)
) COMMENT '';


