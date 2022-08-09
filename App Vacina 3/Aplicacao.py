from tkinter.constants import END
from GUI import *
import BackEnd as core

app = None


def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)


def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtEndereco.get(
    ), app.txtVacinas.get(), app.txtData.get(), app.txtTelefone.get())
    for r in rows:
        app.listClientes.insert(END, r)


def insert_command():
    core.insert(app.txtNome.get(), app.txtEndereco.get(),
                app.txtVacinas.get(), app.txtData.get(), app.txtTelefone.get())
    messagebox.showinfo(title="AgroVac", message="Contato Adicionado")
    view_command()


def update_command():
    core.update(selected[0], app.txtNome.get(), app.txtEndereco.get(
    ), app.txtVacinas.get(), app.txtData.get(), app.txtTelefone.get())
    messagebox.showinfo(title="AgroVac", message="Contato Atualizado")
    view_command()


def del_command():
    id = selected[0]
    core.delete(id)
    messagebox.showinfo(title="AgroVac", message="Contato Deletado")
    view_command()


def clear_all():
    app.listClientes.delete(0, END)
    app.entNome.delete(0, END)
    app.entEndereco.delete(0, END)
    app.entVacinas.delete(0, END)
    app.entData.delete(0, END)
    app.entTelefone.delete(0, END)


def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entEndereco.delete(0, END)
    app.entEndereco.insert(END, selected[2])
    app.entVacinas.delete(0, END)
    app.entVacinas.insert(END, selected[3])
    app.entData.delete(0, END)
    app.entData.insert(END, selected[4])
    app.entTelefone.delete(0, END)
    app.entTelefone.insert(END, selected[5])
    return selected


if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.btnLimpar_Todos.configure(command=clear_all)
    app.run()
