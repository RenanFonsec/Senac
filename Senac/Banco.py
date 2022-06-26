from itertools import tee
from tkinter import *

import ajuda
from Classe_cadastro import *

# ========================================= vetores ===============================================================

nomes_registrados = []

# ========================================= back-end ===============================================================

janela = Tk()
janela.title('Lockbank')
janela.geometry('465x760')
janela.resizable(width=False, height=False)

janela.bind('<Button-1>', ajuda.inicio_place)
janela.bind('<ButtonRelease-1>', lambda arg: ajuda.fim_place(arg, janela))
janela.bind('<Button-2>', lambda arg: ajuda.para_geometry(janela))

# =========================================== Funções =============================================


def registrar():
    nomes_registrados.append(Cadastro(boxNome.get(),
                                      int(boxSenha.get()),
                                      int(boxCpf.get()),
                                      int(boxDatanasc.get()),
                                      int(boxTel.get())))

    for i in range(len(nomes_registrados)):
        print(nomes_registrados[i].nome,
              nomes_registrados[i].senha,
              nomes_registrados[i].cpf,
              nomes_registrados[i].datanasc,
              nomes_registrados[i].tel)

    boxNome.delete(0, 'end')
    boxSenha.delete(0, 'end')
    boxCpf.delete(0, 'end')
    boxDatanasc.delete(0, 'end')
    boxTel.delete(0, 'end')


def login():
    global controle_login
    for i in range(len(nomes_registrados)):
        if nomes_registrados[i].nome == boxEntry.get() and nomes_registrados[i].senha == int(boxEntry2.get()):
            nome_conta['text'] = 'Olá,' + nomes_registrados[i].nome
            exibir_saldo['text'] = 'R$' + str(nomes_registrados[i].saldo)
            controle_login = nomes_registrados[i]
            tela_saldo.pack()
            tela_login.pack_forget()

    boxEntry.delete(0, 'end')
    boxEntry2.delete(0, 'end')


def executa_deposito():
    controle_login.deposito(float(entryValor_deposito.get()))
    exibir_saldo['text'] = 'R$' + str(controle_login.saldo)

    entryValor_deposito.delete(0, 'end')


def executa_saque():
    controle_login.saque(float(entryValor_saque.get()))
    exibir_saldo['text'] = 'R$' + str(controle_login.saldo)

    entryValor_saque.delete(0, 'end')


def executa_transferencia():
    for i in range(len(nomes_registrados)):
        if str(nomes_registrados[i].cpf) == str(entryescolher_CPF.get()):
            valor = float(entryvalor_transferencia.get())
            controle_login.transferencia(valor, nomes_registrados[i])
            exibir_saldo['text'] = 'R$' + str(controle_login.saldo)


def executa_historico():
    for i in range(len(controle_login.historico)):
        print(controle_login.historico[i])


def esconder_saldo():
    if(exibir_saldo['text'] == '---'):
        exibir_saldo['text'] = 'R$' + str(controle_login.saldo)

    else:
        exibir_saldo['text'] = '---'


# ================================== exportações de imagens ==================================
imagem = PhotoImage(file='imagens/Cadastrar.png')

ImagemLogin = PhotoImage(file='imagens/Login.png')

ImagemCadastrar = PhotoImage(file='imagens/Funcionario.png')

ImagemSaldo = PhotoImage(file='imagens/Saldo.png')

Imagemsaque = PhotoImage(file='imagens/telaSaque.png')

Imagemextrato = PhotoImage(file='imagens/telaExtrato.png')

Imagemdeposito = PhotoImage(file='imagens/telaDeposito.png')

Imagemtransferencia = PhotoImage(file='imagens/telaTransferencia.png')

CadastrarImg = PhotoImage(file='imagens/CadastrarBT.png')

EntrarImg = PhotoImage(file='imagens/EntrarBT.png')

RegistrarImg = PhotoImage(file='imagens/Registrar.png')

ExtratoImg = PhotoImage(file='imagens/Extrato.png')

SaqueImg = PhotoImage(file='imagens/Saque.png')

