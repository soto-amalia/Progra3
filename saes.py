alumno={
    "nombre":"Michael",#pares ordenados de informacion=diccionario
    "apellido":"Jackson",
    "edad":"46",
    "genero":"F",
    "direccion":"Ever green stret N. 7",
    "correo":"michael_jackson@gmail.com",
    "ocupacion":"Rey del pop"
}

def registrar_alumno():#def declara una funcion
    alumno={
    "nombre":input("Ingresa tu nombre:"),
    "apellido":input("Ingresa tu apelligo:"),
    "edad":input("Ingresa tu edad:"),
    "genero":input("Ingresa tu genero:"),
    "direccion":input("Ingresa tu direccion"),
    "correo":input("Ingresa tu correo:"),
    "ocupacion":input("Ingresa tu ocupacion:"),
}
registrar_alumno()

print("El perfil del alumno: ")
for clave, valor in alumno.items(): #.items se usa pra recorrer el diccionario
    print(f"{clave.capitalize()} es : {valor}")