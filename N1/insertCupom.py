from conexaoBD import Conexao
from random import choice
import random
import pyodbc
import time
import string

conexao = Conexao().get_connection()
cursor = conexao.cursor()

tempo_inicial = time.time()

for i in range(10):
    try:

        #Randômico para gerar os códigos do cupom
        tamanho = 12
        valores = string.ascii_letters + string.digits + string.punctuation
        codigoCupom = ''
        for j in range(tamanho):
            codigoCupom += choice(valores)
        
        #Insere o cupom no banco de dados
        cursor.execute("INSERT INTO cupomFiscal (codigoCupom) VALUES (?)", codigoCupom)
        
        #Recebe o id do cupom recem inserido
        idCupom = cursor.execute('SELECT @@IDENTITY AS id;').fetchone()[0]
        
        #Cria uma quantidade randomica de itens para esse cupom
        quantidadeItens = random.randint(1, 20)
        
        #Inicia o loop para registrar os itens do cupom
        for x in range(quantidadeItens):
            
            #Seleciona um produto de forma aleatoria no banco
            cursor.execute("SELECT TOP(1) idProduto, valorUnitario FROM produtos order by NEWID()")
            produto = cursor.fetchall()[0]
            
            #Define uma quantidade de produtos para o item do cupom
            quantidadeProduto = random.randint(1, 3)
            
            #insere o item do cupom
            cursor.execute("INSERT INTO itensCupom (idProduto, quantidadeProduto, idCupom, valorProduto) VALUES (?,?,?,?)", produto.idProduto, quantidadeProduto, idCupom, produto.valorUnitario)    

    except (Exception, pyodbc.Error) as error:
        print("Oppss! Algum erro aconteceu :/", error)
        print("ID do cadastro em que o erro aconteceu:", i)
        break

    finally:
        conexao.commit()
        print("Cadastro inserido com sucesso!", i)

tempo_final = time.time()
print("Tempo total de execução: ", tempo_final - tempo_inicial)
