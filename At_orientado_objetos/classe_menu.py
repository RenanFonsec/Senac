from classe_agenda import *

class Menu:
    def __init__(self):
        agenda_renan = Agenda()

        while True:
            entrada = input('Informe a opção desejada'
                            '\n1 - Novo contato'
                            '\n2 - Listar Contatos'
                            '\n3 - Alterar telefone'
                            '\n0 - Sair\n')

            
            if entrada =='1':
                agenda_renan.salvar_contatos()

            elif entrada =='2':
                agenda_renan.listar_todos_contatos()

            elif entrada == '3':
                agenda_renan.alterar_telefone()

            elif entrada =='0': 
                break

            else:
                print('opção errada!')
            