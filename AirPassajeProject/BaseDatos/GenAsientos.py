import csv
import os

# Define the path to the CSV file
csv_path = os.path.join(os.getcwd(), 'asientos.csv')

# Data to be written to the CSV
data = [
    ["ID_Asiento", "ID_Vuelo", "Reservado"],
    [1, 101, "No"],
    [2, 101, "Sí"],
    [3, 101, "No"],
    [4, 102, "No"],
    [5, 102, "Sí"],
    [6, 103, "No"],
    [7, 103, "No"],
    [8, 104, "Sí"],
    [9, 104, "No"]
]

# Write the data to the CSV file
with open(csv_path, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(data)

print(f"Archivo CSV generado en {csv_path}")
