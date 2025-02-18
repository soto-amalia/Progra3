nombre="Alex" 
edad= 32
altura=1.8
print("Tu nombre actual es: "+ nombre)

print("Dame tu uevo nombre : ")
#nombre=input("¿Cual es tu nombe? ")

print("Tu nombre actual es: "+ nombre)
#Tengo barcos que permiten subir a 50 personas y hay una inundación y quiero que me digas el numero de 
#personas que necesitan ser evacuadas y me diga cuantos barcos necesittas no lobran salvarse
capacidad_barco=556
capacidad_barco = int(input("Ingrese el número de personas a evacuar: "))
capacidad_salvavidas=50
botes_salvavidas=capacidad_barco//capacidad_salvavidas
moridos=capacidad_barco%capacidad_salvavidas
print(botes_salvavidas)
print("Y se murieron: "+ str(moridos))
 #de que tamaño es su barco y hacer el calculo
