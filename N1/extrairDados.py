import tabula
import csv
import pyodbc

#Conexão com BD
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BPODJN2\SQLEXPRESS;'
                      'Database=BD_AnaliseVendas;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

#Realiza a leitura de todas as páginas do PDF
#tabelaProdutos = tabula.read_pdf('produtos.pdf', pages='all');

#converte para CSV
#tabula.convert_into("produtos.pdf", "produtos.csv", output_format="csv", pages='all')

#abrir arquivos csv, realizar a leitura e inserção no banco de dados
with open('categorias.csv') as categorias:

  tabelaCategorias = csv.reader(categorias, delimiter=';')

  for l in tabelaCategorias:
    idCategoria = l[0]
    nomeCategoria = l[1]

    cursor.execute("""INSERT INTO [DBO].[categorias] ([IdCategoria],[NomeCategoria])  VALUES  ({0}, {1})""")
    print("Categoria ID %i inserida com sucesso!" %idCategoria)

conn.conexao.commit()

with open('produtos.csv') as produtos:

  tabelaProdutos = csv.reader(produtos, delimiter=',')

  for l in tabelaProdutos:
    nomeProduto = l[0]
    idCategoria = l[1]

    cursor.execute("""INSERT INTO [DBO].[produtos] ([nomeProduto],[idCategoria])  VALUES  ({0}, {1})""")
    print("Produto" + nomeProduto + "inserido com sucesso!")

conn.conexao.commit()

conn.close