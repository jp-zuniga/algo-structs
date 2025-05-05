"""
Implementa las clases que representan las acciones permitidas en la aplicación.
"""


class Accion:
    """
    Clase base que representa una acción genérica en el editor.
    """

    def __init__(self, descripcion):
        self.descripcion = descripcion

    def ejecutar(self, editor):
        """
        Método a implementar en las clases derivadas.
        """

    def deshacer(self, editor):
        """
        Método a implementar en las clases derivadas.
        """


class EscribirTexto(Accion):
    """
    Acción de escribir texto en una posición específica.
    """

    def __init__(self, posicion, texto):
        super().__init__(f"Escribir '{texto}' en posición {posicion}")
        self.posicion = posicion
        self.texto = texto

    def ejecutar(self, editor):
        editor.texto = (
            editor.texto[: self.posicion] + self.texto + editor.texto[self.posicion :]
        )
        editor.posicion_cursor = self.posicion + len(self.texto)

    def deshacer(self, editor):
        # Eliminar el texto que se escribió
        editor.texto = (
            editor.texto[: self.posicion]
            + editor.texto[self.posicion + len(self.texto) :]
        )
        editor.posicion_cursor = self.posicion


class BorrarTexto(Accion):
    """
    Acción de borrar texto desde una posición específica.
    """

    def __init__(self, posicion, longitud):
        super().__init__(f"Borrar {longitud} caracteres desde posición {posicion}")
        self.posicion = posicion
        self.longitud = longitud
        self.texto_borrado = None  # Se guardará al ejecutar

    def ejecutar(self, editor):
        # Guardar el texto que se va a borrar para poder recuperarlo al deshacer
        self.texto_borrado = editor.texto[self.posicion : self.posicion + self.longitud]
        editor.texto = (
            editor.texto[: self.posicion]
            + editor.texto[self.posicion + self.longitud :]
        )
        editor.posicion_cursor = self.posicion

    def deshacer(self, editor):
        # Restaurar el texto borrado
        editor.texto = (
            editor.texto[: self.posicion]
            + self.texto_borrado
            + editor.texto[self.posicion :]
        )
        editor.posicion_cursor = self.posicion + len(self.texto_borrado)


class CopiarTexto(Accion):
    """
    Acción de copiar texto al portapapeles.
    """

    def __init__(self, posicion, longitud):
        super().__init__(f"Copiar {longitud} caracteres desde posición {posicion}")
        self.posicion = posicion
        self.longitud = longitud
        self.texto_anterior_portapapeles = None  # Se guardará al ejecutar

    def ejecutar(self, editor):
        # Guardar el contenido anterior del portapapeles
        self.texto_anterior_portapapeles = editor.portapapeles
        editor.portapapeles = editor.texto[
            self.posicion : self.posicion + self.longitud
        ]

    def deshacer(self, editor):
        # Restaurar el portapapeles anterior
        editor.portapapeles = self.texto_anterior_portapapeles


class PegarTexto(Accion):
    """
    Acción de pegar texto desde el portapapeles.
    """

    def __init__(self, posicion):
        super().__init__(f"Pegar texto en posición {posicion}")
        self.posicion = posicion

    def ejecutar(self, editor):
        if editor.portapapeles:
            editor.texto = (
                editor.texto[: self.posicion]
                + editor.portapapeles
                + editor.texto[self.posicion :]
            )
            editor.posicion_cursor = self.posicion + len(editor.portapapeles)

    def deshacer(self, editor):
        if editor.portapapeles:
            # Eliminar el texto que se pegó
            editor.texto = (
                editor.texto[: self.posicion]
                + editor.texto[self.posicion + len(editor.portapapeles) :]
            )
            editor.posicion_cursor = self.posicion
