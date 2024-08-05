import random
import string
import subprocess

from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry, CTkComboBox
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk  # Asegúrate de importar tkinter
from MapaVuelo import MapaVuelo
import re
import csv
import creadorPDF
# Variables globales
NOMBRE = None
APELLIDO = None
def generar_numero_ticket(longitud=6):
    caracteres = string.ascii_uppercase + string.digits  # Letras mayúsculas y dígitos
    numero_ticket = ''.join(random.choices(caracteres, k=longitud))
    return numero_ticket

# Generar un número de ticket aleatorio
NUMTICKET = generar_numero_ticket()

def cargar_datos():
    global NOMBRE, APELLIDO

    with open('BaseDatos/datos_pasajeros.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            NOMBRE = row['Nombre']
            APELLIDO = row['Apellido']
            # Solo leemos la primera fila. Si necesitas leer más, puedes adaptar este bucle.
            break
# Llamada a la función para cargar los datos
cargar_datos()

# Imprimir las variables globales para verificar
print(f"NOMBRE: {NOMBRE}")
print(f"APELLIDO: {APELLIDO}")


def leer_vuelos_csv(archivo):
    vuelos = []
    with open(archivo, mode='r', newline='', encoding='utf-8') as file:
        vuelos_csv = csv.DictReader(file)
        columnas = vuelos_csv.fieldnames  # Obtener los nombres de las columnas
        for fila in vuelos_csv:
            vuelos.append(fila)
    return vuelos, columnas

# Leer datos desde 'BaseDatos/vuelos.csv'
vuelos_disponibles, columnas = leer_vuelos_csv('BaseDatos/vuelos.csv')

def ajustar_ancho_columnas(tree, columnas, factor=8):
    for col in columnas:
        max_width = max([len(str(tree.set(k, col))) for k in tree.get_children('')])
        tree.column(col, width=max_width * factor)

def show_menu():
    for widget in frame.winfo_children():
        widget.destroy()

    # Mostrar el menú principal
    CTkLabel(master=frame, text="Vuelos", text_color="#000000", anchor="center", justify="center",
             font=("Arial Bold", 24)).pack(anchor="center", pady=(50, 5))

    CTkButton(master=frame, text="Mostrar todos los Vuelos", fg_color="#0485ad", hover_color="#5b94aa",
              font=("Arial Bold", 12), text_color="#ffffff", width=225, command=show_mostrar).pack(anchor="center", pady=(40, 0))
    CTkButton(master=frame, text="Buscar Vuelos", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=show_buscar).pack(anchor="center", pady=(40, 0))
    CTkButton(master=frame, text="Reservar Vuelo", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=show_reservar).pack(anchor="center", pady=(40, 0))
    CTkButton(master=frame, text="Generar gráficas", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=ejecutar_graficas).pack(anchor="center", pady=(40, 0))
    CTkButton(master=frame, text="Salir", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=app.quit).pack(anchor="center", pady=(40, 0))
def ejecutar_graficas():
    subprocess.run(["python", "Graficas.py"])
def show_mostrar():
    for widget in frame.winfo_children():
        widget.destroy()

    # Mostrar la lista de vuelos
    CTkLabel(master=frame, text="Vuelos Existentes", text_color="#000000", anchor="center", justify="center",
             font=("Arial Bold", 24)).pack(anchor="center", pady=(20, 5))

    # Crear un Treeview para mostrar los vuelos
    tree = ttk.Treeview(frame, columns=columnas, show='headings')
    tree.pack(expand=True, fill='both', pady=(20, 20))

    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    for vuelo in vuelos_disponibles:
        tree.insert('', 'end', values=[vuelo.get(col, 'N/A') for col in columnas])

    ajustar_ancho_columnas(tree, columnas)

    CTkButton(master=frame, text="Volver al Menú", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=show_menu).pack(anchor="center", pady=(20, 0))

def show_buscar():
    for widget in frame.winfo_children():
        widget.destroy()

    def buscar_vuelo():
        criterio = criterio_combobox.get().lower()
        valor = valor_entry.get()

        vuelos_encontrados = [vuelo for vuelo in vuelos_disponibles if str(vuelo.get(criterio, '')).lower() == valor.lower()]

        for widget in result_frame.winfo_children():
            widget.destroy()

        if vuelos_encontrados:
            # Crear un Treeview para mostrar los vuelos encontrados
            tree = ttk.Treeview(result_frame, columns=columnas, show='headings')
            tree.pack(expand=True, fill='both', pady=(20, 20))

            for col in columnas:
                tree.heading(col, text=col)
                tree.column(col, anchor='center')

            for vuelo in vuelos_encontrados:
                tree.insert('', 'end', values=[vuelo.get(col, 'N/A') for col in columnas])

            ajustar_ancho_columnas(tree, columnas)
        else:
            CTkLabel(master=result_frame, text="No se encontraron vuelos con los criterios especificados",
                     text_color="#ff0000", anchor="center", justify="center", font=("Arial", 12)).pack(anchor="center", pady=(5, 5))

    CTkLabel(master=frame, text="Buscar Vuelos", text_color="#000000", anchor="center", justify="center",
             font=("Arial Bold", 24)).pack(anchor="center", pady=(50, 5))

    CTkLabel(master=frame, text="Buscar vuelo por:", text_color="#000000", anchor="center", justify="center",
             font=("Arial", 12)).pack(anchor="center", pady=(5, 5))
    criterio_combobox = CTkComboBox(master=frame, values=columnas)
    criterio_combobox.pack(anchor="center", pady=(5, 5))
    criterio_combobox.set(columnas[0])

    CTkLabel(master=frame, text="Ingrese el valor:", text_color="#000000", anchor="center", justify="center",
             font=("Arial", 12)).pack(anchor="center", pady=(5, 5))
    valor_entry = CTkEntry(master=frame, width=200)
    valor_entry.pack(anchor="center", pady=(5, 5))

    CTkButton(master=frame, text="Buscar", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=buscar_vuelo).pack(anchor="center", pady=(20, 0))

    result_frame = CTkFrame(master=frame, fg_color="#ffffff")
    result_frame.pack(expand=True, fill="both", pady=(20, 0))

    CTkButton(master=frame, text="Volver al Menú", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=show_menu).pack(anchor="center", pady=(20, 0))

def show_reservar():
    def leer_vuelos_csv(archivo):
        vuelos = []
        with open(archivo, mode='r', newline='', encoding='utf-8') as file:
            vuelos_csv = csv.DictReader(file)
            columnas = vuelos_csv.fieldnames  # Obtener los nombres de las columnas
            for fila in vuelos_csv:
                vuelos.append(fila)
        return vuelos, columnas

    # Leer datos desde 'BaseDatos/vuelos.csv'
    vuelos_disponibles, columnas = leer_vuelos_csv('BaseDatos/vuelos.csv')

    # Variable para guardar los detalles de la reserva
    global detalle_reserva
    detalle_reserva = {}

    def limpiar_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def mostrar_vuelos_disponibles(frame):
        limpiar_frame(frame)

        # Título de la tabla
        CTkLabel(frame, text="Vuelos Disponibles", text_color="#000000", font=("Arial", 20)).grid(row=0, column=0,
                                                                                                  columnspan=6, pady=10)

        # Encabezados de la tabla
        headers = [ ]  # Ejemplo de encabezados
        for col, header in enumerate(headers):
            CTkLabel(frame, text=header, text_color="#000000", font=("Arial", 12, "bold")).grid(row=1, column=col,
                                                                                                padx=10, pady=5,
                                                                                                sticky="nsew")

        # Mostrar los datos de los vuelos
        for row, vuelo in enumerate(vuelos_disponibles, start=2):
            num_cols = len(vuelo)  # Número de columnas de datos
            for col, (key, value) in enumerate(vuelo.items()):
                CTkLabel(frame, text=value, text_color="#000000").grid(row=row, column=col, padx=10, pady=2,
                                                                       sticky="nsew")

            # Colocar el botón "Seleccionar" en la última columna de la fila
            CTkButton(frame, text="Seleccionar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff",
                      command=lambda v=vuelo: mostrar_resumen_vuelo(frame, v)).grid(row=row, column=num_cols, padx=10,
                                                                                    pady=2)

        # Configurar el peso de las columnas
        for col in range(num_cols + 1):  # Incluyendo la columna del botón
            frame.grid_columnconfigure(col, weight=1)

        # Botón de regresar
        CTkButton(frame, text="Regresar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff",
                  command=show_menu).grid(row=row + 1, column=0, columnspan=num_cols + 1, pady=20)

    def mostrar_resumen_vuelo(frame, vuelo):
        limpiar_frame(frame)

        global detalle_reserva
        detalle_reserva = vuelo

        CTkLabel(frame, text="Resumen del Vuelo Seleccionado", text_color="#000000", font=("Arial", 20)).pack(pady=10)
        global atributosVuelo
        atributosVuelo = []
        for key, value in vuelo.items():
            CTkLabel(frame, text=f"{key.capitalize()}: {value}", text_color="#000000").pack(pady=2)
            atributosVuelo.append({value})

        CTkButton(frame, text="Continuar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=lambda: solicitar_datos_pasajero(frame)).pack(pady=10)
        CTkButton(frame, text="Cancelar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=lambda: (messagebox.showinfo("Cancelado", "Reservación cancelada"), show_menu())).pack(pady=10)

    def limpiar_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    # Función para solicitar datos del pasajero y guardarlos en un archivo CSV
    def solicitar_datos_pasajero(frame):
        limpiar_frame(frame)

        CTkLabel(frame, text="Datos del Pasajero", text_color="#000000", font=("Arial", 20)).pack(pady=10)

        campos = ["Nombre", "Apellido", "Número de Pasaporte", "Nacionalidad", "Correo"]

        entries = {}
        for campo in campos:
            CTkLabel(frame, text=campo, text_color="#000000").pack(pady=2)
            entry = CTkEntry(frame)
            entry.pack(pady=2)
            entries[campo] = entry


        def validar_datos_pasajero():
            global atributosCampos
            atributosCampos = []
            for campo, entry in entries.items():
                valor = entry.get().strip()
                atributosCampos.append(valor)
                if not valor:
                    messagebox.showerror("Error", "Uno o más campos vacíos, revise correctamente.")
                    return False
                if campo in ["Nombre", "Apellido", "Nacionalidad"] and not valor.isalpha():
                    messagebox.showerror("Error", f"{campo.lower()} inválido.")
                    return False
                if campo == "Número de Pasaporte" and not valor.isalnum():
                    messagebox.showerror("Error", "Número de pasaporte inválido.")
                    return False
                if campo == "Correo":
                    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                    if not re.match(email_regex, valor):
                        messagebox.showerror("Error", "Correo inválido.")
                        return False
            return True

        def guardar_datos():
            if validar_datos_pasajero():
                datos = {campo: entry.get() for campo, entry in entries.items()}
                archivo_csv = 'datos_pasajeros.csv'
                with open(archivo_csv, mode='a', newline='', encoding='utf-8') as archivo:
                    escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
                    if archivo.tell() == 0:  # Escribe el encabezado solo si el archivo está vacío
                        escritor_csv.writeheader()
                    escritor_csv.writerow(datos)
                print(f"Datos guardados en {archivo_csv}")
                messagebox.showinfo("Éxito", "Datos guardados correctamente")

        def continuar():
            if validar_datos_pasajero():
                for campo, entry in entries.items():
                    detalle_reserva[campo.lower()] = entry.get()
                seleccionar_asiento()
        # Añadir un botón para guardar los datos
        CTkButton(frame, text="Guardar", command=guardar_datos).pack(pady=10)
        CTkButton(frame, text="Continuar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff",
                  command=continuar).pack(pady=10)
        CTkButton(frame, text="Cancelar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff",
                  command=lambda: (messagebox.showinfo("Cancelado", "Reservación cancelada"), show_menu())).pack(
            pady=10)

    def seleccionar_asiento():
        MapaVuelo(asiento_seleccionado_callback)

    def asiento_seleccionado_callback(asiento, claseS):
        global detalle_reserva
        detalle_reserva["numero_asiento"] = asiento
        detalle_reserva["clase"] = claseS
        global NUMASIENTO
        NUMASIENTO=detalle_reserva["numero_asiento"]
        mostrar_menu_pago(frame)

    def mostrar_menu_pago(frame):
        limpiar_frame(frame)

        CTkLabel(frame, text="Método de Pago", text_color="#000000", font=("Arial", 20)).pack(pady=10)
        CTkButton(frame, text="Tarjeta de Crédito/Débito", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=lambda: solicitar_datos_tarjeta(frame)).pack(pady=10)
        CTkButton(frame, text="PayPal", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=lambda: solicitar_datos_paypal(frame)).pack(pady=10)
        CTkButton(frame, text="Cancelar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=lambda: (messagebox.showinfo("Cancelado", "Reservación cancelada"), show_menu())).pack(pady=10)

    def solicitar_datos_tarjeta(frame):
        limpiar_frame(frame)

        CTkLabel(frame, text="Datos de la Tarjeta de Crédito/Débito", text_color="#000000", font=("Arial", 20)).pack(pady=10)

        campos = ["Número de Tarjeta", "Nombre del Titular", "Fecha de Vencimiento (MM/AA)", "CVV"]
        entries = {}
        for campo in campos:
            CTkLabel(frame, text=campo, text_color="#000000").pack(pady=2)
            if campo == "Número de Tarjeta":
                entry = CTkEntry(frame)
                entry.bind("<KeyRelease>", format_card_number)
            elif campo == "Fecha de Vencimiento (MM/AA)":
                entry = CTkEntry(frame)
                entry.bind("<KeyRelease>", format_expiry_date)
            elif campo == "CVV":
                entry = CTkEntry(frame, show="*")
            else:
                entry = CTkEntry(frame)
            entry.pack(pady=2)
            entries[campo] = entry

        def validar_datos_tarjeta():
            for campo, entry in entries.items():
                valor = entry.get().strip()
                if not valor:
                    messagebox.showerror("Error", "Uno o más campos vacíos, revise correctamente.")
                    return False
                if campo == "Número de Tarjeta" and (not valor.replace(" ", "").isdigit() or len(valor.replace(" ", "")) != 16):
                    messagebox.showerror("Error", "Número de tarjeta inválido.")
                    return False
                if campo == "Nombre del Titular" and not valor.replace(" ", "").isalpha():
                    messagebox.showerror("Error", "Nombre del titular inválido.")
                    return False
                if campo == "Fecha de Vencimiento (MM/AA)" and (not re.match(r"^(0[1-9]|1[0-2])/[0-9]{2}$", valor)):
                    messagebox.showerror("Error", "Fecha de vencimiento inválida.")
                    return False
                if campo == "CVV" and (not valor.isdigit() or len(valor) != 3):
                    messagebox.showerror("Error", "CVV inválido.")
                    return False
            return True

        def continuar():
            if validar_datos_tarjeta():
                for campo, entry in entries.items():
                    detalle_reserva[campo.lower()] = entry.get()
                mostrar_resumen_final(frame)

        CTkButton(frame, text="Continuar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=continuar).pack(pady=10)
        CTkButton(frame, text="Cancelar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=lambda: (messagebox.showinfo("Cancelado", "Reservación cancelada"), show_menu())).pack(pady=10)

    def format_card_number(event):
        widget = event.widget
        value = widget.get().replace(" ", "")
        if value.isdigit():
            formatted = " ".join(value[i:i + 4] for i in range(0, len(value), 4))
            widget.delete(0, tk.END)
            widget.insert(0, formatted)

    def format_expiry_date(event):
        widget = event.widget
        value = widget.get().replace("/", "")
        if value.isdigit() and len(value) <= 4:
            formatted = "/".join(value[i:i + 2] for i in range(0, len(value), 2))
            widget.delete(0, tk.END)
            widget.insert(0, formatted)

    def solicitar_datos_paypal(frame):
        limpiar_frame(frame)

        CTkLabel(frame, text="Datos de PayPal", text_color="#000000", font=("Arial", 20)).pack(pady=10)

        campos = ["Correo electrónico", "Contraseña"]
        entries = {}
        for campo in campos:
            CTkLabel(frame, text=campo, text_color="#000000").pack(pady=2)
            entry = CTkEntry(frame, show="*" if campo == "Contraseña" else None)
            entry.pack(pady=2)
            entries[campo] = entry

        def validar_datos_paypal():
            correo = entries["Correo electrónico"].get().strip()
            contrasena = entries["Contraseña"].get().strip()
            if not correo or not contrasena:
                messagebox.showerror("Error", "Uno o más campos vacíos, revise correctamente.")
                return False
            if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
                messagebox.showerror("Error", "Correo electrónico inválido.")
                return False
            return True

        def continuar():
            if validar_datos_paypal():
                for campo, entry in entries.items():
                    detalle_reserva[campo.lower()] = entry.get()
                mostrar_resumen_final(frame)

        CTkButton(frame, text="Continuar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=continuar).pack(pady=10)
        CTkButton(frame, text="Cancelar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=lambda: (messagebox.showinfo("Cancelado", "Reservación cancelada"), show_menu())).pack(pady=10)

    def mostrar_resumen_final(frame):
        limpiar_frame(frame)

        CTkLabel(frame, text="Resumen de la Reserva", text_color="#000000", font=("Arial", 20)).pack(pady=10)

        resumen = {
            "Vuelo": detalle_reserva.get("id", ""),
            "Aerolinea": detalle_reserva.get("aerolinea", ""),
            "Origen": detalle_reserva.get("origen", ""),
            "Destino": detalle_reserva.get("destino", ""),
            "Hora salida":  detalle_reserva.get("hora_salida", ""),
            "Numero asiento": detalle_reserva.get("numero_asiento", ""),
            "Puerta embarque": "B12",
            "Total a Pagar": detalle_reserva.get("precio", "")
        }

        for key, value in resumen.items():
            CTkLabel(frame, text=f"{key}: {value}", text_color="#000000").pack(pady=2)

        def pagar():
            messagebox.showinfo("Éxito", "Pago realizado exitosamente")
            creadorPDF.EnviarCorreoConPDF(atributosCampos[0], atributosCampos[1], generar_numero_ticket(longitud=6),
                                          detalle_reserva.get("clase", ""), detalle_reserva.get("id", ""), detalle_reserva.get("origen", ""),
                                          detalle_reserva.get("destino", ""), detalle_reserva.get("hora_salida", ""), detalle_reserva.get("hora_llegada", ""),
                                                detalle_reserva.get("numero_asiento", ""), atributosCampos[4])
            messagebox.showinfo("Éxito", "Correo enviado exitosamente")
            show_menu()

        CTkButton(frame, text="Pagar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=pagar).pack(pady=10)
        CTkButton(frame, text="Cancelar", fg_color="#0485ad", hover_color="#5b94aa", text_color="#ffffff", command=lambda: (messagebox.showinfo("Cancelado", "Reservación cancelada"), show_menu())).pack(pady=10)

    mostrar_vuelos_disponibles(frame)

app = CTk()
app.geometry("800x600")
app.title("Vuelos")

frame = CTkFrame(master=app, fg_color="#ffffff")
frame.pack(expand=True, fill="both")

show_menu()

app.mainloop()