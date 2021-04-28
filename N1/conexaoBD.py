import pyodbc

class Conexao():
    def get_connection(self):
        server = 'DESKTOP-BPODJN2\Jessica'
        database = 'BD_AnaliseVendas'
        username = 'dbo'
        password = '1234'
        conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        #conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + 'Trusted_Connection=yes;')
        return conexao