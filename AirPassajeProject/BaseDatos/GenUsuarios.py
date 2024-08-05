import csv
import os

# Define the path to the CSV file
csv_path = os.path.join(os.getcwd(), 'BaseDatos/registros.csv')

# Data to be written to the CSV
data = [
    ["ID", "Nombre", "Apellido", "Correo", "Contraseña", "Confirmación"],
    [1, "Ariadna", "Ceron", "ari@gmail.com", "Ari12345", "Ari12345"],
    [2, "Maria", "Gomez", "maria.gomez@example.com", "mypassword", "mypassword"],
    [3, "Carlos", "Lopez", "carlos.lopez@example.com", "securepass", "securepass"],
    [4, "Ana", "Martinez", "ana.martinez@example.com", "anapass", "anapass"],
    [5, "Luis", "Torres", "luis.torres@example.com", "torres123", "torres123"]
]

# Write the data to the CSV file
with open(csv_path, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(data)

print(f"Archivo CSV generado en {csv_path}")
