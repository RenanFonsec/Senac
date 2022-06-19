from tkinter import *
import ajuda

# ================================== back-end ==================================

janela = Tk()
janela.title('Lockbank')
janela.geometry('465x760')
janela.resizable(width=False, height=False)

janela.bind('<Button-1>', ajuda.inicio_place)
janela.bind('<ButtonRelease-1>', lambda arg: ajuda.fim_place(arg, janela))
janela.bind('<Button-2>', lambda arg: ajuda.para_geometry(janela))


# ================================== exportações de imagens ==================================
imagem = PhotoImage(file='imagens/Cadastrar.png')
CadastrarImg = PhotoImage(file='imagens/CadastrarBT.png')
EntrarImg = PhotoImage(file='imagens/EntrarBT.png')
# ================================== front-end ==================================
login = Frame(janela)
f2 = Frame(janela)

Cadastrar = Label(janela, image=imagem)

Bt_Cadastrar = Button(janela, text='Cadastrar', bd=0,
                      image=CadastrarImg)

Bt_Entrar = Button(janela, text='Entrar', bd=0,
                   image=EntrarImg)


Cadastrar.pack()
Bt_Cadastrar.place(width=186, height=50, x=22, y=459)
Bt_Entrar.place(width=186, height=50, x=249, y=459)
# ================================== roda o programa ==================================
janela.mainloop()

# .place(width='largura', height='altura', x='Cord_X', y=Cord_Y)
