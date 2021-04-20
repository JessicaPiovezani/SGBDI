import tabula
import csv
from conexaoBD import conexaoSQL
conn = conexaoSQL()
cursor = conn.cursor()

#Realiza a leitura de todas as páginas do PDF
#tabelaProdutos = tabula.read_pdf('produtos.pdf', pages='all');

#converte para CSV
#tabula.convert_into("produtos.pdf", "produtos.csv", output_format="csv", pages='all')

#abrir arquivos csv e realizar a leitura
with open('categorias.csv') as categorias:

  tabelaCategorias = csv.reader(categorias, delimiter=';')

  for l in tabelaCategorias:
    idCategoria = l[0]
    nomeCategoria = l[1]

    cursor.execute("""INSERT INTO [DBO].[categorias] ([IdCategoria],[NomeCategoria])  VALUES  ({0}, {1})""")
    print(idCategoria, nomeCategoria)

conn.commit()
"""with open('produtos.csv') as produtos:

  tabelaProdutos = csv.reader(produtos, delimiter=',')

  for l in tabelaProdutos:
    nomeProduto = l[0]
    idCategoria = l[1]

    print(nomeProduto, idCategoria)"""