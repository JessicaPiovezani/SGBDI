from insertCategoria import Categoria;
from insertProduto import Produto;
from insertCupom import Cupom;
from consultas import Consultas;

opcao = -1
while opcao != 0:

    opcao = int(input("Olá! Escolha uma das opções numerais a seguir:\n1- Realizar inserções\n2- Realizar as consultas\nPara parar sair do programa digite 0.\nR: "))

    if opcao == 1:

        try:

            categorias = -1
            while categorias != 1:
                categorias = int (input("\n\nPara começar, deveremos inserir os dados na tabela de categorias. Se você deseja prosseguir, digite 1.\nPara parar sair do programa digite 0.\nR: "))
                if categorias == 0:
                    break
            Categoria().insert_Categoria()
            
            produtos = -1
            while produtos != 1:
                produtos = int (input("\n\nAgora iremos realizar a inserção dos produtos. Se você deseja prosseguir, digite 1.\nPara parar sair do programa digite 0.\nR: "))
                if produtos == 0:
                    break
            Produto().insert_Produtos()

            cupons = -1
            while cupons != 1:
                cupons = int (input("\n\nPor útimo (mas não menos importante), iremos realizar a inserção dos cupons ficais. Se você deseja prosseguir, digite 1.\nPara parar sair do programa digite 0.\nR: "))
                if cupons == 0:
                    break
            Cupom().insert_cupomFiscal()
            break
        
        except ValueError:
            print("Opção inválida, tente novamente.\n")
    
    if opcao == 2:

        try:
            
            tipoConsulta = -1
            
            while tipoConsulta != 0:
                tipoConsulta = int (input("\nEscolha uma das opções numerais a seguir:\n1- Consultar total de valor vendido por categoria de produto (50 registros)\n2- Consultar os 10 produtos mais vendidos.\nPara parar sair do programa digite 0.\nR: "))

                if tipoConsulta == 1:
                    Consultas().get_valorVendidoCategorias()

                if tipoConsulta == 2:
                    Consultas().get_produtosMaisVendidos()

        except ValueError:
            print("Opção inválida, tente novamente.\n")