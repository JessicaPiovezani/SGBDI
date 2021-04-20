import tabula


#Realiza a leitura de todas as páginas do PDF
tabelaProdutos = tabula.read_pdf('produtos.pdf', pages='all');

#converte para CSV
#tabula.convert_into("produtos.pdf", "output.csv", output_format="csv", pages='all')
print(tabelaProdutos)