Depositoicon = PhotoImage(file='imagens/Deposito.png')

TransferenciaImg = PhotoImage(file='imagens/Transferencia.png')

OlhoImg = PhotoImage(file='imagens/olho.png')

HomeImg = PhotoImage(file='imagens/home.png')

VoltarImg = PhotoImage(file='imagens/Voltar.png')

BonecoImg = PhotoImage(file='imagens/Buneco.png')

CincoImg = PhotoImage(file='imagens2/cinco.png')

DezImg = PhotoImage(file='imagens2/dez.png')

VinteImg = PhotoImage(file='imagens2/vinte.png')

CincoentaImg = PhotoImage(file='imagens2/cinquenta.png')

CemImg = PhotoImage(file='imagens2/cem.png')

DoiszentosImg = PhotoImage(file='imagens2/duzentos.png')

SacarImg = PhotoImage(file='imagens2/Sacar.png')

DepositarImg = PhotoImage(file='imagens2/Depositar.png')

TransferirImg = PhotoImage(file='imagens2/Transferir.png')


# ================================================= Frame Entrada ================================================
Entrada = Frame(janela)
Cadastrar = Label(Entrada,
                  image=imagem)

Bt_Cadastrar = Button(Entrada,
                      text='Cadastrar',
                      bd=0,
                      image=CadastrarImg,
                      command=lambda: [tela_cadastro.pack(), Entrada.pack_forget()])

Bt_Entrar = Button(Entrada,
                   text='Entrar',
                   bd=0,
                   image=EntrarImg,
                   command=lambda: [tela_login.pack(), Entrada.pack_forget()])

Entrada.pack()
Cadastrar.pack()

Bt_Cadastrar.place(width=186, height=50, x=145, y=488)
Bt_Entrar.place(width=186, height=50, x=145, y=380)

# ================================================= Frame Login ==================================================

tela_login = Frame(janela)
AbaLogin = Label(tela_login,
                 image=ImagemLogin)

Bt_Entrar2 = Button(tela_login,
                    bd=0,
                    image=EntrarImg,
                    command=login)

Bt_voltar = Button(tela_login,
                   bd=0,
                   image=VoltarImg,
                   command=lambda: [tela_login.pack_forget(), Entrada.pack()])


boxEntry = Entry(tela_login,
                 font='Verdana 20')
boxEntry2 = Entry(tela_login,
                  font='Verdana 20',
                  show='*')

boxEntry.place(width=329, height=42, x=71, y=236)
boxEntry2.place(width=329, height=42, x=70, y=371)

Bt_Entrar2.place(width=186, height=49, x=140, y=545)
Bt_voltar.place(width=50, height=40, x=17, y=27)

AbaLogin.pack()

# ===================================================== Frame Cadastro ===================================================

tela_cadastro = Frame(janela)

AbaCadastrar = Label(tela_cadastro,
                     image=ImagemCadastrar)

boxNome = Entry(tela_cadastro,
                font='Verdana 14')

boxSenha = Entry(tela_cadastro,
                 font='Verdana 14')

boxCpf = Entry(tela_cadastro,
               font='Verdana 14')

boxTel = Entry(tela_cadastro,
               font='Verdana 14')

boxDatanasc = Entry(tela_cadastro,
                    font='Verdana 14')

Bt_Registrar = Button(tela_cadastro,
                      bd=0,
                      image=RegistrarImg,
                      command=lambda: [registrar()])

Bt_voltar = Button(tela_cadastro,
                   bd=0,
                   image=VoltarImg,
                   command=lambda: [Entrada.pack(), tela_cadastro.pack_forget()])


boxNome.place(width=346, height=23, x=99, y=257)

boxSenha.place(width=238, height=23, x=109, y=301)

boxCpf.place(width=189, height=21, x=99, y=350)

boxTel.place(width=163, height=20, x=103, y=400)

boxDatanasc.place(width=164, height=20, x=163, y=453)

Bt_Registrar.place(width=186, height=50, x=136, y=610)

