# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:38:13 2022

@author: leovi
"""

import pandas as pd
import mysql.connector
from mysql.connector import Error


# Carregando as tabelas
folder = r"C:\Users\leovi\CursoDS\estudo\PowerBI\cap10\dados\dados_limpos\\"

tb_data = pd.read_csv(folder + "tb_data.csv")
tb_loja = pd.read_csv(folder + "tb_loja.csv")
tb_produto = pd.read_csv(folder + "tb_produto.csv")
tb_vendas = pd.read_csv(folder + "tb_vendas.csv")
tb_vendedor = pd.read_csv(folder + "tb_vendedor.csv")


# Criando conexão com o mysql
connection = mysql.connector.connect(host='localhost',
                                     database='powerm',
                                     user='root',
                                     password='leozin100174')
cursor = connection.cursor()

# Inserindo os dados no db

# Tabela Data
for idx, row in tb_data.iterrows():
    query = "INSERT INTO powerm.tb_data \
             VALUES ('%s', '%s', '%s', '%s')" % (row["data_completa"], row["dia"], \
                 row["mes"], row["ano"])
    try:
         cursor.execute(query)
            
    except Error as e:
        print("Erro na linha - " + str(idx) + " :" + str(e) )
        
        
# Tabela loja
for idx, row in tb_loja.iterrows():
    query = "INSERT INTO powerm.tb_loja \
             VALUES ('%s', '%s', '%s')" % (row["Loja"], row["Cidade"], row["Estado"])
    try:
         cursor.execute(query)
            
    except Error as e:
        print("Erro na linha - " + str(idx) + " :" + str(e) )
        
        
# Tabela produto
for idx, row in tb_produto.iterrows():
    query = "INSERT INTO powerm.tb_produto \
             VALUES ('%s', '%s', '%s', '%s', '%s')" % (row["ID"], row["NOME"], \
                 row["CATEGORIA"], row["SEGMENTO"], row["MARCA"])
    try:
         cursor.execute(query)
            
    except Error as e:
        print("Erro na linha - " + str(idx) + " :" + str(e) )



# Tabela vendedor
for idx, row in tb_vendedor.iterrows():
    query = "INSERT INTO powerm.tb_vendedor \
             VALUES ('%s', '%s', '%s')" % (str(row["ID-Vendedor"]), row["nome"], row["sobrenome"])
    try:
         cursor.execute(query)
            
    except Error as e:
        print("Erro na linha - " + str(idx) + " :" + str(e) )
        
        
# Tabela Vendas
for idx, row in tb_vendas.iterrows():
    query = "INSERT INTO powerm.tb_vendas \
             VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (row["id_venda"], row["ID-Produto"], row["Loja"], \
                 str(row["ID-Vendedor"]), row["Data Venda"], row["ValorVenda"])
    try:
         cursor.execute(query)
            
    except Error as e:
        print("Erro na linha - " + str(idx) + " :" + str(e) )
        

connection.commit()
connection.close()