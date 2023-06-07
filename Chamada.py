from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

corRoxo = "#8A2BE2"

class Chamada:
    pass

def inserir():    
    global armazenar_nmr
    global armazenar_nome
    global armazenar_hor
    global armazenar_data


    if vnmr.get()=="" or vnome.get()=="" or vhor.get()=="" or vdata.get()=="":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    else:
        tv.insert("","end", values=(vnmr.get(), vnome.get(), vhor.get(), vdata.get()))


    armazenar_nmr = vnmr.get()
    armazenar_nome = vnome.get()
    armazenar_hor = vhor.get()
    armazenar_data = vdata.get()

    connection = pymysql.connect(host="localhost",
                                user="root",
                                passwd="",
                                database="infrequencia")
    cursor = connection.cursor()

    query = (f'INSERT INTO frequencia(numero, nome, horario, data) VALUES ("{armazenar_nmr}", "{armazenar_nome}",  "{armazenar_hor}",  "{armazenar_data}")')
    cursor.execute(query)
    print(query)
    connection.commit()
    connection.close()

    vnmr.delete(0, END)
    vnome.delete(0, END)
    vhor.delete(0, END)
    vdata.delete(0, END)
    vnmr.focus()

def deletar(): 
    if messagebox.askokcancel(title="CONFIRME", message="Você deseja deletar? "):

        item_selecionado = tv.selection()[0]
        tv.delete(item_selecionado)
    
        global armazenar_nmr

        connection = pymysql.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="infrequencia")
        cursor = connection.cursor()

        query = (f'DELETE FROM frequencia WHERE numero = "{armazenar_nmr}"')
        cursor.execute(query)
        print(query)
        connection.commit()
        connection.close()

    else:

        pass

def editar():    
    item_selecionado = tv.selection()[0]

    if not item_selecionado:
        print("oi")
        return
        
    selected_item = tv.selection()[0]
    update_name = tv.item(selected_item)["values"][0]

    update(vnmr.get(), vnome.get(), vhor.get(), vdata.get(), update_name)













app = Tk()
app.title("Sistema Infrequencia")
app.geometry('550x350')
app.resizable(width=FALSE, height=FALSE)


lbnmr = Label(app, text="Número", fg="#8A2BE2", font=("Arial", 10, "bold"))
vnmr= Entry(app)

lbnome = Label(app, text="Nome", fg="#8A2BE2", font=("Arial", 10, "bold"))
vnome= Entry(app)

lbhor = Label(app, text="Horário", fg="#8A2BE2", font=("Arial", 10, "bold"))
vhor = Entry(app)

lbdata =Label(app, text="Data", fg="#8A2BE2", font=("Arial", 10, "bold"))
vdata = Entry(app)

tv = ttk.Treeview(app, columns=('numero', 'nome', 'horario', 'data'), show='headings')

tv.column('numero', minwidth=0, width=60)
tv.column('nome', minwidth=0, width=250)
tv.column('horario', minwidth=0, width=100)
tv.column('data', minwidth=0, width=100)

tv.heading('numero', text="Número")
tv.heading('nome', text="Nome")
tv.heading('horario', text="Horário")
tv.heading('data', text="Data")

btn_inserir = Button(app, text="Inserir", command= inserir, bg="#8A2BE2", fg="#fff",font=("Arial", 10, "bold"))
btn_deletar = Button(app, text="Deletar", command= deletar, bg="#8A2BE2", fg="#fff",font=("Arial", 10, "bold"))
btn_editar = Button(app, text="Editar", command= editar, bg="#8A2BE2", fg="#fff",font=("Arial", 10, "bold"))

lbnmr.grid(column=0, row=0, stick='w')
vnmr.grid(column=0, row=1)

lbnome.grid(column=1, row=0, stick='w')
vnome.grid(column=1, row=1)

lbhor.grid(column=2, row=0, stick='w')
vhor.grid(column=2, row=1, stick='w')

lbdata.grid(column=3, row=0, stick='w')
vdata.grid(column=3, row=1)

tv.grid(column=0, row=3, columnspan=4, pady=5)

btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_editar.grid(column=2, row=4)

app.mainloop()
