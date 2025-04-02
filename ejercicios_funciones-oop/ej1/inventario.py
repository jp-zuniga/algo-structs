"""
Definición de la clase Inventario.
"""

from os import system
from typing import Optional

from .producto import Producto


class Inventario:
    """
    Representa el inventario de productos de un negocio.
    """

    def __init__(self, lista_productos: Optional[list[Producto]] = None) -> None:
        if lista_productos is None:
            self.productos = []
        else:
            self.productos = lista_productos


    def _pedir_codigo(self, accion: str) -> int:
        """
        Pide el código del producto a mostrar/modificar/eliminar.
        """

        try:
            codigo = int(
                input(f"\nIngrese el código del producto que desea {accion}: ")
            )

            if codigo < 0:
                raise ValueError

        except (TypeError, ValueError):
            input("¡El código debe ser un número entero positivo!")
            return self._pedir_codigo(accion)  # volver a pedir input

        return codigo


    def _buscar_producto(self, codigo: int) -> Optional[Producto]:
        """
        Busca el índice del producto con el código indicado
        en self.productos. Retorna -1 si el producto no existe.
        """

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None


    def agregar_producto(self) -> None:
        """
        Pide los datos de un producto nuevo y lo agrega a self.productos.
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
            if self._buscar_producto(codigo) is not None:
                raise NameError

        except (TypeError, ValueError):
            input(
                "\n¡El código y la cantidad del producto deben ser números enteros"
                + " positivos, y el precio debe ser un número real positivo!"
            )

            system("cls || clear")
            return self.agregar_producto()  # volver a pedir input

        except NameError:
            input("\n¡El código ingresado ya existe en el registro de productos!")
            system("cls || clear")
            return self.agregar_producto()  # volver a pedir input


        self.productos.append(Producto(codigo, nombre, cantidad, precio))
        input("\n¡Producto agregado exitosamente!")
        return None


    def consultar_producto(self, codigo: Optional[int] = None) -> None:
        """
        Busca un producto específico en self.productos y muestra sus datos.
        """

        cd = codigo if codigo is not None else self._pedir_codigo("consultar")
        producto = self._buscar_producto(cd)

        if producto is None:
            input(f"\n¡No existe un producto con el código '{cd}'!")
            return

        print(f"\nProducto #{producto.codigo}:")
        print("---------------------------------------------")
        print(f"Nombre: {producto.nombre}")
        print(f"Cantidad: {producto.cantidad}")
        print(f"Precio: {producto.precio}")
        print("---------------------------------------------")


    def mostrar_productos(self) -> None:
        """
        Llama consultar_producto() para todos los productos registrados.
        """

        print("\nProductos Registrados:")
        print("-----------------------------------------------------")

        for producto in self.productos:
            self.consultar_producto(producto.codigo)

        input("\nPresione 'Enter' para regresar al menú principal...")


    def modificar_producto(self) -> None:
        """
        Permite al usuario ingresar los datos de un producto de nuevo para modificarlos
        (excepto el código, ya que se utiliza para identicar los productos).
        """

        codigo = self._pedir_codigo("modificar")
        producto_modificado = self._buscar_producto(codigo)

        if producto_modificado is None:
            input(f"\n¡No existe un producto con el código '{codigo}'!")
            return None

        print("\nModificar Producto:")
        print("-----------------------------------------------------")

        self.consultar_producto(codigo)
        print()

        # eliminar el producto original para sobreescribirlo
        self.productos.remove(producto_modificado)

        # pedir nuevos datos
        print(
            "Ingrese los nuevos datos del producto (dejar en blanco para no modificar):"
        )

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
            return self.modificar_producto()

        self.productos.append(producto_modificado)
        input(
            f"\n¡Datos del producto #{producto_modificado.codigo}"
            + " fueron actualizados exitosamente!"
        )

        return None

    def eliminar_producto(self) -> None:
        """
        Encuentra el índice del producto a eliminar, y lo quita de self.productos.
        """

        codigo = self._pedir_codigo("eliminar")
        producto = self._buscar_producto(codigo)

        if producto is None:
            input(f"\n¡No existe un producto con el código '{codigo}'!")
            return

        print("\nEliminar Producto:")
        print("-----------------------------------------------------")

        self.consultar_producto(codigo)
        print()

        confirmacion = input(
            "\n¿Está seguro que desea eliminar el producto seleccionado? (s/n) "
        ).lower()

        if confirmacion == "s":
            self.productos.remove(producto)
            input(f"\n¡Producto #{producto.codigo} eliminado exitosamente!")
        elif confirmacion == "n":
            input("\n¡De acuerdo! Regresando al menú principal...")
        else:
            input("\n¡Respuesta inválida! Regresando al menú principal...")
