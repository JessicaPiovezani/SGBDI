from conexaoBD import Conexao
import time

class Consultas():
    def get_produtosMaisVendidos(self):
        conexao = Conexao().get_connection()
        cursor = conexao.cursor()

        tempo_inicial = time.time()
        
        cursor.execute('''SELECT TOP(10) p.nomeProduto, 
                COUNT(i.idCupom) as cupons, 
                SUM(i.quantidadeProduto) as quantidadeVendas FROM itensCupom as i, 
                produtos as p where i.idProduto = p.idProduto 
                GROUP BY p.nomeProduto 
                ORDER BY quantidadeVendas DESC;''')
        
        tempo_final = time.time()
        
        return print("Tempo total de execução: ", tempo_final - tempo_inicial)
    
    def get_valorVendidoCategorias(self):
        conexao = Conexao().get_connection()
        cursor = conexao.cursor()

        tempo_inicial = time.time()
        
        cursor.execute('''SELECT TOP(50) c.nomeCategoria,  
                SUM(i.quantidadeProduto * i.valorProduto) as totalVendas FROM itensCupom as i, categorias as c, produtos as p 
                where i.idProduto = p.idProduto 
                AND p.idCategoria = c.IdCategoria
                GROUP BY c.nomeCategoria ORDER BY totalVendas DESC;''')
        
        tempo_final = time.time()
        
        return print("Tempo total de execução: ", tempo_final - tempo_inicial)