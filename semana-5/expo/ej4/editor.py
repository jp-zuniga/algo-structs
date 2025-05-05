"""
Implementación de la clase principal de la aplicación.
"""

from .acciones_editor import (
    EscribirTexto,
    BorrarTexto,
    CopiarTexto,
    PegarTexto
)


class EditorTexto:
    """
    Clase principal que simula un editor de texto con historial de acciones.
    """

    def __init__(self):
        self.texto = ""
        self.posicion_cursor = 0
        self.portapapeles = ""
        self.historial = []  # Lista de acciones realizadas
        self.posicion_actual = -1  # Índice de la última acción ejecutada (-1 significa ninguna)

    def ejecutar_accion(self, accion):
        """
        Ejecuta una nueva acción y la añade al historial.
        """

        # Si hay acciones en el historial después de la posición actual, se eliminan
        if self.posicion_actual < len(self.historial) - 1:
            self.historial = self.historial[:self.posicion_actual + 1]

        # Ejecutar la acción
        accion.ejecutar(self)

        # Añadir al historial
        self.historial.append(accion)
        self.posicion_actual += 1

    def deshacer(self):
        """
        Deshace la última acción ejecutada.
        """

        if self.posicion_actual >= 0:
            # Deshacer la acción actual
            self.historial[self.posicion_actual].deshacer(self)
            self.posicion_actual -= 1
            return True
        return False

    def rehacer(self):
        """
        Rehace la siguiente acción en el historial.
        """

        if self.posicion_actual < len(self.historial) - 1:
            # Avanzar a la siguiente acción
            self.posicion_actual += 1
            # Ejecutar esa acción
            self.historial[self.posicion_actual].ejecutar(self)
            return True
        return False

    def escribir(self, texto):
        """
        Método para escribir texto en la posición actual del cursor.
        """

        accion = EscribirTexto(self.posicion_cursor, texto)
        self.ejecutar_accion(accion)

    def borrar(self, longitud):
        """
        Método para borrar texto desde la posición actual del cursor.
        """

        if self.posicion_cursor - longitud >= 0:
            accion = BorrarTexto(self.posicion_cursor - longitud, longitud)
            self.ejecutar_accion(accion)

    def copiar(self, longitud):
        """
        Método para copiar texto desde la posición actual del cursor.
        """

        if self.posicion_cursor + longitud <= len(self.texto):
            accion = CopiarTexto(self.posicion_cursor, longitud)
            self.ejecutar_accion(accion)

    def pegar(self):
        """
        Método para pegar el texto del portapapeles en la posición actual del cursor.
        """

        if self.portapapeles:
            accion = PegarTexto(self.posicion_cursor)
            self.ejecutar_accion(accion)

    def mostrar_historial(self):
        """
        Muestra el historial de acciones.
        """

        print("\nHistorial de acciones:")
        for i, accion in enumerate(self.historial):
            marcador = "→" if i == self.posicion_actual else " "
            print(f"{marcador} {i+1}. {accion.descripcion}")

    def mostrar_estado(self):
        """
        Muestra el estado actual del editor.
        """

        print("\nEditor de Texto")
        print("==============")
        print(f"Texto: '{self.texto}'")
        print(f"Posición del cursor: {self.posicion_cursor}")
        print(f"Portapapeles: '{self.portapapeles}'")

        # Mostrar posición del cursor visualmente
        print("\nRepresentación visual:")
        cursor_visual = " " * self.posicion_cursor + "^"
        print(self.texto)
        print(cursor_visual)
