from conexaoBD import Conexao
import pyodbc
import random
import time

tempo_inicial = time.time()

i = 1

while i <= 50000:
    
    try:
        conexao = Conexao().get_connection()
        cursor = conexao.cursor()

        id = i
        descricao = "produto " + str(i)
        categoria = random.randint(1, 50)
        numero = random.uniform(1, 100)
        preco = round(numero, 2)

        count = cursor.execute('''INSERT INTO [dbo].[produtos] ([id] ,[descricao] ,[categoria] ,[preco]) VALUES (?, ?, ?, ?)''', id, descricao, categoria, preco).rowcount
        conexao.commit()
        i + 1

    except (Exception, pyodbc.Error) as error:
        print("Oppss! Algum erro aconteceu :/", error)
        print("ID do cadastro em que o erro aconteceu:", i)
        break

tempo_final = time.time()
print("Tempo total de execução: ", tempo_final - tempo_inicial)
