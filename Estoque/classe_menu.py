from classe_estoque import DBEstoque

class Menu:
        def __init__(self):
            estoque = DBEstoque()

            while True:
                entrada = input('Informe a opção desejada'
                                '\n1 - Cadastrar Produto'
                                '\n2 - Procurar produto'
                                '\n3 - Listar todos'
                                '\n4 - Alterar produto'
                                '\n5 - Excluir produto'
                                '\n0 - Sair')

                if entrada =='1':
                    cod = None
                    nome = input('Informe o nome do produto: ')
                    fabricante = input('Informe o nome do fabricante: ')
                    quantidade = input('Informe a quantidade de produto: ')

                    estoque.registrar_produto(cod, nome, fabricante, quantidade)

                elif entrada =='2':
                    valor = input('Informe o codigo do produto: ')

                    estoque.achar_produto(valor)

                elif entrada =='3':
                    estoque.listar_todos_produtos()

                elif entrada =='4':
                    cod = int(input('Informe o código do produto: '))
                    valor = input('Informe o novo nome: ')
                    atributo = 'nome'
                    estoque.alterar_produto(atributo, valor, cod)

                elif entrada=='5':
                    valor = int(input('Informe o código do produto: '))
                    estoque.excluir_produto(valor)

                elif entrada =='0':
                    break

                else:
                    print('opção errada !')