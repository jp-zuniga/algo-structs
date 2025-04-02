"""
Crear un programa que simule la gestión de un inventario en una tienda.
Utilizar un menú para agregar, eliminar, modificar y consultar productos
en el inventario. Cada producto tendrá un código, nombre, cantidad y precio.
"""

from os import system  # para limpiar la pantalla
from typing import Optional


class Producto:
    """
    Clase de datos para representar un producto con:
    - un código,
    - un nombre,
    - una cantidad,
    - un precio
    """

    def __init__(
        self,
        codigo: int = 0,
        nombre: str = "",
        cantidad: int = 0,
        precio: float = 0.0
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


def pedir_codigo(accion: str) -> int:
    """
    Pide el código del producto a mostrar/modificar/eliminar.
    """

    try:
        codigo = int(input(f"\nIngrese el código del producto que desea {accion}: "))
        if codigo < 0:
            raise ValueError

    except (TypeError, ValueError):
        input("¡El código debe ser un número entero positivo!")
        return pedir_codigo(accion)  # volver a pedir input

    return codigo


def buscar_producto(codigo: int, inventario: list[Producto]) -> Optional[Producto]:
    """
    Busca el índice del producto con el código indicado
    en el inventario de productos registrados.
    Retorna -1 si el producto no existe.
    """

    for producto in inventario:
        if producto.codigo == codigo:
            return producto

    return None


def agregar_producto(inventario: list[Producto]) -> None:
    """
    Pide los datos de un producto nuevo y lo agrega al inventario.
    """

    print("\nAgregar Producto Nuevo:")
    print("-----------------------------------------------------")

    print("\nIngrese los datos del producto:")
    try:
        codigo = int(input("Código: "))
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio (en C$): "))

        if codigo < 0 or cantidad < 0 or precio <= 0:
            raise ValueError

    except (TypeError, ValueError):
        input(
            "\n¡El código y la cantidad del producto deben ser números enteros"
            + " positivos, y el precio debe ser un número real positivo!"
        )

        system("cls || clear")
        return agregar_producto(inventario)  # volver a pedir input

    inventario.append(Producto(codigo, nombre, cantidad, precio))
    input("\n¡Producto agregado exitosamente!")
    return None


def consultar_producto(codigo: int, inventario: list[Producto]) -> None:
    """
    Busca un producto específico en el inventario y muestra sus datos.
    """

    producto = buscar_producto(codigo, inventario)
    if producto is None:
        input(f"\n¡No existe un producto con el código '{codigo}'!")
        return

    print(f"\nProducto #{producto.codigo}:")
    print("---------------------------------------------")
    print(f"Nombre: {producto.nombre}")
    print(f"Cantidad: {producto.cantidad}")
    print(f"Precio: {producto.precio}")
    print("---------------------------------------------")


def mostrar_productos(inventario: list[Producto]) -> None:
    """
    Llama consultar_producto() para todos los productos registrados.
    """

    print("\nProductos Registrados:")
    print("-----------------------------------------------------")

    for producto in inventario:
        consultar_producto(producto.codigo, inventario)

    input("\nPresione 'Enter' para regresar al menú principal...")


def modificar_producto(codigo: int, inventario: list[Producto]) -> None:
    """
    Permite al usuario ingresar los datos de un producto de nuevo
    para modificarlos (excepto el código, ya que se utiliza
    para identicar los productos).
    """

    producto_modificado = buscar_producto(codigo, inventario)
    if producto_modificado is None:
        input(f"\n¡No existe un producto con el código '{codigo}'!")
        return None

    print("\nModificar Producto:")
    print("-----------------------------------------------------")

    consultar_producto(codigo, inventario)
    print()

    # eliminar el producto original para sobreescribirlo
    inventario.remove(producto_modificado)

    # pedir nuevos datos
    print("Ingrese los nuevos datos del producto (dejar en blanco para no modificar):")
    nuevo_nombre = input("Nombre: ")
    nueva_cantidad = input("Cantidad: ")
    nuevo_precio = input("Precio: ")

    # los strings vacios se evaluan como False,
    # entonces si el usuario decide no modificar un atributo,
    # el valor del objeto original permanecera igual

    if nuevo_nombre:
        producto_modificado.nombre = nuevo_nombre

    try:
        if nueva_cantidad:
            producto_modificado.cantidad = int(nueva_cantidad)
        if nuevo_precio:
            producto_modificado.precio = float(nuevo_precio)

        if producto_modificado.cantidad < 0 or producto_modificado.precio <= 0:
            raise ValueError

    except (TypeError, ValueError):
        input(
            "\n¡El código y la cantidad del producto deben ser números enteros"
            + " positivos, y el precio debe ser un número real positivo!"
        )

        system("cls || clear")
        return modificar_producto(codigo, inventario)

    inventario.append(producto_modificado)
    input(
        f"\n¡Datos del producto #{producto_modificado.codigo}"
        + " fueron actualizados exitosamente!"
    )

    return None


def eliminar_producto(codigo: int, inventario: list[Producto]) -> None:
    """
    Encuentra el índice del producto a eliminar, y lo
    quita del inventario de productos.
    """

    producto = buscar_producto(codigo, inventario)
    if producto is None:
        input(f"\n¡No existe un producto con el código '{codigo}'!")
        return

    print("\nEliminar Producto:")
    print("-----------------------------------------------------")

    consultar_producto(codigo, inventario)
    print()

    confirmacion = input(
        "\n¿Está seguro que desea eliminar el producto seleccionado? (s/n) "
    ).lower()

    if confirmacion == "s":
        inventario.remove(producto)
        input(f"\n¡Producto #{producto.codigo} eliminado exitosamente!")
    elif confirmacion == "n":
        input("\n¡De acuerdo! Regresando al menú principal...")
    else:
        input("\n¡Respuesta inválida! Regresando al menú principal...")


def menu_principal(inventario: list[Producto]) -> None:
    """
    Loop principal del programa que le muestra un menú de opciones al usuario.
    """

    opcion = ""
    while opcion != "6":
        system("cls || clear")
        print("\nGestión de Inventario")
        print("-----------------------------------------------------\n")
        print("1. Agregar producto")
        print("2. Consultar un producto específico")
        print("3. Mostrar todos productos registrados")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("\n-> ")

        match opcion:
            case "1":
                system("cls || clear")
                agregar_producto(inventario)
            case "2":
                codigo = pedir_codigo("consultar")
                system("cls || clear")
                consultar_producto(codigo, inventario)
                input("\nPresione 'Enter' para regresar al menú principal...")
            case "3":
                system("cls || clear")
                mostrar_productos(inventario)
            case "4":
                codigo = pedir_codigo("modificar")
                system("cls || clear")
                modificar_producto(codigo, inventario)
            case "5":
                codigo = pedir_codigo("eliminar")
                system("cls || clear")
                eliminar_producto(codigo, inventario)
            case "6":
                print("\nSaliendo del programa...\n")
            case _:
                input("\n¡Opción inválida, intente nuevamente!")
        inventario.sort(key=lambda p: p.codigo)


def main() -> None:
    """
    Ejecución del programa.
    """

    inventario: list[Producto] = []
    menu_principal(inventario)


if __name__ == "__main__":
    main()
