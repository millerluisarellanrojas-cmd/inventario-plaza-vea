# SISTEMA DE GESTIÓN DE CATÁLOGO E INVENTARIO

ARCHIVO = "inventario.txt"
ADMIN_USUARIO = "admin"
ADMIN_CLAVE = "1234"

# ALMACEN DE PRODUCTOS
codigos = []
productos = []
stocks = []
precios = []

def cargar_productos():
    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
        for linea in archivo:
            linea = linea.strip()
            if linea != "":
                datos = linea.split(",")
                if len(datos) == 4:
                    codigo = datos[0]
                    producto = datos[1]
                    try:
                        stock = int(datos[2])
                        precio = float(datos[3])
                        codigos.append(codigo)
                        productos.append(producto)
                        stocks.append(stock)
                        precios.append(precio)
                    except ValueError:
                        print("Se encontró un registro inválido en el archivo.")
        archivo.close()
        print("\nInventario cargado correctamente.")
    except FileNotFoundError:
        print("\nNo existe todavía el archivo de inventario.")
        print("Se iniciará con un catálogo vacío.")

def guardar_productos():
    try:
        archivo = open(ARCHIVO, "w", encoding="utf-8")
        for i in range(len(codigos)):
            linea = (
                codigos[i]
                + ","
                + productos[i]
                + ","
                + str(stocks[i])
                + ","
                + str(precios[i])
                + "\n"
            )
            archivo.write(linea)
        archivo.close()
        print("\nCambios guardados correctamente en", ARCHIVO)
    except:
        print("\nOcurrió un error al guardar el archivo.")

def mostrar_productos():
    print("\n==============================================================")
    print("                     CATÁLOGO DE PRODUCTOS")
    print("==============================================================")
    if len(codigos) == 0:
        print("No existen productos registrados.")
    else:
        print(
            f"{'CÓDIGO':<12}"
            f"{'PRODUCTO':<25}"
            f"{'STOCK':<12}"
            f"{'PRECIO':<12}"
        )
        print("--------------------------------------------------------------")
        for i in range(len(codigos)):
            print(
                f"{codigos[i]:<12}"
                f"{productos[i]:<25}"
                f"{stocks[i]:<12}"
                f"S/ {precios[i]:.2f}"
            )
    print("==============================================================")

def buscar_indice_producto(codigo):
    for i in range(len(codigos)):
        if codigos[i].upper() == codigo.upper():
            return i
    return -1