Bt_voltar.place(width=50, height=40, x=17, y=27)

AbaCadastrar.pack()

# ================================================ Frame Saldo ========================================================

tela_saldo = Frame(janela)

AbaSaldo = Label(tela_saldo,
                 image=ImagemSaldo)

exibir_saldo = Label(tela_saldo,
                     font='Verdana 14',
                     bg='#fff')

nome_conta = Label(tela_saldo,
                   background='#f01f44',
                   font='Verdana 20',
                   text='Olá,',
                   fg='#fff')

Bt_Boneco = Button(tela_saldo,
                   bd=0,
                   image=BonecoImg)

Bt_extrato = Button(tela_saldo,
                    bd=0,
                    image=ExtratoImg,
                    command=lambda: [executa_historico(), tela_extrato.pack(), tela_saldo.pack_forget()])


Bt_saque = Button(tela_saldo,
                  bd=0,
                  image=SaqueImg,
                  command=lambda: [tela_saque.pack(), tela_saldo.pack_forget()])


Bt_deposito = Button(tela_saldo,
                     bd=0,
                     image=Depositoicon,
                     command=lambda: [tela_deposito.pack(), tela_saldo.pack_forget()])


Bt_transferencia = Button(tela_saldo,
                          bd=0,
                          image=TransferenciaImg,
                          command=lambda: [tela_transferencia.pack(), tela_saldo.pack_forget()])


Bt_saldo = Button(tela_saldo,
                  bd=0,
                  image=OlhoImg,
                  command=esconder_saldo)

Bt_home = Button(tela_saldo,
                 bd=0,
                 image=HomeImg,
                 command=lambda: [Entrada.pack(), tela_saldo.pack_forget()])


AbaSaldo.pack()

exibir_saldo.place(width=140, height=30, x=155, y=169)

nome_conta.place(width=244, height=47, x=102, y=24)

Bt_Boneco.place(width=50, height=50, x=21, y=26)

Bt_extrato.place(width=162, height=125, x=38, y=296)

Bt_saque.place(width=163, height=125, x=257, y=296)

Bt_deposito.place(width=163, height=125, x=37, y=473)

Bt_transferencia.place(width=160, height=125, x=258, y=472)

Bt_saldo.place(width=52, height=33, x=328, y=164)

Bt_home.place(width=55, height=61, x=203, y=697)

# ================================================ Frame Saque =================================================

tela_saque = Frame(janela)

AbaSaque = Label(tela_saque,
                 image=Imagemsaque)

exibir_valor = Label(tela_saque,
                     bg='#fff',
                     font='Verdana 16',
                     text='R$',
                     bd=0)

Bt_cinco = Button(tela_saque,
                  bd=0,
                  image=CincoImg)

Bt_dez = Button(tela_saque,
                bd=0,
                image=DezImg)

Bt_vinte = Button(tela_saque,
                  bd=0,
                  image=VinteImg)

Bt_cinquenta = Button(tela_saque,
                      bd=0,
                      image=CincoentaImg)

Bt_cem = Button(tela_saque,
                bd=0,
                image=CemImg)

Bt_duzentos = Button(tela_saque,
                     bd=0,
                     image=DoiszentosImg)

Bt_sacar = Button(tela_saque,
                  bd=0,
                  image=SacarImg,
                  command=executa_saque)

entryValor_saque = Entry(tela_saque,
                         font='Verdana 12')

Bt_voltar = Button(tela_saque,
                   bd=0,
                   image=VoltarImg,
                   command=lambda: [tela_saldo.pack(), tela_saque.pack_forget()])


exibir_valor.place(width=167, height=25, x=152, y=465)


Bt_cinco.place(width=135, height=76, x=13, y=251)

Bt_dez.place(width=135, height=76, x=165, y=251)

Bt_vinte.place(width=135, height=76, x=317, y=251)

Bt_cinquenta.place(width=135, height=76, x=13, y=346)

Bt_cem.place(width=135, height=76, x=165, y=346)

Bt_duzentos.place(width=135, height=76, x=317, y=346)

