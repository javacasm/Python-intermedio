from tkinter import *
from tkinter import ttk

# importamos el módulo agenda
import agenda

# cargamos los contactos que están guardados
agenda.cargar_agenda()

lista_campos = ['nombre'] # nos aseguramos de que al menos esté el campo "nombre"


# campos disponibles
for contacto in agenda.lista_contactos:
    for clave,valor in contacto.items():
        if clave not in lista_campos:
            lista_campos.append(clave)

window_base = Tk()
window_base.title(f'Agenda {agenda.v}')

style = ttk.Style()
style.theme_use('clam')

tree = ttk.Treeview(window_base, 
                    column=lista_campos,
                    show='headings')
 
contador = 1
for campo in lista_campos:
    columna_id = "#"+str(contador)
    if campo == 'nombre':
        tree.column(columna_id, anchor = CENTER)
    elif campo == 'edad':
        tree.column(columna_id, anchor = E )
    else:
        tree.column(columna_id, anchor = W )

    tree.heading(columna_id, text=campo)
    contador += 1


for contacto in agenda.lista_contactos:
    valores = []
    for campo in lista_campos:
        if campo in contacto.keys():
            valores.append(contacto[campo])
        else:
            valores.append('-')
    print(valores)
    tree.insert("",END,values=valores) # insertamos al final de la tabla
            
tree.pack()


def about_window():
    window_about = Tk()
    window_about.title('Acerca de...')
    label_about = Label(window_about,
                      text = f'Agenda{agenda.v}',
                      justify = CENTER,
                      font = ('Poppins 18 bold'))
    label_about.grid(row=0,column=0)

# Menu de aplicacion

menubar = Menu(window_base)
window_base.config(menu=menubar)

# grupo de menus
file_menu = Menu(menubar)
menubar.add_cascade(label = 'Archivo',
                    menu = file_menu)

# menu salir
file_menu.add_command(label = 'Salir',
                      command = window_base.destroy)

# menu about
file_menu.add_command(label = 'Acerca de ...',
                      command = about_window)

window_base.mainloop()
