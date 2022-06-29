from classe_estoque import *

class Compra:
    def __init__(self):
        self.entrada = Estoque ()


def comprar(self):
    controle = int(input('Informe o codigo de produto: '))

    for i in range (len(self.entrada.listarProdutos)):
        if controle == self.entrada.listarProdutos[i].cod:
            self.entrada.listar_produtos[i].quantidade += int (input('Informe a quantidade comprada'))
    
    else:
        pass