Bt_sacar.place(width=190, height=31, x=135, y=683)

Bt_voltar.place(width=50, height=40, x=21, y=27)

entryValor_saque.place(width=356, height=20, x=55, y=594)

AbaSaque.pack()


# ============================================== Frame Extrato =================================================

tela_extrato = Frame(janela)

AbaExtrato = Label(tela_extrato,
                   image=Imagemextrato)

exibir_extrato = Label(
    tela_extrato, text='executa_historico()', background='#fff')

Bt_voltar = Button(tela_extrato,
                   bd=0,
                   image=VoltarImg,
                   command=lambda: [tela_saldo.pack(), tela_extrato.pack_forget()])


Bt_voltar.place(width=50, height=40, x=21, y=27)

exibir_extrato.place(width=60, height=30, x=50, y=120)

AbaExtrato.pack()

# ============================================== Frame Deposito ==================================================

tela_deposito = Frame(janela)

AbaDeposito = Label(tela_deposito,
                    image=Imagemdeposito)

Lb_saldo = Label(tela_deposito,
                 bg='#fff',
                 font='Verdana 16',
                 text='R$', bd=0)


Bt_cinco = Button(tela_deposito,
                  bd=0,
                  image=CincoImg)

Bt_dez = Button(tela_deposito,
                bd=0,
                image=DezImg)

Bt_vinte = Button(tela_deposito,
                  bd=0,
                  image=VinteImg)

Bt_cinquenta = Button(tela_deposito,
                      bd=0,
                      image=CincoentaImg)

Bt_cem = Button(tela_deposito,
                bd=0,
                image=CemImg)

Bt_duzentos = Button(tela_deposito,
                     bd=0,
                     image=DoiszentosImg)

Bt_deposito = Button(tela_deposito,
                     bd=0,
                     image=DepositarImg,
                     command=executa_deposito)


Bt_voltar = Button(tela_deposito,
                   bd=0,
                   image=VoltarImg,
                   command=lambda: [tela_saldo.pack(), tela_deposito.pack_forget()])


entryValor_deposito = Entry(tela_deposito,
                            font='Verdana 12')

Lb_saldo.place(width=167, height=25, x=152, y=465)

Bt_cinco.place(width=135, height=76, x=13, y=251)

Bt_dez.place(width=135, height=76, x=165, y=251)

Bt_vinte.place(width=135, height=76, x=317, y=251)

Bt_cinquenta.place(width=135, height=76, x=13, y=346)

Bt_cem.place(width=135, height=76, x=165, y=346)

Bt_duzentos.place(width=135, height=76, x=317, y=346)

Bt_deposito.place(width=190, height=31, x=137, y=687)

Bt_voltar.place(width=50, height=40, x=21, y=27)

entryValor_deposito.place(width=356, height=20, x=55, y=594)

AbaDeposito.pack()

# ============================================== Frame Transferencia ==========================================

tela_transferencia = Frame(janela)

AbaTransferencia = Label(tela_transferencia,
                         image=Imagemtransferencia)

Bt_transferir = Button(tela_transferencia,
                       bd=0,
                       image=TransferirImg,
                       command=executa_transferencia)

Bt_voltar = Button(tela_transferencia,
                   bd=0,
                   image=VoltarImg,
                   command=lambda: [tela_saldo.pack(), tela_transferencia.pack_forget()])


entryescolher_CPF = Entry(tela_transferencia,
                          font='Verdana 16',
                          fg='#2d2e3d')

entryvalor_transferencia = Entry(tela_transferencia,
                                 font='Verdana 16',
                                 fg='#2d2e3d')

Bt_transferir.place(width=190, height=31, x=145, y=697)

Bt_voltar.place(width=50, height=40, x=21, y=27)

entryescolher_CPF.place(width=411, height=42, x=27, y=265)

entryvalor_transferencia.place(width=408, height=42, x=28, y=466)

AbaTransferencia.pack()
# ================================== roda o programa ==================================
janela.mainloop()


# .place(width='largura', height='altura', x='Cord_X', y=Cord_Y)
