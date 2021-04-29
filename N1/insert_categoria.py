from conexaoBD import Conexao
import pyodbc
import time

conexao = Conexao().get_connection()
cursor = conexao.cursor()

tempo_inicial = time.time()
for i in range(50):
    
    try:
        nomeCategoria = "categoria " + str(i)
        count = cursor.execute("INSERT INTO categorias (nomeCategoria) VALUES (?)", nomeCategoria).rowcount
        
    except (Exception, pyodbc.Error) as error:
        print("Oppss! Algum erro aconteceu :/", error)
        print("ID do cadastro em que o erro aconteceu:", i)
        break
    
    finally:
        conexao.commit()
        print("Cadastro inserido com sucesso!", i)

tempo_final = time.time()
print("Tempo total de execução: ", tempo_final - tempo_inicial)
