import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import customtkinter as ctk
import os

# Datos
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'aerolinea': ['Sky High', 'Eagle Airlines', 'Eagle Airlines', 'Sky High', 'Sky High', 'Air Passage', 'Air Passage', 'Wings Air', 'Wings Air', 'Air Passage'],
    'origen': ['Nueva York', 'Los Ángeles', 'Nueva York', 'Nueva York', 'Nueva York', 'Chicago', 'Chicago', 'Nueva York', 'Houston', 'Los Ángeles'],
    'destino': ['Houston', 'Houston', 'Houston', 'Miami', 'Miami', 'Miami', 'Los Ángeles', 'Houston', 'Los Ángeles', 'Nueva York'],
    'hora_salida': ['08:51', '00:51', '06:51', '08:51', '01:51', '03:51', '06:51', '05:51', '08:51', '01:51'],
    'hora_llegada': ['10:51', '05:51', '07:51', '13:51', '05:51', '06:51', '10:51', '09:51', '11:51', '05:51'],
    'duracion': ['2:00:00', '5:00:00', '1:00:00', '5:00:00', '4:00:00', '3:00:00', '4:00:00', '4:00:00', '3:00:00', '4:00:00'],
    'precio': [886.15, 961.72, 605.56, 177.16, 921.94, 534.45, 872.52, 655.89, 487.81, 522.42]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Convertir duracion a formato de tiempo
df['duracion'] = pd.to_timedelta(df['duracion'])

# Crear gráficos y guardarlos en archivos
def crear_graficos():
    # Graficar precios por aerolínea
    plt.figure(figsize=(12, 8))
    df.groupby('aerolinea')['precio'].mean().plot(kind='bar', color='skyblue')
    plt.title('Precio promedio por Aerolínea')
    plt.xlabel('Aerolínea')
    plt.ylabel('Precio promedio ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('precio_promedio_por_aerolinea.png')
    plt.close()

    # Graficar duración por destino
    plt.figure(figsize=(12, 8))
    df.groupby('destino')['duracion'].mean().dt.total_seconds().div(3600).plot(kind='bar', color='lightgreen')
    plt.title('Duración promedio de vuelo por Destino')
    plt.xlabel('Destino')
    plt.ylabel('Duración promedio (horas)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('duracion_promedio_por_destino.png')
    plt.close()

    # Graficar precios por origen
    plt.figure(figsize=(12, 8))
    df.groupby('origen')['precio'].mean().plot(kind='bar', color='salmon')
    plt.title('Precio promedio por Origen')
    plt.xlabel('Origen')
    plt.ylabel('Precio promedio ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('precio_promedio_por_origen.png')
    plt.close()

# Crear la interfaz gráfica
def mostrar_grafico(ruta):
    imagen = Image.open(ruta)
    imagen = imagen.resize((600, 450), Image.LANCZOS)
    ctk_imagen = ctk.CTkImage(dark_image=imagen, size=(600, 450))
    panel.configure(image=ctk_imagen)
    panel.image = ctk_imagen

def mostrar_precio_promedio_por_aerolinea():
    mostrar_grafico('precio_promedio_por_aerolinea.png')

def mostrar_duracion_promedio_por_destino():
    mostrar_grafico('duracion_promedio_por_destino.png')

def mostrar_precio_promedio_por_origen():
    mostrar_grafico('precio_promedio_por_origen.png')

def salir():
    app.destroy()

# Crear gráficos al inicio
crear_graficos()

# Configurar la interfaz
app = ctk.CTk()
app.title("Gráficos de Vuelos")
app.geometry("800x700")

boton1 = ctk.CTkButton(app, text="Precio Promedio por Aerolínea", command=mostrar_precio_promedio_por_aerolinea)
boton1.pack(pady=10)

boton2 = ctk.CTkButton(app, text="Duración Promedio por Destino", command=mostrar_duracion_promedio_por_destino)
boton2.pack(pady=10)

boton3 = ctk.CTkButton(app, text="Precio Promedio por Origen", command=mostrar_precio_promedio_por_origen)
boton3.pack(pady=10)

boton_salir = ctk.CTkButton(app, text="Salir", command=salir)
boton_salir.pack(pady=10)

panel = ctk.CTkLabel(app, text="")
panel.pack(pady=20)

app.mainloop()
