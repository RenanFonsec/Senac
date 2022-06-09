from tkinter import *




janela = Tk()
janela.title('Cadastro')
janela.config(background='#d2b9d6')


fr1 = Frame (janela,background='#d2b9d6', width=100,  borderwidth=12, relief='sunken')
fr2 = Frame (janela,background='#d2b9d6',width=100,  borderwidth=12, relief='sunken')
fr3 = Frame (janela,background='#d2b9d6', width=100, borderwidth=12, relief='sunken')
login = Frame(janela,background='#d2b9d6', width=100, borderwidth=12, relief='sunken')


janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_rowconfigure(3, weight=1)
janela.grid_rowconfigure(4, weight=1)
janela.grid_rowconfigure(5, weight=1)
janela.grid_rowconfigure(6, weight=1)
janela.grid_rowconfigure(7, weight=1)
janela.grid_rowconfigure(8, weight=1)
janela.grid_rowconfigure(9, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)
janela.grid_columnconfigure(4, weight=1)
janela.grid_columnconfigure(5, weight=1)
janela.grid_columnconfigure(6, weight=1)
janela.grid_columnconfigure(7, weight=1)

Dados = Label(fr1, text='Dados Pessoais',font='Arial 18',background='#d2b9d6',fg='#000', pady=10, borderwidth=2, anchor=W)
Nome = Label(fr1, text='Nome:', font='Arial 16', background='#d2b9d6', fg='#000', borderwidth=5, anchor=E, padx=10)
DataNasc = Label(fr1, text='Data Nasc:', font='Arial 16', background='#d2b9d6', fg='#000', anchor=E, padx=10)
CPF = Label(fr1, text='CPF:', font='Arial 16', background='#d2b9d6', fg='#000', anchor=E, padx=10,)
Telefone = Label(fr1, text='Telefone:', font='Arial 16', background='#d2b9d6', fg='#000', anchor=E, padx=10)

Endereco = Label(fr2, text='Endereço', font='Arial 18',background='#d2b9d6',fg='#000', pady=10, borderwidth=2, anchor=W)
Rua = Label(fr2, text='Rua:', font='Arial 16', background='#d2b9d6', fg='#000', borderwidth=5, anchor=E, padx=10)
Numero = Label(fr2, text='N°:', font='Arial 16', background='#d2b9d6', fg='#000', anchor=E, padx=5)
UF = Label(fr2, text='UF:', font='Arial 16', background='#d2b9d6', fg='#000',padx=5)
Bairro = Label(fr2, text='Bairro:', font='Arial 16', background='#d2b9d6', fg='#000', anchor=E, padx=10)
Cidade = Label(fr2, text='Cidade:', font='Arial 16', background='#d2b9d6', fg='#000', anchor=E, padx=10)

Login = Label(login, text='Login:', font='Arial 16', background='#d2b9d6', fg='#000', anchor=W, padx=10)
Senha = Label(login, text='Senha:', font='Arial 16', background='#d2b9d6', fg='#000', anchor=W, padx=10)

Entry_Nome = Entry(fr1, font='Arial 15',width=60)
Entry_DataNasc = Entry(fr1, font='Arial 15',width=15)
Entry_CPF = Entry(fr1, font='Arial 15', width=30)
Entry_Telefone = Entry(fr1, font='Arial 15', width=15)

Entry_Rua = Entry(fr2, font='Arial 15', width=60)
Entry_Numero = Entry(fr2, font='Arial 15', width=5)
Entry_UF = Entry(fr2, font='Arial 15', width=5)
Entry_Bairro = Entry(fr2, font='Arial 15', width=30)
Entry_Cidade = Entry(fr2, font='Arial 15', width=20)

Entry_Login = Entry(login, font='Arial 15', width=25)
Entry_Senha = Entry(login, font='Arial 15', width=25)

Bt1 = Button(fr3, text='Gravar Dados', font='Arial 14', background='#d7b5d3', fg='#000', width=10, padx=5, command=lambda: [fr1.grid_forget(), fr2.grid_forget(), fr3.grid_forget(), login.grid(sticky=NSEW)])
Bt2 = Button(fr3, text='Sair', font='Arial 14', background='#c797bf', fg='#000', width=5, padx=5, command=quit)

Bt_voltar = Button(login, text='Voltar', font='Arial 14', background='#d7b5d3', fg='#000', width=10, padx=5, command=lambda:[fr1.grid(sticky=NSEW), fr2.grid(sticky=NSEW), fr3.grid(sticky=NSEW), login.grid_forget()])
Bt_Entrar = Button(login, text='Entrar', font='Arial 14', background='#d7b5d3', fg='#000', width=10, padx=5)

fr1.grid(sticky=NSEW)
fr2.grid(sticky=NSEW)
fr3.grid(sticky=NSEW)

Dados.grid(row=0,column=0, columnspan=3, sticky=NSEW)
Nome.grid(row=1,column=0, sticky=EW)
DataNasc.grid(row=2,column=5, sticky=EW)
CPF.grid(row=2,column=0, sticky=EW)
Telefone.grid(row=2, column=3, sticky=EW)

Endereco.grid(row=0,column=0, columnspan=2, sticky=NSEW)
Rua.grid(row=1,column=0, sticky=EW)                            
Numero.grid(row=1,column=5, sticky=EW)
UF.grid(row=2,column=5)
Bairro.grid(row=2,column=0, sticky=EW)
Cidade.grid(row=2, column=2, sticky=EW)

Login.grid(row=0, column=0, columnspan=1, sticky=EW)
Senha.grid(row=1, column=0, columnspan=1, sticky=EW)

Entry_Nome.grid(row=1,column=1, columnspan=7, sticky=EW)
Entry_DataNasc.grid(row=2,column=6)                     
Entry_CPF.grid(row=2,column=1)
Entry_Telefone.grid(row=2,column=4)

Entry_Rua.grid(row=1, column=1, sticky=EW, columnspan=3)
Entry_Numero.grid(row=1,column=6, sticky=EW)
Entry_UF.grid(row=2,column=6)
Entry_Bairro.grid(row=2,column=1, sticky=EW)
Entry_Cidade.grid(row=2,column=3, sticky=EW, columnspan=2)

Entry_Login.grid(row=0, column=1, columnspan=2, sticky=EW)
Entry_Senha.grid(row=1, column=1, columnspan=2, sticky=EW)

Bt1.grid(row=0,column=0)
Bt2.grid(row=0,column=1)

Bt_voltar.grid(row=2, column=1)
Bt_Entrar.grid(row=2, column=2)

#login.grid()

janela.mainloop()