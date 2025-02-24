alumno={
    "nombre":"Michael",#pares ordenados de informacion=diccionario
    "apellido":"Jackson",
    "edad":"46",
    "genero":"F",
    "direccion":"Ever green stret N. 7",
    "correo":"michael_jackson@gmail.com",
    "ocupacion":"Rey del pop"
}


def obtener_edad():
    while True:#hasta que te de una entrada valida
        edad=input("Ingresa tu edad:")
        if edad.isdigit():
            return int(edad)#inte es una funcion que convierte strings a enteros
        else:
            print("La edad debe de ser un numero")


def registrar_alumno():#def declara una funcion
    alumno_variableLocal={
    "nombre":input("Ingresa tu nombre:"),
    "apellido":input("Ingresa tu apellido:"),
    "edad":obtener_edad(),
    "genero":input("Ingresa tu genero:"),
    "direccion":input("Ingresa tu direccion"),
    "correo":input("Ingresa tu correo:"),
    "ocupacion":input("Ingresa tu ocupacion:"),
    }
    return alumno_variableLocal #Aqui retornamos el diccionario llenado


alumno = registrar_alumno()

print("El perfil del alumno: ")
for clave, valor in alumno.items(): #.items se usa pra recorrer el diccionario
    print(f"{clave.capitalize()} es : {valor}")