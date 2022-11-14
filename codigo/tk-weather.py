from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

v= 0.3

base_window = Tk()

ancho_ventana = 350
alto_ventana = 400
base_window.geometry(f'{ancho_ventana}x{alto_ventana}+1200+200')
# base_window.geometry('350x400+3400+20') # 2 monitores
base_window.title('Weather forecast')  # asignamos un título

base_window.resizable(height=False,width=False)  # definimos su comportamiento ante cambios de tamaño

# Colores https://www.w3schools.com/colors/colors_picker.asp
color_blanco = '#FFFFFF'
color_negro = '#000000'
color_titulo = '#081F4D'
color_boton = '#0083FF'


def get_weather():
    try:
        tipo = combo_tipo_peticion.get()
        lugar = entry_lugar.get()
        
        if tipo == '' or lugar == '':
            raise Exception
        
        resultado = 'hecho '+tipo+' en ' + lugar
        
        print(resultado)
        
        text_resultado.delete(1.0,"end")
        text_resultado.insert(1.0, resultado)
       

    except Exception as e:
        print('Error',e)        
        showerror(title='Error', message='Debes seleccionar un tipo e introducir un lugar')

        
# Creamos los controles

# frame superior
top_frame_titulo = Frame(base_window,
                         bg = color_titulo,
                         width = ancho_ventana,
                         height = 80)
top_frame_titulo.grid(row=0,column=0)

# etiqueta del título
label_titulo = Label(top_frame_titulo,
                      text = 'Prevision del tiempo',
                      bg = color_titulo,
                      fg = color_blanco,
                      pady = 30, padx = 10,
                      justify = CENTER,
                      font = ('Poppins 18 bold'))
 
label_titulo.grid(row=0,column=0) 

# frame inferior
main_frame = Frame(base_window,
                   width = ancho_ventana,
                   height = alto_ventana - 80)
main_frame.grid(row = 1,column = 0)

font_etiquetas = ('Poppins 15 bold')

# etiquetas de los controles
label_tipo_peticion = Label(main_frame,
                            text = 'Peticion',
                            font = font_etiquetas,
                            justify = LEFT)
label_tipo_peticion.place(x = 5,y = 0)

label_lugar = Label(main_frame,
                    text = 'Lugar',
                    font = font_etiquetas,
                    justify = RIGHT)

label_lugar.place(x = 160,y = 0)        

font_texto = ('Poppins 15')

tipo_peticion = ['actual','pronostico']
combo_tipo_peticion=ttk.Combobox(main_frame,
                                 values = tipo_peticion,
                                 width = 9,
                                 font = font_texto)
combo_tipo_peticion.place(x = 10,y = 32)
                    
entry_lugar = ttk.Entry(main_frame,
                        width = 11,
                        font = font_texto)
entry_lugar.place(x = 170, y = 32)


text_resultado = Text(main_frame,
                      width = 22,
                      height = 6,
                      wrap = WORD,
                      font = font_texto,
                      state = 'normal')

text_resultado.insert(INSERT,"Aqui se mostrara el resultado de haber hecho la peticion")
text_resultado.place(x = 5, y = 72)

button_get = Button(main_frame,
                    text = 'get',
                    bg = color_boton,
                    fg = color_blanco,
                    font = font_etiquetas,
                    command = get_weather)

button_get.place(x = 5, y = 255)
                    
base_window.mainloop() # hasta que la cerremos