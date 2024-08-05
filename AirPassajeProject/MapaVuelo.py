import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Variables globales para simular persistencia de los asientos reservados
asientos_primera_clase_reservados = [[False for _ in range(3)] for _ in range(6)]
asientos_clase_economica_reservados = [[False for _ in range(20)] for _ in range(6)]

class MapaVuelo:

    def __init__(self, seleccionar_asiento_callback):
        self.root = tk.Toplevel()
        self.seleccionar_asiento_callback = seleccionar_asiento_callback
        self.asiento_seleccionado = None
        self.asientoSelec = None
        self.claseSelec = None

        # Ruta de la imagen
        imagen_path = "imagen_2024-07-18_223833796-removebg-preview.png"

        # Cargar la imagen de los asientos
        try:
            self.img = Image.open(imagen_path)
            self.img = self.img.resize((800, 300), Image.LANCZOS)
            self.img = ImageTk.PhotoImage(self.img)
        except FileNotFoundError:
            print(f"No se encontró la imagen en la ruta: {imagen_path}")
            self.root.destroy()

        # Crear un Label para mostrar la imagen
        label_img = tk.Label(self.root, image=self.img)
        label_img.pack()

        # Función para mostrar el estado de un asiento al hacer clic
        def mostrar_estado_asiento(fila, columna, clase, boton):
            if clase == "primera":
                estado = asientos_primera_clase_reservados[fila][columna]
            else:
                estado = asientos_clase_economica_reservados[fila][columna]

            if estado:
                messagebox.showinfo("Estado del Asiento", "Asiento no disponible")
            else:
                estado_texto = "Libre"
                clase_texto = "Primera Clase" if clase == "primera" else "Clase Económica"
                numero_asiento = f"{chr(65 + fila)}{columna + 1 if clase == 'primera' else columna + 4}"
                self.claseSelec = clase_texto
                self.asientoSelec = numero_asiento
                messagebox.showinfo("Estado del Asiento",
                                    f"Clase '{clase_texto}' - Asiento '{numero_asiento}' {estado_texto}")
                boton.config(bg="red", state="disabled")  # Cambia el color del botón y lo desactiva
                if clase == "primera":
                    asientos_primera_clase_reservados[fila][columna] = True
                else:
                    asientos_clase_economica_reservados[fila][columna] = True
                self.asiento_seleccionado = numero_asiento
                self.claseSelec = clase_texto
                self.root.destroy()
                self.seleccionar_asiento_callback(self.asiento_seleccionado, self.claseSelec)

        # Crear un frame para los asientos
        frame_asientos = tk.Frame(self.root)
        frame_asientos.pack()

        # Crear la disposición de los asientos para primera clase y clase económica
        asientos_primera_clase = [[False for _ in range(3)] for _ in range(6)]  # 3 columnas para primera clase
        asientos_clase_economica = [[False for _ in range(20)] for _ in range(6)]  # 20 columnas para clase económica

        # Función auxiliar para crear botones de asientos
        def crear_boton_asiento(fila, columna, clase):
            texto = f"{chr(65 + fila)}{columna + 1 if clase == 'primera' else columna + 4}"
            if clase == "primera" and asientos_primera_clase_reservados[fila][columna]:
                boton = tk.Button(frame_asientos, text=texto, bg="red", state="disabled")
            elif clase == "economica" and asientos_clase_economica_reservados[fila][columna]:
                boton = tk.Button(frame_asientos, text=texto, bg="red", state="disabled")
            else:
                boton = tk.Button(frame_asientos, text=texto,
                                  command=lambda: mostrar_estado_asiento(fila, columna, clase, boton))
            return boton

        # Crear botones para los asientos de primera clase
        for columna in range(3):
            for fila in range(6):
                boton = crear_boton_asiento(fila, columna, "primera")
                boton.grid(row=fila, column=columna)

        # Crear una separación entre primera clase y clase económica
        separator = tk.Label(frame_asientos, text="   |   ")
        separator.grid(row=0, column=3, rowspan=6)

        # Crear botones para los asientos de clase económica
        for columna in range(20):
            for fila in range(6):
                boton = crear_boton_asiento(fila, columna, "economica")
                boton.grid(row=fila, column=columna + 4)

        # Ejecutar la ventana principal
        self.root.mainloop()
