#Eres una billetera del metro,el bolero vale 5 pesos,Pero si eres menor de edad cuesta 4
#Y si tienesaineres mayor d3 65 años tienes que cobrar 2 pesos, Solo le preguntas a la gente su edad
""""
age=0
tickets_mars=0
age=int(input("Ingresa la edad de la persona que va a comprar un ticket: "))
if 0<age<19:
    tickets_mars =4
elif age>65:
    tickets_mars=2
else:
    tickets_mars=5
print("El costo del boleto es:"+str(tickets_mars))


#La persona da ua edad y dependiendo la edad de de da un boleto diferente 

#Escribe un programa que pida dos números y muestre cuál es el mayor. Si son iguales, indícalo.
number1=int(input("Ingresa un numero: "))
number2=int(input("Ingresa otro numero: "))
if number1==number2:
    print(f"Ambos numeros son iguales: {number1 }es igual que {number2}")
elif number1>number2:
    print("EL primer numero es mayor que el segundo")
else:
    print(f"El segundo numero es mayor al primero")


# Crear un programa que calcule un impuesto, pides la cantidad, y se cobra de 1 a 100 mil el 5%
# de 100 mil a 600 mil el 12% y de 600 mil en adelante el 20%, de manera escalonada

salario=int(input("¿Cuánto ganas?"))
pago=0
if salario>600000:
    pago+=(salario-600000)*.20 # mas igual(+=) hace la operacion y guarda el resultado en la misma variable
    salario=600000
    print(f"Tu pago de impuestos es {pago}")

if salario>100000:
    pago+=(salario-100000)*.125
    salario=100000
    print(f"Tu pago de impuestos es {pago}")

if 0 <salario<=100000:
    pago+=(salario)*.05
print(f"Tu pago de impuestos es {pago}")

print(f"Tu pago de impuestos total es {pago}")
"""""

#Determina el tipo de triángulo (equilátero, isósceles o escaleno) basado en las longitudes de sus lados.
lado1=30
lado2=30
lado3=30
def tipo_triangulo(a, b, c):
    # Verificar si es un triángulo válido
    if a + b > c and a + c > b and b + c > a: #desigualdad triangular
        if a==b==c:
            return "Es Equilatero"
        elif a==b or a==c or b==c:
            return "Es Isosceles"
        else:
            return "Es escaleno"

    else:
        return "No es un triangulo valido"
print(tipo_triangulo(40, lado2, 50))

