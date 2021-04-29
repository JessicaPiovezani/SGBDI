from conexaoBD import Conexao
from random import choice
import random
import pyodbc
import time
import string

tempo_inicial = time.time()

i = 1
conexao = Conexao().get_connection()
cursor = conexao.cursor()
while i <= 100000:

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
        id_cupom = cursor.lastrowid
        
        #Cria uma quantidade randomica de itens para esse cupom
        total_itens = random.randint(1, 20);
        
        #Inicia o loop para registrar os itens do cupom
        for x in total_itens:
            
            #Seleciona um produto de forma aleatoria no banco
            cursor.execute("SELECT idProduto, valorUnitario FROM produtos order by rand() limit 1")
            produto = cursor.fetchone()
            
            #Define uma quantidade de produtos para o item do cupom
            quant_produto = random.randint(1, 3)
            
            #insere o item do cupom
            cursor.execute("INSERT INTO itensCupom (idProduto, quantidadeProduto, idCupom, valorProduto) VALUES (?,?,?,?)", produto["idProduto"],quant_produto,id_cupom,produto["valorUnitario"])    

    except (Exception, pyodbc.Error) as error:
        print("Oppss! Algum erro aconteceu :/", error)
        print("ID do cadastro em que o erro aconteceu:", i)
        break

conexao.commit()
tempo_final = time.time()
print("Tempo total de execução: ", tempo_final - tempo_inicial)
