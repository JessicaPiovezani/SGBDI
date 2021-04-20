import pyodbc

#Dados de conexão com servidor
server = "DESKTOP\SQLEXPRESS"
database = "BD_AnaliseVendas"
#username = "adminBD"
#password = "1234"

#conecta com usuário e senha
#conexao = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

#conexao via autenticação microsoft
conexao = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

cursor = conexao.cursor()