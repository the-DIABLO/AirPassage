import csv
import os

# Define the path to the CSV file
csv_path = os.path.join(os.getcwd(), 'BaseDatos/reservas.csv')

# Data to be written to the CSV
data = [
    ["ID_Reserva", "ID_Usuario", "ID_Asiento", "Fecha_Reserva", "Total_Pago"],
    [1, 1, 1, "2024-07-25", 886.15],
    [2, 2, 2, "2024-07-26", 886.15],
    [3, 1, 3, "2024-07-27", 886.15],
    [4, 3, 4, "2024-07-28", 961.72],
    [5, 4, 5, "2024-07-29", 961.72]
]

# Write the data to the CSV file
with open(csv_path, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(data)

print(f"Archivo CSV generado en {csv_path}")
