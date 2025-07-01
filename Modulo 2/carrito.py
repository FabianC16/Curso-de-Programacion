cesta = []

precios = {}

while True:
    print("\n--- MENU ---")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar el contenido de la cesta de la compra")
    print("3. Eliminar un elemento")
    print("4. Calcular el total")
    print("5. Renunciar (salir)")

    opcion = input("Elige una opcion (1-5): ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: $"))
        cesta.append(nombre)
        precios[nombre] = precio
        print(f"{nombre} agregado a la cesta.")

    elif opcion == "2":
        if cesta:
            print("Cesta de la compra:")
            for item in cesta:
                print(f"- {item} (${precios[item]:.2f})")
        else:
            print("La cesta está vacía.")

    elif opcion == "3":
        nombre = input("Nombre del producto a eliminar: ")
        if nombre in cesta:
            cesta.remove(nombre)
            precios.pop(nombre, None)
            print(f"{nombre} eliminado de la cesta.")
        else:
            print("Ese producto no está en la cesta.")

    elif opcion == "4":
        total = sum(precios[item] for item in cesta)
        print(f"Total a pagar: ${total:.2f}")

    elif opcion == "5":
        print("Gracias por usar la cesta de compra. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
