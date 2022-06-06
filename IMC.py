from tkinter import *

def imc():
    try:
        Resultado['text'] =  round(float(barra_peso.get())/(float(barra_altura.get())*float (barra_altura.get())),2)
    except:
        Resultado['text'] = 'Valor Inválido'

janela = Tk()

fr1 = Frame (janela,background='#333436')
fr2 = Frame (janela, background='#333436')

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_rowconfigure(3, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

janela.minsize (width=300, height=150)
janela.maxsize (width=1920, height=1080)
janela.config (background='#333436')
janela.title ('Calculador de IMC')



Peso = Label(fr1, text='Peso', font='Arial 18', background='#333436',foreground='#fff')
Altura = Label(fr1, text='Altura', font='Arial 18',background='#333436',foreground='#fff')
Resultado = Label(fr2, font='Arial 18',background='#333436', foreground='#fff')


barra_peso = Entry(fr1, font='Arial 14')
barra_altura = Entry(fr1, font='Arial 14')


Botao_imc = Button(fr2, text='IMC', font='Arial 18', command=imc,background='#333436',foreground='#fff')

fr1.pack()
fr2.pack()

barra_peso.grid(row=0,column=1)
barra_altura.grid(row=1,column=1)

Peso.grid(row=0,column=0)
Altura.grid(row=1,column=0)


Botao_imc.grid (row=0,column=1)

Resultado.grid(row=1,column=1)

janela.mainloop()
