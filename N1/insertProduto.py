from conexaoBD import Conexao
import pyodbc
import random
import time

conexao = Conexao().get_connection()
cursor = conexao.cursor()

tempo_inicial = time.time()

for i in range(50000):   

    try:
        #Definição das informações que compõe o produto
        nomeProduto = ("Produto %d" %i)
        
        numero = random.uniform(1, 100)
        valorUnitario = round(numero, 2)

        #Selecionando categorias já existentes no banco de dados de forma randomica
        cursor.execute("SELECT TOP(1) idCategoria FROM categorias order by NEWID()")
        categoria = cursor.fetchall()[0]

        #Insere os produtos no banco de dados
        count = cursor.execute("INSERT INTO produtos (nomeProduto, idCategoria, valorUnitario) VALUES ( ?, ?, ?)", nomeProduto, categoria.idCategoria, valorUnitario)

    except (Exception, pyodbc.Error) as error:
        print("Oppss! Algum erro aconteceu :/", error)
        print("ID do cadastro em que o erro aconteceu:", i)
        break

    finally:
        conexao.commit()
        print("Cadastro inserido com sucesso!", i)

tempo_final = time.time()
print("Tempo total de execução: ", tempo_final - tempo_inicial)
