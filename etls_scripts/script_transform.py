# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

# Carregando as tabelas
folder = r"C:\Users\leovi\CursoDS\estudo\PowerBI\cap10\dados\\"

tb_data = pd.read_csv(folder + "data.csv")
tb_loja = pd.read_csv(folder + "loja.csv")
tb_produto = pd.read_csv(folder + "produto.csv")
tb_vendas = pd.read_csv(folder + "vendas.csv")
tb_vendedor = pd.read_csv(folder + "vendedor.csv")


# Transformando tabela data
tb_data["dia"] = [i[0] for i in tb_data["Data"].str.split("/")]
tb_data["mes"] = [i[1] for i in tb_data["Data"].str.split("/")]
tb_data["ano"] = [i[2] for i in tb_data["Data"].str.split("/")]

tb_data.rename({"Data": "data_completa"},axis=1, inplace=True)
tb_data["data_completa"] = pd.to_datetime(tb_data["data_completa"])
tb_data = tb_data.sort_values(by="data_completa")
tb_data.reset_index(drop=True, inplace=True)


# Transformando tabela vendas
tb_vendas["Data Venda"] = pd.to_datetime(tb_vendas["Data Venda"])
tb_vendas.sort_values(by="Data Venda", inplace=True)
tb_vendas.reset_index(drop=True, inplace=True)
tb_vendas["id_venda"] = [str(i) for i in range(1, tb_vendas.shape[0] + 1)]


# Transformando tabela vendedor
tb_vendedor["nome"] = [i[0] for i in tb_vendedor["Vendedor"].str.split(" ")]
tb_vendedor["sobrenome"] = [i[1] for i in tb_vendedor["Vendedor"].str.split(" ")]
tb_vendedor.iloc[8, 0] = "1008"
tb_vendedor.drop("Vendedor", axis=1, inplace=True)


# Salvando os arquivos limpos e transformados
folder_to_save = r"C:\Users\leovi\CursoDS\estudo\PowerBI\cap10\dados\dados_limpos\\"

tb_data.to_csv(path_or_buf = folder_to_save + "tb_data.csv", encoding="utf-8", index=False)
tb_loja.to_csv(path_or_buf = folder_to_save + "tb_loja.csv", encoding="utf-8", index=False)
tb_produto.to_csv(path_or_buf = folder_to_save + "tb_produto.csv", encoding="utf-8", index=False)
tb_vendas.to_csv(path_or_buf = folder_to_save + "tb_vendas.csv", encoding="utf-8", index=False)
tb_vendedor.to_csv(path_or_buf = folder_to_save + "tb_vendedor.csv", encoding="utf-8", index=False)