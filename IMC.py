from tkinter import *

def imc():
    try:
        Resultado['text'] =  round(float(barra_peso.get())/(float(barra_altura.get())*float (barra_altura.get())),2)
    except:
        Resultado['text'] = 'Valor Inválido'

janela = Tk()
janela.minsize (width=400, height=250)
janela.maxsize (width=400, height=250)
janela.config (background= '#979CDB')

IMC = Label(janela, text='Calculo de IMC', font='Arial 20', background='#979CDB')
Peso = Label(janela, text='Peso', font='Arial 18',background='#979CDB')
Altura = Label(janela,text='Altura', font='Arial 18',background='#979CDB')
Resultado = Label(janela,font='Arial 18',background='#979CDB')


barra_peso = Entry(janela,font='Arial 14')
barra_altura = Entry(janela,font='Arial 14')


Botao_imc = Button(janela,text='IMC', font='Arial 18', command=imc)


barra_peso.grid(row=1,column=1)
barra_altura.grid(row=2,column=1)

Peso.grid(row=1,column=0)
Altura.grid(row=2,column=0)

IMC.grid(row=0,column=1)
Botao_imc.grid (row=4,column=0)

Resultado.grid(row=4,column=1)

janela.mainloop()