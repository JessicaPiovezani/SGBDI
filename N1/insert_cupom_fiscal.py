from conexaoBD import Conexao
import random
import pyodbc
import time

tempo_inicial = time.time()

i = 1

while i <= 100000:

    try:
        conexao = Conexao().get_connection()
        cursor = conexao.cursor()

        id = i
        itens = []
        valores = []

        numero_itens = random.randint(1, 20)
        num_itens = random.sample(range(1, 80000), numero_itens)

        for y in num_itens:
            resultado = cursor.execute("select id, produto, preco, quantidade from itens where id = %d" %y)
            item_encontrado = resultado.fetchone()
            itens.append(item_encontrado[0])
            valores.append(item_encontrado[2])

        preco_total = 0

        for x in valores:
            preco_total = preco_total + x

        count = cursor.execute('''
            INSERT INTO [dbo].[cupomFiscal] ([id], [total]) VALUES (?, ?)''', id, preco_total).rowcount
        conexao.commit()

        for j in itens:
            count = cursor.execute('''
            INSERT INTO [dbo].[cupom_item] ([id_cupom], [id_item]) VALUES (?, ?)''', id, j).rowcount
            conexao.commit()
        i+1

    except (Exception, pyodbc.Error) as error:
        print("Oppss! Algum erro aconteceu :/", error)
        print("ID do cadastro em que o erro aconteceu:", i)
        break

tempo_final = time.time()
print("Tempo total de execução: ", tempo_final - tempo_inicial)
