import random
import os
from datetime import datetime, timedelta
import csv


def generar_datos_vuelo(n):
    aerolineas = ["Air Passage", "Sky High", "FlyAway", "Wings Air", "Eagle Airlines"]
    vuelos = []
    for i in range(1, n + 1):
        aerolinea = random.choice(aerolineas)
        fecha_salida = datetime.now() + timedelta(
            days=random.randint(1, 30))  # Fecha de salida aleatoria dentro de los próximos 30 días
        hora_salida = fecha_salida + timedelta(hours=random.randint(1, 10))
        hora_llegada = hora_salida + timedelta(hours=random.randint(1, 5))
        duracion = hora_llegada - hora_salida
        precio = round(random.uniform(100, 1000), 2)
        vuelo = [i, aerolinea, fecha_salida.strftime('%Y-%m-%d'), hora_salida.strftime('%H:%M'),
                 hora_llegada.strftime('%H:%M'), str(duracion), precio]
        vuelos.append(vuelo)
    return vuelos


def escribir_csv(nombre_archivo, datos):
    # Asegurarse de que el directorio existe
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

    # Escribir los datos en el archivo CSV
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        # Escribir la cabecera del archivo CSV
        escritor_csv.writerow(
            ['ID', 'Aerolínea', 'Fecha de Salida', 'Hora de Salida', 'Hora de Llegada', 'Duración', 'Precio'])
        # Escribir los datos de los vuelos
        escritor_csv.writerows(datos)


# Generar datos de vuelos
datos_vuelos = generar_datos_vuelo(10)

# Escribir los datos de los vuelos en un archivo CSV
escribir_csv('BaseDatos/vuelos.csv', datos_vuelos)
