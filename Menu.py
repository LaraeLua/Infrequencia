from tkinter import *
from tkinter import Tk

from Chamada import Application


corVerde = "#00FF00"
corBranca = "#fff"
corLaranja = "#da4f1c"
corPreta = "#000000"
corRoxo = "#8A2BE2"

def Chamada():
    
    from Chamada import Application
    Application = Application()
   
def relatorio():
    
    from relatorio import relatorio
    relatorio()
   
   
   
janela = Tk()
janela.title('Menu')
janela.geometry('500x350')
janela.configure(background=corBranca)
janela.resizable(width=FALSE, height=FALSE)

#dividindo a janela
frame_cima = Frame(janela, width=500, height=50, relief='flat', bg=corRoxo)
frame_cima.grid(row=0, column=0, pady=5, padx=0, sticky=NSEW)

#configurando o frame cima
l_login = Label(frame_cima, text='Menu', anchor=NE, font=("Arial", 20, "bold"), bg=corRoxo, fg=corBranca, padx=3, pady=5)
l_login.place(x=200, y=3)

botaoEnt = Button(janela, width=15, text='Turmas', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo, command = Chamada )
botaoEnt.place(x=85, y=250)

botaoCad = Button(janela, width=15, text='Cadastrar Faltas', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo, command = relatorio )
botaoCad.place(x=290, y=250)

janela.mainloop()
