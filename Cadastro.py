from tkinter import *

def tel(event = None):
    tel = Entry_Telefone.get().replace('-', '').replace('(', '').replace(')', '').replace(' ','')[:12]
    novo_texto = ''

    if event.keysym.lower() == 'Backspace': return

    for content in range(len(tel)):

        if tel[content] in '0123456789':
            if content == 0: novo_texto += '(' + tel[content]
            elif content == 2: novo_texto += tel[content] + ')'
            elif content in [2, 3]: novo_texto += tel[content] + ' '
            elif content == 7: novo_texto += tel[content] + '-'
            else: novo_texto += tel[content]
    
    Entry_Telefone.delete(0, 'end')
    Entry_Telefone.insert(0, novo_texto)

def test(event = None):

    text = Entry_CPF.get().replace('.', '').replace('-','')[:11]
    new_text = ''

    if event.keysym.lower() == 'Backspace': return

    for contador in range(len(text)):

        if text[contador] in '0123456789': 
            if contador in [2,5]: new_text += text[contador] + '.'
            elif contador == 8: new_text += text[contador] + '-'
            else: new_text += text[contador]

    Entry_CPF.delete(0, 'end')
    Entry_CPF.insert(0, new_text)
    
# =======================================================================================<Inicio>==================================================================================================
janela = Tk()
janela.title('Cadastro')
janela.config(background='#666666')

# =======================================================================================<Frames>==================================================================================================
fr1 = Frame(janela, background='#3c3c3c', width=100,
            borderwidth=15, relief='sunken')

fr2 = Frame(janela, background='#3c3c3c', width=100,
            borderwidth=15, relief='sunken')

fr3 = Frame(janela, background='#3c3c3c', width=100,
            borderwidth=15, relief='sunken')

login = Frame(janela, background='#3c3c3c', width=70,
              borderwidth=12, relief='sunken')

# ======================================================================================<MinsizeMaxsize>==========================================================================================

# =======================================================================================<RowConfigure>============================================================================================
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

# =======================================================================================<ColumnConfigure>=========================================================================================

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)
janela.grid_columnconfigure(4, weight=1)
janela.grid_columnconfigure(5, weight=1)
janela.grid_columnconfigure(6, weight=1)
janela.grid_columnconfigure(7, weight=1)

# =======================================================================================<LabelFr1>================================================================================================

Dados = Label(fr1, text='Dados Pessoais', font='Arial 18',
              background='#3c3c3c', fg='#fff', pady=10, borderwidth=2, anchor=W)
Nome = Label(fr1, text='Nome:', font='Arial 16', background='#3c3c3c',
             fg='#fff', borderwidth=5, anchor=E, padx=10)
DataNasc = Label(fr1, text='Data Nasc:', font='Arial 16',
                 background='#3c3c3c', fg='#fff', anchor=E, padx=10)
CPF = Label(fr1, text='CPF:', font='Arial 16',
            background='#3c3c3c', fg='#fff', anchor=E, padx=10,)
Telefone = Label(fr1, text='Telefone:', font='Arial 16',
                 background='#3c3c3c', fg='#fff', anchor=E, padx=10)
Sexo = Label(fr1,text='Sexo:',font='Arial 16',
                background='#3c3c3c', fg='#fff', anchor=E, padx=10, pady=3)

# =======================================================================================<LabelFr2>================================================================================================

Endereco = Label(fr2, text='Endereço', font='Arial 18',
                 background='#3c3c3c', fg='#fff', pady=10, borderwidth=2, anchor=W)
Rua = Label(fr2, text='Rua:', font='Arial 16', background='#3c3c3c',
            fg='#fff', borderwidth=5, anchor=E, padx=10)
Numero = Label(fr2, text='N°:', font='Arial 16',
               background='#3c3c3c', fg='#fff', anchor=E, padx=5)
UF = Label(fr2, text='UF:', font='Arial 16',
           background='#3c3c3c', fg='#fff', padx=5)
Bairro = Label(fr2, text='Bairro:', font='Arial 16',
               background='#3c3c3c', fg='#fff', anchor=E, padx=10)
Cidade = Label(fr2, text='Cidade:', font='Arial 16',
               background='#3c3c3c', fg='#fff', anchor=E, padx=10)

# =======================================================================================<LabelFr3>================================================================================================

Login = Label(login, text='Login:', font='Arial 16',
              background='#3c3c3c', fg='#fff', anchor=W, padx=10)
Senha = Label(login, text='Senha:', font='Arial 16',
              background='#3c3c3c', fg='#fff', anchor=W, padx=10)

# ======================================================================================<EntryFr1>=================================================================================================

