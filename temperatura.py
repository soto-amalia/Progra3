def cel_a_fare(celsius):
    farenheit=(celsius*9/5)+32
    return farenheit

def fare_a_cel(farenheit):
    return (farenheit-32)*5/9

def menu():
    print("\n Convertidor de temperatura\n ")
    print("1. Convertir de Celcius a Farenheit ")
    print("2. COnvertir de Farenheit a Celcius ")
    print("Salir")

def main():
    while True: 
        menu()
        seleccion= input("Selecciona una opción del 1 al 3: ")
        if seleccion==("1"):
            celsius=float(input("\nDame la temperatura    "))
            print(f"La temperatura es {cel_a_fare(celsius)} Fareheit")
        elif seleccion==("2"):
            farenheit=float(input("\nDame la temperatura   "))
            print(f"La temperatura es {fare_a_cel(farenheit)} Celsius")
        elif seleccion==("3"):
            print("Se termino el programa ")
            break
        else:
            print("Opción invalida")

main()