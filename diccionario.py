#Un diccionario es una lista de pares 
personas={"Ana":25}#los pares son divididos por : a la izquierda la llave entre ""
personas2={"Ana":25,"Luis":30,"Martha":50}#Las claves son unicas y no se pueden repetir
#Para acceder al valor llamamos la clave 
print(personas2["Luis"])
#La MANERA MAS FACIL DE RECORRER UN DICCIONARIO ES USANDO UN FOR IN
#Si no espesificas imprime la clave 
for clave in personas2:
    print(clave)

for valores in personas2.values():#Para imprimir los valore sutilizas .values()
    print(valores)
#Para usar ambos al mismo tiempo se recomiend ausar .items()
for clave,valores in personas2.items():
    print(f"La clave es: {clave},y el valor es: {valores}")
    
