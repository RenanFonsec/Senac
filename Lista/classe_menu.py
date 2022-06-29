from classe_estoque import *

class Menu:
        def __init__(self):
            listar_produtos = Estoque()

            while True:
                entrada = input('Informe a opção desejada'
                                '\n1 - Cadastrar Produto'
                                '\n2 - Listar todos'
                                '\n3 - Procurar produto'
                                '\n4 - Alterar produto'
                                '\n5 - Sair')

                if entrada =='1':
                    listar_produtos.registrar_produto()

                elif entrada =='2':
                    listar_produtos.listar_todos_produtos()

                elif entrada =='3':
                    listar_produtos.achar_produto()

                elif entrada =='4':
                    listar_produtos.alterar_nome()

                elif entrada =='5':
                    break

                else:
                    print('opção errada !')