Entry_Nome = Entry(fr1, font='Arial 15', width=60)
Entry_DataNasc = Entry(fr1, font='Arial 15', width=15)
Entry_CPF = Entry(fr1, font='Arial 15', width=30)
Entry_CPF.bind('<KeyRelease>', test)
Entry_Telefone = Entry(fr1, font='Arial 15', width=15)
Entry_Telefone.bind('<KeyRelease>', tel)

# ======================================================================================<EntryFr2>=================================================================================================

Entry_Rua = Entry(fr2, font='Arial 15', width=60)
Entry_Numero = Entry(fr2, font='Arial 15', width=5)
Entry_UF = Entry(fr2, font='Arial 15', width=5)
Entry_Bairro = Entry(fr2, font='Arial 15', width=30)
Entry_Cidade = Entry(fr2, font='Arial 15', width=20)

# ======================================================================================<EntryLogin>===============================================================================================

Entry_Login = Entry(login, font='Arial 15', width=25)
Entry_Senha = Entry(login, font='Arial 15', width=25, show='*')

# ======================================================================================<ButtonsFr1>===============================================================================================

Bt1 = Button(fr3, text='Voltar', font='Arial 14', background='#666666', fg='#fff', width=10, padx=5,
             command=lambda: [login.grid(row=0, column=3, columnspan=2), fr1.grid_forget(), fr2.grid_forget(), fr3.grid_forget()])
Bt2 = Button(fr3, text='Sair', font='Arial 14', background='#666666',
             fg='#fff', width=5, padx=5, command=quit)
Bt3 = Checkbutton(fr1,text='Feminino',font='Arial 14',background='#3c3c3c', fg='#fff', padx=5, pady=5)

Bt4 = Checkbutton(fr1,text='Masculino',font='Arial 14',background='#3c3c3c', fg='#fff', padx=5, pady=5)

# ======================================================================================<ButtonsLogin>=============================================================================================

Bt_voltar = Button(login, text='Cadastrar', font='Arial 14', background='#666666', fg='#fff', width=10, padx=5, command=lambda: [
                   login.grid_forget(), fr1.grid(sticky=NSEW), fr2.grid(sticky=NSEW), fr3.grid(sticky=NSEW)])
Bt_Entrar = Button(login, text='Entrar', font='Arial 14',
                   background='#666666', fg='#fff', width=10, padx=5)

# =======================================================================================<LabelFr1>================================================================================================

Dados.grid(row=0, column=0, columnspan=3, sticky=NSEW)
Nome.grid(row=1, column=0, sticky=EW)
DataNasc.grid(row=2, column=5, sticky=EW)
CPF.grid(row=2, column=0, sticky=EW)
Telefone.grid(row=2, column=3, sticky=EW)
Sexo.grid(row=3,column=0)

# =======================================================================================<LabelFr2>================================================================================================

Endereco.grid(row=0, column=0, columnspan=2, sticky=NSEW)
Rua.grid(row=1, column=0, sticky=EW)
Numero.grid(row=1, column=5, sticky=EW)
UF.grid(row=2, column=5)
Bairro.grid(row=2, column=0, sticky=EW)
Cidade.grid(row=2, column=2, sticky=EW)

# =======================================================================================<EntryFr1>================================================================================================

Entry_Nome.grid(row=1, column=1, columnspan=7, sticky=EW)
Entry_DataNasc.grid(row=2, column=6)
Entry_CPF.grid(row=2, column=1)
Entry_Telefone.grid(row=2, column=4)

# =======================================================================================<EntryFr2>================================================================================================

Entry_Rua.grid(row=1, column=1, sticky=EW, columnspan=3)
Entry_Numero.grid(row=1, column=6, sticky=EW)
Entry_UF.grid(row=2, column=6)
Entry_Bairro.grid(row=2, column=1, sticky=EW)
Entry_Cidade.grid(row=2, column=3, sticky=EW, columnspan=2)

# =======================================================================================<LabelLogin>==============================================================================================

Login.grid(row=0, column=0, columnspan=1, sticky=NSEW)
Senha.grid(row=1, column=0, columnspan=1, sticky=NSEW)

# =======================================================================================<EntryLogin>==============================================================================================

Entry_Login.grid(row=0, column=1, columnspan=2, sticky=NSEW)
Entry_Senha.grid(row=1, column=1, columnspan=2, sticky=NSEW)

# =======================================================================================<BotõesFr1>===============================================================================================

Bt1.grid(row=0, column=0)
Bt2.grid(row=0, column=1)
Bt3.grid(row=3,column=1)
Bt4.grid(row=3,column=2)

# =======================================================================================<BotõesLogin>=============================================================================================

Bt_voltar.grid(row=2, column=1, sticky=NSEW)
Bt_Entrar.grid(row=2, column=2, sticky=NSEW)

# ==================================================================================<Inicializador>================================================================================================

login.grid(row=0, column=3, columnspan=2)
janela.mainloop()
