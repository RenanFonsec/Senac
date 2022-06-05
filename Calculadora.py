from tkinter import *

# ==========================================================================================<Back-End>==================================================================================================================


def entrada(valor):
    Resultado['text'] += valor


def saida():
    resultado = eval(Resultado['text'])
    Resultado['text'] = str(resultado)


def limpar():
    Resultado['text'] = ''


def apagar():
    Resultado['text'] = Resultado['text'][:-1]


def excluir():
    i = len(Resultado['text']) - 1

    if str(Resultado['text'][i]) == '.' and Resultado['text'][i] == '/' and Resultado['text'][i] == '*' and Resultado['text'][i] == '-' and Resultado['text'][i] == '+' and Resultado['text'][i] == '(' and Resultado['text'][i] == ')':
        print('Valor Invalido')

    else:
        resultado = eval(Resultado['text'])
        Resultado['text'] = str(resultado)


# ==========================================================================================<Front-End>=================================================================================================================
janela = Tk()
janela.title('Calculadora')


janela.grid_rowconfigure(0, weight=1)

janela.grid_rowconfigure(1, weight=1)

janela.grid_rowconfigure(2, weight=1)

janela.grid_rowconfigure(3, weight=1)

janela.grid_rowconfigure(4, weight=1)

janela.grid_rowconfigure(5, weight=1)


janela.grid_columnconfigure(0, weight=1)

janela.grid_columnconfigure(1, weight=1)

janela.grid_columnconfigure(2, weight=1)

janela.grid_columnconfigure(3, weight=1)


janela.minsize(width=500, height=650)
janela.maxsize(width=1920, height=1080)
janela.config(background='#333436')


Resultado = Label(janela, font='Arial 25',
                  background='#333436', foreground='#fff')


botao1 = Button(janela, text='7', font='Arial 18', background='#fff',
                command=lambda: entrada('7'))
botao2 = Button(janela, text='8', font='Arial 18', background='#fff',
                command=lambda: entrada('8'))
botao3 = Button(janela, text='9', font='Arial 18', background='#fff',
                command=lambda: entrada('9'))
botao4 = Button(janela, text='4', font='Arial 18', background='#fff',
                command=lambda: entrada('4'))
botao5 = Button(janela, text='5', font='Arial 18', background='#fff',
                command=lambda: entrada('5'))
botao6 = Button(janela, text='6', font='Arial 18', background='#fff',
                command=lambda: entrada('6'))
botao7 = Button(janela, text='1', font='Arial 18', background='#fff',
                command=lambda: entrada('1'))
botao8 = Button(janela, text='2', font='Arial 18', background='#fff',
                command=lambda: entrada('2'))
botao9 = Button(janela, text='3', font='Arial 18', background='#fff',
                command=lambda: entrada('3'))
botao10 = Button(janela, text='0', font='Arial 18', background='#fff',
                 command=lambda: entrada('0'))

bt1 = Button(janela, text='C', font='Arial 16',
             background='#bc544b', command=lambda: limpar())
bt2 = Button(janela, text='←', font='Arial 18',
             background='#1b98e0', command=lambda: apagar())
bt3 = Button(janela, text='÷', font='Arial 18',
             background='#e6e1e1', command=lambda: entrada('/'))
bt4 = Button(janela, text='⨉', font='Arial 18',
             background='#e6e1e1', command=lambda: entrada('*'))
bt5 = Button(janela, text='-', font='Arial 18',
             background='#e6e1e1', command=lambda: entrada('-'))
bt6 = Button(janela, text='+', font='Arial 18',
             background='#e6e1e1', command=lambda: entrada('+'))
bt7 = Button(janela, text='.', font='Arial 18',
             background='#e6e1e1', command=lambda: entrada('.'))
bt8 = Button(janela, text='=', font='Arial 18',
             background='#e6e1e1', command=lambda: excluir())
bt9 = Button(janela, text='(', font='Arial 18',
             background='#e6e1e1', command=lambda: entrada('('))
bt10 = Button(janela, text=')', font='Arial 18',
              background='#e6e1e1', command=lambda: entrada(')'))

Resultado.grid(row=0, column=0, columnspan=5)

botao1.grid(row=2, column=0, sticky=NSEW)

botao2.grid(row=2, column=1, sticky=NSEW)

botao3.grid(row=2, column=2, sticky=NSEW)

botao4.grid(row=3, column=0, sticky=NSEW)

botao5.grid(row=3, column=1, sticky=NSEW)

botao6.grid(row=3, column=2, sticky=NSEW)

botao7.grid(row=4, column=0, sticky=NSEW)

botao8.grid(row=4, column=1, sticky=NSEW)

botao9.grid(row=4, column=2, sticky=NSEW)

botao10.grid(row=5, column=1, sticky=NSEW)


bt1.grid(row=5, column=2, sticky=NSEW)

bt2.grid(row=1, column=2, sticky=NSEW)

bt3.grid(row=1, column=3, sticky=NSEW)

bt4.grid(row=2, column=3, sticky=NSEW)

bt5.grid(row=3, column=3, sticky=NSEW)

bt6.grid(row=4, column=3, sticky=NSEW)

bt7.grid(row=5, column=0, sticky=NSEW)

bt8.grid(row=5, column=3, sticky=NSEW)

bt9.grid(row=1, column=0, sticky=NSEW)

bt10.grid(row=1, column=1, sticky=NSEW)


janela.bind('1', lambda event: entrada('1'))

janela.bind('2', lambda event: entrada('2'))

janela.bind('3', lambda event: entrada('3'))

janela.bind('4', lambda event: entrada('4'))

janela.bind('5', lambda event: entrada('5'))

janela.bind('6', lambda event: entrada('6'))

janela.bind('7', lambda event: entrada('7'))

janela.bind('8', lambda event: entrada('8'))

janela.bind('9', lambda event: entrada('9'))

janela.bind('0'), lambda event: entrada('0'))

janela.bind('/', lambda event: entrada('/'))

janela.bind('+', lambda event: entrada('+'))

janela.bind('-', lambda event: entrada('-'))

janela.bind('*', lambda event: entrada('*'))

janela.bind('(', lambda event: entrada('('))

janela.bind(')', lambda event: entrada(')'))

janela.bind('<Return>', lambda event: excluir())

janela.mainloop()
