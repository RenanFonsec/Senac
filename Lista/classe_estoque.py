from classe_produto import *

class Estoque:
    def __init__(self):
        self.listarProdutos = []


    def registrar_produto(self):
        entrada_cod = str(len(self.listarProdutos)+1)
        entrada_nome = input('Informe o nome: ')
        entrada_fabricante = input('Informe o fabricante: ')
        entrada_quantidade = input('Informe a quantidade: ')
        self.listarProdutos.append(Produtos(entrada_cod,
                                            entrada_nome,
                                            entrada_fabricante,
                                            entrada_quantidade, 
                                            ))
        print('Produto registrado com sucesso !')


    def achar_produto(self):
        cont = 0
        entrada = input('Informe o codigo do produto: ')
        for i in range(len(self.listarProdutos)):
            if entrada == self.listarProdutos[i].cod:
                print(' - Cod', self.listarProdutos[i].cod,
                      ' - Nome', self.listarProdutos[i].nome,
                      ' - Quantidade', self.listarProdutos[i].quantidade)

            else:
                cont += 1
                for i in range(len(self.listarProdutos)):
                    if cont == len(self.listarProdutos):
                        print(' - Cod', self.listarProdutos[i].cod,
                            ' - Nome', self.listarProdutos[i].nome,
                            ' - Fabricante', self.listarProdutos[i].fabricante,
                            ' - Quantidade', self.listarProdutos[i].quantidade)
            

    def listar_todos_produtos (self):
        for i in range(len(self.listarProdutos)):
            print(' - Cod:', self.listarProdutos[i].cod,
                  ' - Nome:', self.listarProdutos[i].nome,
                  ' - Fabricante:', self.listarProdutos[i].fabricante,
                  ' - Quantidade: ', self.listarProdutos[i].quantidade)


    def alterar_nome (self):
        cont = 0
        entrada = input('Informe o codigo do produto:')
        for i in range(len(self.listarProdutos)):
            if entrada == self.listarProdutos[i].cod:
                self.listarProdutos[i].nome = input('Novo nome: ')

            else:
                cont += 1
                if cont == len(self.listarProdutos):
                    print('Codigo não cadastrado')
