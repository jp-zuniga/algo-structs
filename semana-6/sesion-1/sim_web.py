"""
Implementación de la clase SimWeb, que maneja la simulación de navegación.
"""

from typing import Optional

from . import Pila


class SimWeb:
    """
    Simulación de un navegador web con una pila de las páginas web visitadas.
    """

    def __init__(self, paginas: Pila) -> None:
        self.pila_paginas = paginas
        self.pagina_actual: Optional[str] = None

    def visitar_nueva(self, nueva_pagina: str) -> None:
        """
        Agrega la página actual a la pila y cambia a la nueva página.
        """

        self.pila_paginas.add(nueva_pagina)
        self.pagina_actual = nueva_pagina

    def retroceder(self) -> None:
        """
        Extrae la última página de la pila y la muestra como la página actual.
        """

        self.pagina_actual = self.pila_paginas.extract()

    def obtener_actual(self) -> str:
        """
        Retorna la página donde se encuentra el usuario.
        """

        return (
            self.pagina_actual
            if self.pagina_actual is not None
            else "No se ha visitado ninguna página web."
        )
