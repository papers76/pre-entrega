

# Pre-entrega - Sistema de gestion de productos

productos = []  # Cada producto se guarda como: [nombre, categoria, precio]

while True:
    print("\n--- SISTEMA DE GESTION BASICA DE PRODUCTOS ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elegi una opcion: ").strip()

    if opcion == "1":
        print("\n--- Agregar producto ---")

        nombre = ""

        while nombre == "":
            nombre = input("Ingresa el nombre: ").strip()

            if nombre == "":
                print("El nombre no puede estar vacio.")

        categoria = ""

        while categoria == "":
            categoria = input("Ingresa la categoria: ").strip()

            if categoria == "":
                print("La categoria no puede estar vacia.")

        precio = 0

        while precio <= 0:
            precio_ingresado = input("Ingresa el precio sin centavos: ").strip()

            if precio_ingresado.isdigit():
                precio = int(precio_ingresado)

                if precio <= 0:
                    print("El precio debe ser mayor a cero.")
            else:
                print("El precio debe ser un numero entero valido.")

        producto = [nombre.title(), categoria.title(), precio]
        productos.append(producto)

        print("Producto agregado correctamente.")

    elif opcion == "2":
        print("\n--- Productos registrados ---")

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            numero = 1

            for producto in productos:
                print(f"{numero}. {producto[0]} | {producto[1]} | ${producto[2]}")
                numero += 1

    elif opcion == "3":
        print("\n--- Buscar producto ---")

        if len(productos) == 0:
            print("No hay productos registrados para buscar.")
        else:
            busqueda = input("Ingresa el nombre a buscar: ").strip().lower()

            if busqueda == "":
                print("Debes ingresar un nombre para buscar.")
            else:
                encontrado = False
                numero = 1

                for producto in productos:
                    if busqueda in producto[0].lower():
                        print(f"{numero}. {producto[0]} | {producto[1]} | ${producto[2]}")
                        encontrado = True

                    numero += 1

                if encontrado == False:
                    print("No se encontraron resultados.")

    elif opcion == "4":
        print("\n--- Eliminar producto ---")

        if len(productos) == 0:
            print("No hay productos registrados para eliminar.")
        else:
            numero = 1

            for producto in productos:
                print(f"{numero}. {producto[0]} | {producto[1]} | ${producto[2]}")
                numero += 1

            posicion = input("Ingresa el numero del producto a eliminar: ").strip()

            if posicion.isdigit():
                posicion = int(posicion)

                if posicion >= 1 and posicion <= len(productos):
                    producto_eliminado = productos.pop(posicion - 1)

                    print(f"Producto '{producto_eliminado[0]}' eliminado correctamente.")
                else:
                    print("El numero no corresponde a un producto registrado.")
            else:
                print("Debes ingresar un numero valido.")

    elif opcion == "5":
        print("\nGracias por utilizar el sistema.")
        break

    else:
        print("Opcion invalida. Elegi una opcion del 1 al 5.")