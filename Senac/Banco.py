from itertools import tee
from tkinter import *
from Classe_cadastro import *
import ajuda


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
    nomes_registrados.append(Cadastro(boxEntry3.get(), boxEntry5.get()))
    for i in range(len(nomes_registrados)):
        print(nomes_registrados[i].nome,nomes_registrados[i].cpf)

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
Cadastrar = Label(Entrada, image=imagem)

Bt_Cadastrar = Button(Entrada, text='Cadastrar', bd=0,
                      image=CadastrarImg, command=lambda: [tela_cadastro.pack(), Entrada.pack_forget()])

Bt_Entrar = Button(Entrada, text='Entrar', bd=0,
                   image=EntrarImg, command=lambda: [tela_login.pack(), Entrada.pack_forget()])


Entrada.pack()
Cadastrar.pack()

Bt_Cadastrar.place(width=186, height=50, x=145, y=488)
Bt_Entrar.place(width=186, height=50, x=145, y=380)

# ================================================= Frame Login ==================================================

tela_login = Frame(janela)
AbaLogin = Label(tela_login, image=ImagemLogin)

Bt_Entrar2 = Button(tela_login, bd=0, image=EntrarImg, command=lambda: [
                    tela_saldo.pack(), tela_login.pack_forget()])

boxEntry = Entry(tela_login, font='Verdana 20')
boxEntry2 = Entry(tela_login, font='Verdana 20', show='*')

boxEntry.place(width=341, height=52, x=64, y=230)
boxEntry2.place(width=340, height=54, x=65, y=365)

AbaLogin.pack()

# ===================================================== Frame Cadastro ===================================================

tela_cadastro = Frame(janela)

AbaCadastrar = Label(tela_cadastro, image=ImagemCadastrar)

Bt_Registrar = Button(tela_cadastro, bd=0, image=RegistrarImg, command=lambda: [registrar()])

Bt_voltar = Button(tela_cadastro, bd=0, image=VoltarImg, command=lambda: [Entrada.pack(), tela_cadastro.pack_forget()])

boxEntry3 = Entry(tela_cadastro)

boxEntry4 = Entry(tela_cadastro)

boxEntry5 = Entry(tela_cadastro)

boxEntry6 = Entry(tela_cadastro)

boxEntry7 = Entry(tela_cadastro)

boxEntry8 = Entry(tela_cadastro)

boxEntry9 = Entry(tela_cadastro)

boxEntry10 = Entry(tela_cadastro)

boxEntry11 = Entry(tela_cadastro)

boxEntry12 = Entry(tela_cadastro)

boxEntry13 = Entry(tela_cadastro)

boxEntry14 = Entry(tela_cadastro)


boxEntry.place(width=341, height=52, x=64, y=230)

boxEntry2.place(width=340, height=54, x=65, y=365)

boxEntry3.place(width=353, height=20, x=96, y=116)

boxEntry4.place(width=349, height=21, x=96, y=157)

boxEntry5.place(width=164, height=21, x=71, y=202)

boxEntry6.place(width=155, height=22, x=291, y=201)

boxEntry7.place(width=299, height=22, x=129, y=242)

boxEntry8.place(width=360, height=21, x=82, y=349)

boxEntry9.place(width=349, height=21, x=94, y=394)

boxEntry10.place(width=348, height=21, x=100, y=439)

boxEntry11.place(width=119, height=21, x=190, y=485)

boxEntry12.place(width=65, height=20, x=387, y=486)

boxEntry13.place(width=103, height=18, x=75, y=525)

boxEntry14.place(width=102, height=20, x=261, y=524)

Bt_Entrar2.place(width=186, height=49, x=140, y=545)

Bt_Registrar.place(width=186, height=50, x=136, y=610)

Bt_voltar.place(width=50, height=40, x=21, y=27)

AbaCadastrar.pack()

# ================================================ Frame Saldo ========================================================

tela_saldo = Frame(janela)

AbaSaldo = Label(tela_saldo, image=ImagemSaldo)

Bt_extrato = Button(tela_saldo, bd=0, image=ExtratoImg, command=lambda: [
    tela_extrato.pack(), tela_saldo.pack_forget()])

Bt_saque = Button(tela_saldo, bd=0, image=SaqueImg, command=lambda: [
                  tela_saque.pack(), tela_saldo.pack_forget()])

Bt_deposito = Button(tela_saldo, bd=0, image=Depositoicon, command=lambda: [
                     tela_deposito.pack(), tela_saldo.pack_forget()])

Bt_transferencia = Button(tela_saldo, bd=0, image=TransferenciaImg, command=lambda: [
                          tela_transferencia.pack(), tela_saldo.pack_forget()])

Bt_saldo = Button(tela_saldo, bd=0, image=OlhoImg)

Bt_home = Button(tela_saldo, bd=0, image=HomeImg, command=lambda: [
                 Entrada.pack(), tela_saldo.pack_forget()])


AbaSaldo.pack()
Bt_extrato.place(width=162, height=125, x=38, y=296)

Bt_saque.place(width=163, height=125, x=257, y=296)

Bt_deposito.place(width=163, height=125, x=37, y=473)

Bt_transferencia.place(width=160, height=125, x=258, y=472)

Bt_saldo.place(width=60, height=40, x=325, y=160)

Bt_home.place(width=55, height=61, x=203, y=697)

