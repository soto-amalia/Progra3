import json

def obtener_edad():
    while True:#hasta que te de una entrada valida
        edad=input("Ingresa tu edad:")
        if edad.isdigit():
            return int(edad)#inte es una funcion que convierte strings a enteros
        else:
            print("La edad debe de ser un numero")

def obtener_genero():
    while True:
        genero=input("Ingresa tu genero Hombre o Mujer con H/M/NB").upper() #uper transforma el texto ingresado a mayusculas
        if genero in ["M","H","NB"]:#in checa que el objeto este dentro de la lista
            return genero
        else:
            print("Genero no valido")
def validar_entrada(mensaje):
    while True:
        escrito_del_usuario=input(mensaje)
        if escrito_del_usuario:#cuasiverdad o cuasifalso
            return escrito_del_usuario
        else:
            print("Este campo no puede estar vacío")

def registrar_alumno():#def declara una funcion
    alumno_variableLocal={
    "nombre":validar_entrada("Ingresa tu nombre:"),
    "apellido":validar_entrada("Ingresa tu apellido:"),
    "edad":obtener_edad(),
    "genero":obtener_genero(),
    "direccion":validar_entrada("Ingresa tu direccion"),
    "correo":input("Ingresa tu correo:"),
    "ocupacion":validar_entrada("Ingresa tu ocupacion:"),
    }
    return alumno_variableLocal #Aqui retornamos el diccionario llenado

def guardar_json(alumno_a_guardar): #open solo permite leer, escribir o modificar archivos 
    #Para manejar archivos, rutas, directorios, copiar y pegar arvichos se usa "os"
    try:#Intenta hacer esto si no funciona vete al escept
        try: #Intentar leer el archivo si existe y que sea un archivo de json
            with open("lista.json", "r") as archivo:
                alumnos = json.load(archivo)  # Cargar lista de alumnos existente
        except (FileNotFoundError, json.JSONDecodeError):
            alumnos = []  # Si el archivo no existe o está vacío, iniciar una lista vacía
        alumnos.append(alumno_a_guardar)  # Agregar el nuevo alumno a la lista
        with open("lista.json", "w") as archivo:  # Escribir toda la lista de nuevo
            #.domp()sirve para meter cosas a un archivo de json
            json.dump(alumnos, archivo, indent=4)  # Formato legible con indentación
        print("Se guardó en un archivo correctamente.")
    except Exception as error:#SIrve para cachar errores de lo que este dentro del try 
        print(f"Error del sistema: {error}")

def mostrar_alumno(alumno):
    print("El perfil del alumno: ")
    for clave, valor in alumno.items(): #.items se usa pra recorrer el diccionario
        print(f"{clave.capitalize()} es : {valor}")
        

def mostrar_alumnos():
    try:
        with open("lista.json", "r") as archivo:
            alumnos = json.load(archivo)  # Leer lista de alumnos
        print("Estos son los alumnos registrados:")
        for alumno in alumnos:
            print("-------------------")
            mostrar_alumno(alumno)
            print("-------------------")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay alumnos registrados aún.")
    except Exception as error:#SIrve para cachar errores de lo que este dentro del try 
        print(f"Error del sistema: {error}")


def menu():
    while True:

        print("Menu de opciones: ")
        print("1.Registrar al alumno")
        print("2.Mostrar alumnos")
        print("3.Salir")
        opcion=input("Elige una opcion")
        if opcion=="1":
            alumno_temporal=registrar_alumno()
            guardar_json(alumno_temporal)
        elif opcion=="2":
            mostrar_alumnos()
            print("Estos son los alumnos: ")
        elif opcion=="3":
            break ##Termina la funcion
        else:
            print("Opcion no valida")

menu()

#2Validar todas las entradas, con una funcion y que no esten vacias
#3.BUscar alumnos por nombre en el archivo
#Borrar alumnos
#Hacer una copia o exportar el json 
#a cada alumno hacerle su propio json

