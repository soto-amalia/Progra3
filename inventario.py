#Un diccionario es una estructura de datos que usa pares de llave y valor
#
productos = {
    101: {"producto": "Laptop", "precio": 800, "marca": "Lenovo"},
    102: {"producto": "Teléfono", "precio": 500, "marca": "Samsung"},
    103: {"producto": "Tablet", "precio": 300, "marca": "Apple"},
    104: {"producto": "Monitor", "precio": 250, "marca": "HP"},
    105: {"producto": "Teclado", "precio": 50, "marca": "Lenovo"},
    106: {"producto": "Mouse", "precio": 30, "marca": "Lenovo"},
    107: {"producto": "Impresora", "precio": 200, "marca": "HP"},
    108: {"producto": "Router", "precio": 120, "marca": "Samsung"},
    109: {"producto": "Auriculares", "precio": 80, "marca": "Apple"},
    110: {"producto": "Webcam", "precio": 90, "marca": "HP"},
    111: {"producto": "Disco Duro", "precio": 100, "marca": "Lenovo"},
    112: {"producto": "SSD", "precio": 150, "marca": "Samsung"},
    113: {"producto": "Placa Madre", "precio": 180, "marca": "ASUS"},
    114: {"producto": "Memoria RAM", "precio": 75, "marca": "ASUS"},
    115: {"producto": "Fuente de Poder", "precio": 110, "marca": "ASUS"},
    116: {"producto": "Tarjeta Gráfica", "precio": 600, "marca": "ASUS"},
    117: {"producto": "Microprocesador", "precio": 320, "marca": "HP"},
    118: {"producto": "Consola", "precio": 450, "marca": "Samsung"},
    119: {"producto": "Smartwatch", "precio": 220, "marca": "Apple"},
    120: {"producto": "Proyector", "precio": 350, "marca": "HP"},
}
ventas = [
    {"id_producto": 101, "tienda": "Tienda A", "cantidad": 5},
    {"id_producto": 102, "tienda": "Tienda B", "cantidad": 3},
    {"id_producto": 103, "tienda": "Tienda C", "cantidad": 4},
    {"id_producto": 104, "tienda": "Tienda A", "cantidad": 2},
    {"id_producto": 105, "tienda": "Tienda B", "cantidad": 6},
    {"id_producto": 106, "tienda": "Tienda C", "cantidad": 1},
    {"id_producto": 107, "tienda": "Tienda A", "cantidad": 3},
    {"id_producto": 108, "tienda": "Tienda B", "cantidad": 2},
    {"id_producto": 109, "tienda": "Tienda A", "cantidad": 4},
    {"id_producto": 110, "tienda": "Tienda C", "cantidad": 1},
    {"id_producto": 111, "tienda": "Tienda B", "cantidad": 5},
    {"id_producto": 112, "tienda": "Tienda A", "cantidad": 2},
    {"id_producto": 113, "tienda": "Tienda C", "cantidad": 3},
    {"id_producto": 114, "tienda": "Tienda A", "cantidad": 2},
    {"id_producto": 115, "tienda": "Tienda B", "cantidad": 1},
    {"id_producto": 116, "tienda": "Tienda C", "cantidad": 2},
    {"id_producto": 117, "tienda": "Tienda A", "cantidad": 2},
    {"id_producto": 118, "tienda": "Tienda B", "cantidad": 1},
    {"id_producto": 119, "tienda": "Tienda C", "cantidad": 2},
    {"id_producto": 120, "tienda": "Tienda A", "cantidad": 1},
]

def calcular_iva(precio, cantidad):
    iva=.16
    total=precio*cantidad
    total_iva =total*(1+iva)
    return total_iva

""""productos_iva=calcular_iva(500,3)
print(productos_iva)
"""

def ventas_totales(productos,ventas):
    for venta in ventas:
        id_producto=venta["id_producto"]
        cantidad=venta["cantidad"]
        producto=productos[id_producto]
        precio=producto["precio"]
        total=calcular_iva(precio,cantidad)
        print(f"EL producto {producto['producto']} se vendio por un total de: {total:.2f}")
ventas_totales(productos,ventas)