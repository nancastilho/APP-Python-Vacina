from tkinter import *
from tkinter import messagebox


class Gui():
    """Classe que define a interface gráfica da aplicação
    """
    x_pad = 5
    y_pad = 3
    width_entry = 30

    # Criando a janela...
    window = Tk()
    window.wm_title("AgroVac")
    window.configure(bg='#696969')

    messagebox.showinfo(title="AgroVac", message="Bem Vindo a AgroVac")

    # Criando variáveis que armazenarão o texto inserido pelo usuário...
    txtNome = StringVar()
    txtEndereco = StringVar()
    txtVacinas = StringVar()
    txtData = StringVar()
    txtTelefone = StringVar()

    # Criando os objetos que estarão na janela...
    lbltitulo = Label(window, text="AgroVac🐮", background="#A9A9A9",
                      font="impact 30", relief="groove", bd=5)
    lblnome = Label(window, text="Nome", background="#A9A9A9",
                    relief="raised", bd=1)
    lblendereco = Label(window, text="Enderço",
                        background="#A9A9A9", relief="raised", bd=1)
    lblvacinas = Label(window, text="Vacinas a Aplicar",
                       background="#A9A9A9", relief="raised", bd=1)
    lbldata = Label(window, text="Data de Vacinação",
                    background="#A9A9A9", relief="raised", bd=1)
    lbltelefone = Label(window, text="Telefone",
                        background="#A9A9A9", relief="raised", bd=1)
    entNome = Entry(window, textvariable=txtNome, width=width_entry,
                    background="#A9A9A9", relief="sunken", bd=2)
    entEndereco = Entry(window, textvariable=txtEndereco,
                        width=width_entry, background="#A9A9A9", relief="sunken", bd=2)
    entVacinas = Entry(window, textvariable=txtVacinas,
                       width=width_entry, background="#A9A9A9", relief="sunken", bd=2)
    entData = Entry(window, textvariable=txtData, width=width_entry,
                    background="#A9A9A9", relief="sunken", bd=2)
    entTelefone = Entry(window, textvariable=txtTelefone,
                        width=width_entry, background="#A9A9A9", relief="sunken", bd=2)
    listClientes = Listbox(
        window, width=50, background="#A9A9A9", borderwidth=2, relief="ridge", bd=2)
    scrollClientes = Scrollbar(
        window, background="#A9A9A9", relief="ridge", bd=2)
    btnViewAll = Button(window, text="Ver todos",
                        background="#C0C0C0", relief="ridge", bd=3)
    btnBuscar = Button(window, text="Buscar",
                       background="#C0C0C0", relief="ridge", bd=3)
    btnInserir = Button(window, text="Adicionar Contato",
                        background="#C0C0C0", relief="ridge", bd=3)
    btnUpdate = Button(window, text="Atualizar Contato",
                       background="#C0C0C0", relief="ridge", bd=3)
    btnDel = Button(window, text="Deletar Contato",
                    background="#C0C0C0", relief="ridge", bd=3)
    btnClose = Button(window, text="Fechar",
                      background="#C0C0C0", relief="ridge", bd=3)
    btnLimpar_Todos = Button(window, text="Limpar",
                             background="#C0C0C0", relief="ridge", bd=3)

    # Associando os objetos a grid da janela...
    lbltitulo.grid(row=0, columnspan=5)
    lblnome.grid(row=1, column=0)
    lblendereco.grid(row=2, column=0)
    lblvacinas.grid(row=5, column=0)
    lbldata.grid(row=4, column=0)
    lbltelefone.grid(row=3, column=0)
    entNome.grid(row=1, column=1)
    entEndereco.grid(row=2, column=1)
    entVacinas.grid(row=5, column=1)
    entData.grid(row=4, column=1)
    entTelefone.grid(row=3, column=1)
    listClientes.grid(row=1, column=2, rowspan=10)
    scrollClientes.grid(row=1, column=6, rowspan=10)
    btnViewAll.grid(row=6, column=0, columnspan=2)
    btnBuscar.grid(row=7, column=0, columnspan=2)
    btnInserir.grid(row=8, column=0, columnspan=2)
    btnUpdate.grid(row=9, column=0, columnspan=2)
    btnDel.grid(row=10, column=0, columnspan=2)
    btnLimpar_Todos.grid(row=11, column=0, columnspan=2)
    btnClose.grid(row=12, column=0, columnspan=2)

    # Associando a Scrollbar com a Listbox...
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    # Adicionando um pouco de SWAG a interface...
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        Gui.window.mainloop()
