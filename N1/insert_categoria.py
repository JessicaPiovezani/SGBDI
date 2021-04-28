from conexaoBD import Conexao
import pyodbc
import time

tempo_inicial = time.time()

i = 0

while i <= 50:
    
    try:
        conexao = Conexao().get_connection()
        cursor = conexao.cursor()

        id = i
        palavra = "categoria " + str(i)

        count = cursor.execute("""INSERT INTO categorias (id, categoria) VALUES (?,?)""", id, palavra).rowcount
        conexao.commit()
        print("Cadastro %d inserido com sucesso! ID:" %i)
        i+1

    except (Exception, pyodbc.Error) as error:
        print("Oppss! Algum erro aconteceu :/", error)
        print("ID do cadastro em que o erro aconteceu:", i)
        break

tempo_final = time.time()
print("Tempo total de execução: ", tempo_final - tempo_inicial)
