import os
import json
import zipfile

v = 2.3
print('Agenda v',v)

lista_contactos = []
fichero_datos = 'agenda_v2.json'

def buscar_contacto(nombre):
    global lista_contactos
    for contacto in lista_contactos:
        if contacto['nombre'] == nombre:
            print('Ya existe el contacto '+nombre)
            mostrar_contacto(contacto)
            return True
    print('No existe el contacto '+nombre)
    return False

def añadir_contactos():
    global lista_contactos
    while True:
        nombre = input('Introduzca el contacto (Enter para terminar) ')
        if nombre == '':
            break
        if buscar_contacto(nombre) == True:
            continue
        
        contacto = {}
        contacto['nombre'] = nombre
        
        email = input('Introduzca el email de '+nombre+' (Enter para omitir) ')
        if email != '':
            contacto['email'] = email

        telefono = input('Introduzca el telefono de '+nombre+' (Enter para omitir) ')
        if telefono != '':
            contacto['telefono'] = telefono
            
        edad_cadena = input('Introduzca la edad de '+nombre+' (Enter para omitir) ')
        if edad_cadena != '':
            contacto['edad'] = int(edad_cadena)
        
        lista_contactos.append(contacto)
        print('Añadido contacto '+nombre)
        mostrar_contacto(contacto)
        print('-------------')

def mostrar_contacto(contacto):
    for clave,valor in contacto.items():
        print(clave,valor)
        
def listado_contacto():
    global lista_contactos
    print('Hay',len(lista_contactos),'contactos')
    print('------------------')
    for contacto in lista_contactos:
        mostrar_contacto(contacto)
        print('------------------')

def cargar_agenda():
    global fichero_datos
    if fichero_datos in os.listdir():
        f = open(fichero_datos,'rt',encoding='utf8')
        for linea in f.readlines():
            contacto = json.loads(linea)
            lista_contactos.append(contacto)
        f.close()
        print('Se han recuperado',len(lista_contactos),'contactos')
    else:
        print('No se ha encontrado el fichero', fichero_datos)

def guardar_agenda():
    global fichero_datos
    try:
        f = open(fichero_datos,'wt',encoding='utf8')
        for contacto in lista_contactos:
            linea = json.dumps(contacto)+'\n'
            f.write(linea)
        f.close()
        print('Guardados '+str(len(lista_contactos))+' contactos')
    except Exception as e:
        print('ERROR: no se ha podido guardar el fichero',e)
        
def copia_seguridad():
    global fichero_datos
    f_zip = zipfile.ZipFile('agenda.zip','w')
    f_zip.write(fichero_datos)
    f_zip.close()
    
    