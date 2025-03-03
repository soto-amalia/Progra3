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

def registrar_alumno():#def declara una funcion
    alumno_variableLocal={
    "nombre":input("Ingresa tu nombre:"),
    "apellido":input("Ingresa tu apellido:"),
    "edad":obtener_edad(),
    "genero":obtener_genero(),
    "direccion":input("Ingresa tu direccion"),
    "correo":input("Ingresa tu correo:"),
    "ocupacion":input("Ingresa tu ocupacion:"),
    }
    return alumno_variableLocal #Aqui retornamos el diccionario llenado

def guardar_json(alumno_a_guardar): #open solo permite leer, escribir o modificar archivos 
    #Para manejar archivos, rutas, directorios, copiar y pegar arvichos se usa "os"
    try:#Intenta hacer esto si no funciona vete al escept
        with open("lista.json","a") as archivo:# "a" añade a los archivos, w escribe y sobrescribe, r sólo lee
            json.dump(alumno_a_guardar,archivo)#json.dump mete informacion de json en forma de objeto
            print("Se guardo en un archivo")

    except Exception as error:#SIrve para cachar errores de lo que este dentro del try 
        print(f"Error del sistema: {error}")

def mostrar_alumno(alumno):
    print("El perfil del alumno: ")
    for clave, valor in alumno.items(): #.items se usa pra recorrer el diccionario
        print(f"{clave.capitalize()} es : {valor}")
        print("-------------------")

def mostrar_alumnos():#dentro de la funcion vamos a leer el archivo
    try:#Intenta hacer esto si no funciona vete al escept
        print("Aqui empieza la funcion mostrar alumnos")
        with open("lista.json","r") as archivo:#  r sólo lee
            alumnos=archivo.readlines()##lee lineas de un archivo y convertirlas a un diccionario de python
            print("Estos son los alumnos:")

            for alumno_json in alumnos:
                alumno=json.loads(alumno_json)
                mostrar_alumno(alumno)
                

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
#1 implementar mostrar todos los alumnos leyendo desde el archivo
#2Validar todas las entradas, con una funcion y que no esten vacias
#3.BUscar alumnos por nombre en el archivo
#Borrar alumnos
#Hacer una copia o exportar el json 
#a cada alumno hacerle su propio json
