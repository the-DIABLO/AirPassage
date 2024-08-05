import customtkinter as ctk
import csv
from datetime import datetime

# Función para cargar los datos del archivo CSV
def cargar_vuelos():
    vuelos = {}
    with open('BaseDatos/vuelos.csv', mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            numero_vuelo = fila['id']  # Usa 'id' como identificador del vuelo
            hora_salida = fila['hora_salida']
            estado = determinar_estado(hora_salida)
            vuelos[numero_vuelo] = {
                "aerolinea": fila['aerolinea'],
                "origen": fila['origen'],
                "destino": fila['destino'],
                "hora_salida": hora_salida,
                "estado": estado
            }
    return vuelos

def determinar_estado(hora_salida):
    # Asume que 'hora_salida' está en formato 'HH:MM' (24 horas)
    hora_salida_dt = datetime.strptime(hora_salida, '%H:%M')
    ahora_dt = datetime.now().replace(microsecond=0, second=0, minute=0)
    if hora_salida_dt < ahora_dt:
        return "Programada"
    else:
        return "Cancelada"

def mostrar_vuelos(frame, filtro=None):
    limpiar_frame(frame)

    ctk.CTkLabel(frame, text="Estado de Vuelos", font=("Arial", 20)).grid(row=0, column=0, columnspan=6, pady=10)

    search_frame = ctk.CTkFrame(frame)
    search_frame.grid(row=1, column=0, columnspan=6, pady=10)

    ctk.CTkLabel(search_frame, text="Buscar vuelo:").pack(side="left", padx=5)
    entry_busqueda = ctk.CTkEntry(search_frame)
    entry_busqueda.pack(side="left", padx=5)

    def buscar_vuelo():
        filtro = entry_busqueda.get().upper()
        mostrar_vuelos(frame, filtro)

    ctk.CTkButton(search_frame, text="Buscar", command=buscar_vuelo).pack(side="left", padx=5)

    headers = ["id", "aerolínea", "origen", "destino", "hora_salida", "Estado"]
    for col, header in enumerate(headers):
        ctk.CTkLabel(frame, text=header, font=("Arial", 12, "bold")).grid(row=2, column=col, padx=10, pady=5, sticky="nsew")

    vuelos = cargar_vuelos()  # Cargar los vuelos desde el CSV

    for row, (numero_vuelo, datos) in enumerate(vuelos.items(), start=3):
        if filtro and filtro not in numero_vuelo:
            continue
        ctk.CTkLabel(frame, text=numero_vuelo).grid(row=row, column=0, padx=10, pady=2, sticky="nsew")
        ctk.CTkLabel(frame, text=datos["aerolinea"]).grid(row=row, column=1, padx=10, pady=2, sticky="nsew")
        ctk.CTkLabel(frame, text=datos["origen"]).grid(row=row, column=2, padx=10, pady=2, sticky="nsew")
        ctk.CTkLabel(frame, text=datos["destino"]).grid(row=row, column=3, padx=10, pady=2, sticky="nsew")
        ctk.CTkLabel(frame, text=datos["hora_salida"]).grid(row=row, column=4, padx=10, pady=2, sticky="nsew")
        ctk.CTkLabel(frame, text=datos["estado"]).grid(row=row, column=5, padx=10, pady=2, sticky="nsew")

    for col in range(6):
        frame.grid_columnconfigure(col, weight=1)

def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def main():
    ventana = ctk.CTk()
    ventana.title("Estado de Vuelos")
    ventana.geometry("800x600")

    frame_principal = ctk.CTkFrame(ventana)
    frame_principal.pack(expand=True, fill="both", padx=20, pady=20)

    mostrar_vuelos(frame_principal)

    ventana.mainloop()

if __name__ == "__main__":
    main()