def registrar_producto():
    print("\n================ REGISTRAR PRODUCTO ================")
    codigo = input("Ingrese código del producto: ").strip().upper()
    if codigo == "":
        print("El código no puede estar vacío.")
        return
    indice = buscar_indice_producto(codigo)
    if indice != -1:
        print("Ya existe un producto con ese código.")
        return
    descripcion = input("Ingrese descripción del producto: ").strip()
    if descripcion == "":
        print("La descripción no puede estar vacía.")
        return
    while True:
        try:
            stock = int(input("Ingrese cantidad disponible: "))
            if stock < 0:
                print("El stock no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Debe ingresar un número entero.")
    while True:
        try:
            precio = float(input("Ingrese precio de venta: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
            else:
                break
        except ValueError:
            print("Debe ingresar un número válido.")
    codigos.append(codigo)
    productos.append(descripcion)
    stocks.append(stock)
    precios.append(precio)
    print("\nProducto registrado correctamente.")
    print("IMPORTANTE:")
    print("El producto está guardado temporalmente en memoria.")
    print("Use la opción GUARDAR para escribirlo en el archivo.")

def registrar_venta():
    print("\n================ REGISTRAR VENTA ================")
    if len(codigos) == 0:
        print("No existen productos registrados.")
        return
    codigo = input("Ingrese el código del producto vendido: ").strip().upper()
    indice = buscar_indice_producto(codigo)
    if indice == -1:
        print("Producto no encontrado.")
        return
    print("\nProducto encontrado:")
    print("Producto:", productos[indice])
    print("Stock actual:", stocks[indice])
    print("Precio unitario: S/", format(precios[indice], ".2f"))
    while True:
        try:
            cantidad_vendida = int(
                input("\nIngrese cantidad vendida: ")
            )
            if cantidad_vendida <= 0:
                print("La cantidad debe ser mayor que cero.")
            elif cantidad_vendida > stocks[indice]:
                print("\nStock insuficiente.")
                print("Stock disponible:", stocks[indice])
            else:
                break
        except ValueError:
            print("Ingrese una cantidad válida.")
    stock_anterior = stocks[indice]
    nuevo_stock = stock_anterior - cantidad_vendida
    stocks[indice] = nuevo_stock
    total_venta = cantidad_vendida * precios[indice]
    print("\n================ RESULTADO DE LA VENTA ================")
    print("Producto:", productos[indice])
    print("Stock anterior:", stock_anterior)
    print("Cantidad vendida:", cantidad_vendida)
    print("Nuevo stock:", stocks[indice])
    print("Precio unitario: S/", format(precios[indice], ".2f"))
    print("Total de venta: S/", format(total_venta, ".2f"))
    print("========================================================")
    print("\nEl stock fue actualizado solamente en memoria.")
    print("Debe guardar los cambios para actualizar el archivo TXT.")

def buscar_producto():
    print("\n================ BUSCAR PRODUCTO ================")
    codigo = input("Ingrese código del producto: ").strip().upper()
    indice = buscar_indice_producto(codigo)
    if indice == -1:
        print("Producto no encontrado.")
    else:
        print("\nProducto encontrado:")
        print("---------------------------------------")
        print("Código:", codigos[indice])
        print("Descripción:", productos[indice])
        print("Stock disponible:", stocks[indice])
        print("Precio: S/", format(precios[indice], ".2f"))
        print("---------------------------------------")

def actualizar_producto():
    print("\n================ ACTUALIZAR PRODUCTO ================")
    codigo = input("Ingrese código del producto: ").strip().upper()
    indice = buscar_indice_producto(codigo)
    if indice == -1:
        print("Producto no encontrado.")
        return
    print("\nDatos actuales:")
    print("Código:", codigos[indice])
    print("Producto:", productos[indice])
    print("Stock:", stocks[indice])
    print("Precio: S/", format(precios[indice], ".2f"))
    print("\n¿Qué desea actualizar?")
    print("1. Descripción")
    print("2. Stock")
    print("3. Precio")
    print("4. Cancelar")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nueva_descripcion = input(
            "Ingrese nueva descripción: "
        ).strip()
        if nueva_descripcion == "":
            print("La descripción no puede estar vacía.")
        else:
            productos[indice] = nueva_descripcion
            print("Descripción actualizada.")
    elif opcion == "2":
        while True:
            try:
                nuevo_stock = int(
                    input("Ingrese nuevo stock: ")
                )
                if nuevo_stock < 0:
                    print("El stock no puede ser negativo.")
                else:
                    stocks[indice] = nuevo_stock
                    print("Stock actualizado.")
                    break
            except ValueError:
                print("Debe ingresar un número entero.")
    elif opcion == "3":
        while True:
            try:
                nuevo_precio = float(
                    input("Ingrese nuevo precio: ")
                )
                if nuevo_precio <= 0:
                    print("El precio debe ser mayor que cero.")
                else:
                    precios[indice] = nuevo_precio
                    print("Precio actualizado.")
                    break
            except ValueError:
                print("Debe ingresar un número válido.")
    elif opcion == "4":
        print("Actualización cancelada.")
    else:
        print("Opción inválida.")
    print("\nRecuerde guardar los cambios.")

def autenticar_administrador():
    print("\n===============================================")
    print("        SISTEMA DE CATÁLOGO E INVENTARIO")
    print("===============================================")
    intentos = 0
    while intentos < 3:
        usuario = input("\nUsuario: ")
        clave = input("Contraseña: ")
        if usuario == ADMIN_USUARIO and clave == ADMIN_CLAVE:
            print("\nAcceso correcto.")
            return True
        else:
            intentos = intentos + 1
            print("\nUsuario o contraseña incorrectos.")
            print(
                "Intentos restantes:",
                3 - intentos
            )
    print("\nSe agotaron los intentos de acceso.")
    return False

def mostrar_menu():
    print("\n================================================")
    print("               MENÚ PRINCIPAL")
    print("================================================")
    print("1. Ver catálogo")
    print("2. Registrar producto")
    print("3. Registrar venta")
    print("4. Buscar producto")
    print("5. Actualizar producto")
    print("6. Guardar cambios")
    print("7. Salir")
    print("================================================")

def programa_principal():
    acceso = autenticar_administrador()
    if acceso == False:
        print("\nPrograma finalizado.")
        return
    cargar_productos()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            registrar_producto()
        elif opcion == "3":
            registrar_venta()
        elif opcion == "4":
            buscar_producto()
        elif opcion == "5":
            actualizar_producto()
        elif opcion == "6":
            guardar_productos()
        elif opcion == "7":
            print("\nGuardando los cambios antes de salir...")
            guardar_productos()
            print("\nPrograma finalizado correctamente.")
            break
        else:
            print("\nOpción inválida.")
            print("Seleccione una opción entre 1 y 7.")
programa_principal()