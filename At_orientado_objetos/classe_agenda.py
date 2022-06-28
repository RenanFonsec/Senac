from classe_contato import *

class Agenda:
    def __init__(self):
        self.listaContatos = [] 


    def salvar_contatos(self):
        entrada_cod = str(len(self.listaContatos)+1)
        entrada_nome = input('Informe o nome: ')
        entrada_telefone = input('Informe o telefone: ')
        self.listaContatos.append(Contato(entrada_cod, entrada_nome, entrada_telefone))
        print('Contato salvo com sucesso !')

    def listar_todos_contatos(self):
        for i in range(len(self.listaContatos)):
            print('- Cod:', self.listaContatos[i].cod,
                  '- Nome:', self.listaContatos[i].nome,
                  '- Telefone:', self.listaContatos[i].telefone)

    def alterar_telefone(self):
        cont = 0
        entrada = input('Informe o codigo do contato:')
        for i in range(len(self.listaContatos)):
            if entrada == self.listaContatos[i].cod:
                self.listaContatos[i].telefone = input('Novo telefone: ')

            else:
                cont += 1
                if cont == len(self.listaContatos):
                    print('Codigo não cadastrado')