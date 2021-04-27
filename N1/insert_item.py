from conexaoBD import Conexao
import random
import pyodbc
import time

tempo_inicial = time.time()

i = 1

while i <= 80000:
    
    try:
        conexao = Conexao().get_connection()
        cursor = conexao.cursor()

        id = i
        produto = random.randint(1, 50)

        resultado = cursor.execute("select id, descricao, categoria, preco from produtos where id = %d" %produto)
        produto_encontrado = resultado.fetchone()

        quantidade = random.randint(1, 20)
        preco = produto_encontrado[3] * quantidade


        count = cursor.execute('''
        INSERT INTO [dbo].[itens] ([id], [produto], [preco], [quantidade]) VALUES (?, ?, ?, ?)''', id, produto, preco, quantidade).rowcount
        conexao.commit()
        i + 1

    except (Exception, pyodbc.Error) as error:
        print("Oppss! Algum erro aconteceu :/", error)
        print("ID do cadastro em que o erro aconteceu:", i)
        break

tempo_final = time.time()
print("Tempo total de execução: ", tempo_final - tempo_inicial)
