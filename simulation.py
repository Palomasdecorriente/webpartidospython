import random

class Equipo:
    def __init__(self, nombre, habilidad, promedio_goles_por_partido):
        self.nombre = nombre
        self.habilidad = habilidad
        self.promedio_goles_por_partido = promedio_goles_por_partido

    def calcular_probabilidad_de_ganar(self, otro_equipo):
        # Calcula la probabilidad de ganar del equipo local
        probabilidad_de_ganar = self.habilidad / (self.habilidad + otro_equipo.habilidad)
        return probabilidad_de_ganar

    def calcular_goles(self, probabilidad_de_ganar):
        # Calcula el número de goles del equipo
        goles = round(self.promedio_goles_por_partido * probabilidad_de_ganar)
        return goles

def calcular_resultado(equipo_local, equipo_visitante):
    # Calcula la probabilidad de ganar del equipo local
    probabilidad_de_ganar_local = equipo_local.calcular_probabilidad_de_ganar(equipo_visitante)

    # Calcula la probabilidad de ganar del equipo visitante
    probabilidad_de_ganar_visitante = equipo_visitante.calcular_probabilidad_de_ganar(equipo_local)

    # Calcula el número de goles del equipo local
    goles_local = equipo_local.calcular_goles(probabilidad_de_ganar_local)

    # Calcula el número de goles del equipo visitante
    goles_visitante = equipo_visitante.calcular_goles(probabilidad_de_ganar_visitante)

    return goles_local, goles_visitante

while True:
    # Pide el nombre del equipo local y visitante
    nombre_local = input("Ingrese el nombre del equipo local: ")
    nombre_visitante = input("Ingrese el nombre del equipo visitante: ")

    # Pide la habilidad del equipo local y visitante
    habilidad_local = int(input("Ingrese la habilidad del equipo local (1-100): "))
    habilidad_visitante = int(input("Ingrese la habilidad del equipo visitante (1-100): "))

    # Pide el promedio de goles por partido del equipo local y visitante
    promedio_goles_local = float(input("Ingrese el promedio de goles por partido del equipo local: "))
    promedio_goles_visitante = float(input("Ingrese el promedio de goles por partido del equipo visitante: "))

    # Crea objetos de la clase Equipo
    equipo_local = Equipo(nombre_local, habilidad_local, promedio_goles_local)
    equipo_visitante = Equipo(nombre_visitante, habilidad_visitante, promedio_goles_visitante)

    # Calcula el resultado del partido
    goles_local, goles_visitante = calcular_resultado(equipo_local, equipo_visitante)

    # Muestra el resultado
    print(f"Resultado del partido: {equipo_local.nombre} {goles_local} - {goles_visitante} {equipo_visitante.nombre}")

    # Pregunta si se desea continuar
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() != 's':
        break
    