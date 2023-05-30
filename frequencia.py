from tkinter import *
from tkinter import ttk
from tkinter import messagebox

corRoxo = "#8A2BE2"

def inserir():
    if vnmr.get()=="" or vnome.get()=="" or vhora.get()=="":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    tv.insert("","end", values=(vnmr.get(), vnome.get(), vhora.get()))
    vnmr.delete(0, END)
    vnome.delete(0, END)
    vhora.delete(0, END)
    vnmr.focus()
    
def deletar():
    try:
        itemSelecionado = tv.selection()[0]    
        tv.delete(itemSelecionado)
    except:
         messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")
    
    
def obter():
    try: 
        itemSelecionado = tv.selection()[0]
        valores= tv.item(itemSelecionado, "values")
        print("ID: " + valores[0])
        print("Nome: " + valores[1])
        print("Horário: " + valores[2])
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado")
        
app = Tk()
app.title("Sistema Infrequencia")
app.geometry('472x330')


lbnmr =Label(app, text="Número")
vnmr= Entry(app)

lbnome=Label(app, text="Nome")
vnome= Entry(app)

lbhora=Label(app, text="Horário")
vhora = Entry(app)

tv = ttk.Treeview(app, columns=('numero', 'nome', 'horario'), show='headings')
tv.column('numero', minwidth=10, width=70)
tv.column('nome', width=250)
tv.column('horario', width=150)

tv.heading('numero', text="Número")
tv.heading('nome', text="Nome do Aluno")
tv.heading('horario', text="Horário")

btn_inserir = Button(app, text="Inserir", command= inserir)
btn_deletar = Button(app, text="Deletar", command= deletar)
btn_obter = Button(app, text="Obter", command= obter)

lbnmr.grid(column=0, row=0, stick='w')
vnmr.grid(column=0, row=1)

lbnome.grid(column=1, row=0, stick='w')
vnome.grid(column=1, row=1)

lbhora.grid(column=2, row=0, stick='w')
vhora.grid(column=2, row=1, stick='w')

tv.grid(column=0, row=3, columnspan=3, pady=5)

btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_obter.grid(column=2, row=4)


app.mainloop()
