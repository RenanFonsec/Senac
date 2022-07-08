from classe_estoque import DBEstoque
from classe_fabricante import Fabricante

class Menu:
        def __init__(self):
            estoque = DBEstoque()

            while True:
                entrada = input('Informe a opção desejada'
                                '\n1 - Cadastrar Produto'
                                '\n2 - Cadastrar Fabricante'
                                '\n3 - Procurar produto'
                                '\n4 - Listar todos'
                                '\n5 - Alterar produto'
                                '\n6 - Excluir produto'
                                '\n0 - Sair')

                if entrada =='1':
                    cod = None
                    nome = input('Informe o nome do produto: ')
                    cod_fabricante = input('Informe o código do fabricante: ')
                    quantidade = input('Informe a quantidade de produto: ')

                    estoque.registrar_produto(cod, nome, cod_fabricante, quantidade)

                elif entrada=='2':
                    cod = None
                    fabricante = input('Informe o nome do fabricante: ')

                    estoque.registrar_fabricante(cod, fabricante)

                elif entrada =='3':
                    valor = input('Informe o codigo do produto: ')

                    estoque.achar_produto(valor)

                elif entrada =='4':
                    estoque.listar_todos_produtos()

                elif entrada =='5':
                    cod = int(input('Informe o código do produto: '))
                    valor = input('Informe o novo nome: ')
                    atributo = 'nome'
                    estoque.alterar_produto(atributo, valor, cod)

                elif entrada=='6':
                    valor = int(input('Informe o código do produto: '))
                    estoque.excluir_produto(valor)

                elif entrada =='0':
                    break

                else:
                    print('opção errada !')