"""
Implementación de la clase Ruta.
"""


class Ruta:
    """
    Representa una ruta en un mapa.
    """

    def __init__(self):
        # Diccionario que representa el grafo de estaciones
        # Cada estación tiene una lista de tuplas (estación_destino, tiempo_minutos)
        self.estaciones = {}

        # Inicializar el mapa con algunas estaciones de ejemplo
        # En una aplicación real, esto podría cargarse desde un archivo o base de datos
        self.inicializar_mapa_ejemplo()

    def inicializar_mapa_ejemplo(self):
        """
        Inicializa un mapa de ejemplo con estaciones y tiempos entre ellas.
        """

        # Formato: "estación": [(estación_destino, tiempo_en_minutos), ...]
        self.estaciones = {
            "Terminal Central": [("Plaza Mayor", 10), ("Parque Industrial", 15)],
            "Plaza Mayor": [
                ("Terminal Central", 10),
                ("Universidad", 8),
                ("Centro Comercial", 5),
            ],
            "Parque Industrial": [("Terminal Central", 15), ("Zona Residencial", 12)],
            "Universidad": [("Plaza Mayor", 8), ("Hospital", 6)],
            "Centro Comercial": [
                ("Plaza Mayor", 5),
                ("Zona Residencial", 7),
                ("Hospital", 9),
            ],
            "Zona Residencial": [("Parque Industrial", 12), ("Centro Comercial", 7)],
            "Hospital": [("Universidad", 6), ("Centro Comercial", 9)],
        }

    def agregar_estacion(self, nombre):
        """
        Agrega una nueva estación al mapa.
        """

        if nombre not in self.estaciones:
            self.estaciones[nombre] = []
            return True
        return False

    def conectar_estaciones(self, origen, destino, tiempo):
        """
        Conecta dos estaciones con un tiempo determinado en minutos.
        """

        if origen in self.estaciones and destino in self.estaciones:
            # Verificar si ya existe la conexión
            for i, (est, _) in enumerate(self.estaciones[origen]):
                if est == destino:
                    # Actualizar tiempo si ya existe la conexión
                    self.estaciones[origen][i] = (destino, tiempo)
                    return True

            # Agregar nueva conexión si no existe
            self.estaciones[origen].append((destino, tiempo))
            return True
        return False

    def obtener_conexiones(self):
        """
        Devuelve todas las conexiones del mapa.
        """

        conexiones = []
        for origen, destinos in self.estaciones.items():
            for destino, tiempo in destinos:
                conexiones.append((origen, destino, tiempo))
        return conexiones

    def calcular_ruta_mas_rapida(self, inicio, fin):
        """
        Implementa el algoritmo de Dijkstra para encontrar la ruta más rápida.
        """

        if inicio not in self.estaciones or fin not in self.estaciones:
            return None, None

        # Inicializar distancias con valores infinitos
        tiempos = {estacion: float("infinity") for estacion in self.estaciones}
        tiempos[inicio] = 0

        # Diccionario para almacenar el predecesor de cada estación en la ruta más corta
        predecesores = {estacion: None for estacion in self.estaciones}

        # Conjunto de nodos no visitados
        no_visitados = set(self.estaciones.keys())

        while no_visitados:
            # Encontrar la estación no visitada con el tiempo mínimo actual
            actual = min(no_visitados, key=lambda x: tiempos[x])

            # Si llegamos al destino o si el tiempo es infinito (no hay ruta)
            if actual == fin or tiempos[actual] == float("infinity"):
                break

            no_visitados.remove(actual)

            # Revisar vecinos de la estación actual
            for vecino, tiempo in self.estaciones[actual]:
                # Calcular nuevo tiempo a través de esta ruta
                nuevo_tiempo = tiempos[actual] + tiempo

                # Si encontramos una ruta más rápida, actualizamos
                if nuevo_tiempo < tiempos[vecino]:
                    tiempos[vecino] = nuevo_tiempo
                    predecesores[vecino] = actual

        # Reconstruir la ruta
        if tiempos[fin] == float("infinity"):
            return None, None  # No hay ruta

        ruta = []
        actual = fin
        while actual:
            ruta.insert(0, actual)
            actual = predecesores[actual]

        return ruta, tiempos[fin]

    def mostrar_estaciones(self):
        """
        Muestra todas las estaciones disponibles.
        """

        return list(self.estaciones.keys())