# ================================================ Frame Saque =================================================

tela_saque = Frame(janela)

AbaSaque = Label(tela_saque, image=Imagemsaque)

entryValor2 = Label(tela_saque, bg='#fff', font='Verdana 16', text='R$', bd=0)

Bt_cinco = Button(tela_saque, bd=0, image=CincoImg)

Bt_dez = Button(tela_saque, bd=0, image=DezImg)

Bt_vinte = Button(tela_saque, bd=0, image=VinteImg)

Bt_cinquenta = Button(tela_saque, bd=0, image=CincoentaImg)

Bt_cem = Button(tela_saque, bd=0, image=CemImg)

Bt_duzentos = Button(tela_saque, bd=0, image=DoiszentosImg)

Bt_sacar = Button(tela_saque, bd=0, image=SacarImg)

Bt_voltar = Button(tela_saque, bd=0, image=VoltarImg, command=lambda: [
                   tela_saldo.pack(), tela_saque.pack_forget()])

entryValor2.place(width=167, height=25, x=152, y=465)

entryValor = Entry(tela_saque)

Bt_cinco.place(width=135, height=76, x=13, y=251)

Bt_dez.place(width=135, height=76, x=165, y=251)

Bt_vinte.place(width=135, height=76, x=317, y=251)

Bt_cinquenta.place(width=135, height=76, x=13, y=346)

Bt_cem.place(width=135, height=76, x=165, y=346)

Bt_duzentos.place(width=135, height=76, x=317, y=346)

Bt_sacar.place(width=190, height=31, x=135, y=683)

Bt_voltar.place(width=50, height=40, x=21, y=27)

entryValor.place(width=356, height=20, x=55, y=594)

AbaSaque.pack()


# ============================================== Frame Extrato =================================================

tela_extrato = Frame(janela)

AbaExtrato = Label(tela_extrato, image=Imagemextrato)

Bt_voltar = Button(tela_extrato, bd=0, image=VoltarImg, command=lambda: [
                   tela_saldo.pack(), tela_extrato.pack_forget()])

Bt_voltar.place(width=50, height=40, x=21, y=27)

AbaExtrato.pack()

# ============================================== Frame Deposito ==================================================

tela_deposito = Frame(janela)

AbaDeposito = Label(tela_deposito, image=Imagemdeposito)

entryValor2 = Label(tela_deposito, bg='#fff', font='Verdana 16', text='R$', bd=0)

Bt_cinco = Button(tela_deposito, bd=0, image=CincoImg)

Bt_dez = Button(tela_deposito, bd=0, image=DezImg)

Bt_vinte = Button(tela_deposito, bd=0, image=VinteImg)

Bt_cinquenta = Button(tela_deposito, bd=0, image=CincoentaImg)

Bt_cem = Button(tela_deposito, bd=0, image=CemImg)

Bt_duzentos = Button(tela_deposito, bd=0, image=DoiszentosImg)

Bt_deposito = Button(tela_deposito, bd=0, image=DepositarImg)

Bt_voltar = Button(tela_deposito, bd=0, image=VoltarImg, command=lambda: [
                   tela_saldo.pack(), tela_deposito.pack_forget()])


entryValor = Entry(tela_deposito)

entryValor2.place(width=167, height=25, x=152, y=465)

Bt_cinco.place(width=135, height=76, x=13, y=251)

Bt_dez.place(width=135, height=76, x=165, y=251)

Bt_vinte.place(width=135, height=76, x=317, y=251)

Bt_cinquenta.place(width=135, height=76, x=13, y=346)

Bt_cem.place(width=135, height=76, x=165, y=346)

Bt_duzentos.place(width=135, height=76, x=317, y=346)

Bt_deposito.place(width=190, height=31, x=137, y=687)

Bt_voltar.place(width=50, height=40, x=21, y=27)

entryValor.place(width=356, height=20, x=55, y=594)

AbaDeposito.pack()

# ============================================== Frame Transferencia ==========================================

tela_transferencia = Frame(janela)

AbaTransferencia = Label(tela_transferencia, image=Imagemtransferencia)

Bt_transferir = Button(tela_transferencia, bd=0, image=TransferirImg)

Bt_voltar = Button(tela_transferencia, bd=0, image=VoltarImg, command=lambda: [
                   tela_saldo.pack(), tela_transferencia.pack_forget()])

entryTipos_Conta = Entry(tela_transferencia, font='Verdana 16', fg='#2d2e3d')
entryAgencia = Entry(tela_transferencia, font='Verdana 16', fg='#2d2e3d')
entryConta = Entry(tela_transferencia, font='Verdana 16', fg='#2d2e3d')
entryTransferencia = Entry(tela_transferencia, font='Verdana 16', fg='#2d2e3d')

Bt_transferir.place(width=190, height=31, x=145, y=697)
Bt_voltar.place(width=50, height=40, x=21, y=27)

entryTipos_Conta.place(width=410, height=41, x=23, y=237)
entryAgencia.place(width=409, height=42, x=24, y=335)
entryConta.place(width=411, height=42, x=23, y=447)
entryTransferencia.place(width=409, height=42, x=24, y=566)
AbaTransferencia.pack()
# ================================== roda o programa ==================================
janela.mainloop()


# .place(width='largura', height='altura', x='Cord_X', y=Cord_Y)
