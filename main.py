productos = []
historial_acciones = []

def registrar_accion(accion):
    from datetime import datetime
    ahora = datetime.now().strftime("%H:%M:%S")
    historial_acciones.append(f"[{ahora}] {accion}")

def leer_float_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = float(entrada)
            if valor <= 0:
                print("El valor debe ser mayor que 0.")
            else:
                return valor
        except ValueError:
            print("Entrada no valida. Debes escribir un numero.")

def leer_int_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor <= 0:
                print("La cantidad debe ser mayor que 0.")
            else:
                return valor
        except ValueError:
            print("Entrada no valida. Debes escribir un numero entero.")

def agregar_producto(lista_productos):
    print("\n--- Agregar producto ---")
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    precio = leer_float_positivo("Precio del producto: ")
    cantidad = leer_int_positivo("Cantidad: ")
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "subtotal": precio * cantidad,
    }
    lista_productos.append(producto)
    registrar_accion(f"Agregado {nombre} (${precio} x {cantidad})")
    print(f"Producto '{nombre}' agregado correctamente.")

def mostrar_productos(lista_productos):
    print("\n--- Lista de productos ---")
    if not lista_productos:
        print("No hay productos registrados.")
        return
    for i, producto in enumerate(lista_productos, start=1):
        print(
            f"{i}. {producto['nombre']} | "
            f"Precio: ${producto['precio']:.2f} | "
            f"Cantidad: {producto['cantidad']} | "
            f"Subtotal: ${producto['subtotal']:.2f}"
        )

def calcular_total(lista_productos):
    print("\n--- Total de la compra ---")
    if not lista_productos:
        print("No hay productos para calcular.")
        return
    total = 0
    for producto in lista_productos:
        total += producto["subtotal"]
    print(f"El total de la compra es: ${total:.2f}")

def filtrar_productos_por_precio(lista_productos):
    print("\n--- Filtrar productos por precio ---")
    if not lista_productos:
        print("No hay productos registrados.")
        return
    precio_minimo = leer_float_positivo("Mostrar productos con precio mayor a: ")
    encontrados = []
    for producto in lista_productos:
        if producto["precio"] > precio_minimo:
            encontrados.append(producto)
    if not encontrados:
        print("No se encontraron productos que cumplan la condicion.")
        return
    print(f"Productos con precio mayor a ${precio_minimo:.2f}:")
    for i, producto in enumerate(encontrados, start=1):
        print(
            f"{i}. {producto['nombre']} | "
            f"Precio: ${producto['precio']:.2f} | "
            f"Cantidad: {producto['cantidad']}"
        )

def mostrar_menu():
    print("\n===== Sistema basico de gestion de compras =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Calcular total de la compra")
    print("4. Filtrar productos por precio")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            calcular_total(productos)
        elif opcion == "4":
            filtrar_productos_por_precio(productos)
        elif opcion == "5":
            print("Gracias por usar el sistema. Hasta luego.")
            break
        else:
            print("Opcion no valida. Intenta nuevamente.")

if _name_ == "_main_":
    main()