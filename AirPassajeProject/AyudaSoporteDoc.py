import tkinter as tk
from tkinter import messagebox
import webbrowser
from customtkinter import *
from PIL import Image

def abrir_enlace(url):
    webbrowser.open(url)

def mostrar_informacion_documentacion():
    info = """
    Información sobre la documentación necesaria para su vuelo:
    - Pasaporte: Debe estar vigente y en buen estado.
    - Visa: Verifique si necesita una visa para su destino.
    - Identificación: Puede ser su cédula o licencia de conducir.
    - Otros documentos: Cualquier otro documento requerido por la aerolínea o el país de destino.

    Para obtener más información, visite los siguientes enlaces:
    """
    messagebox.showinfo("Documentación", info)

    enlaces = [
        ("Sitio web del gobierno", "https://www.gob.mx/"),

        ("Información sobre visas", "https://travel.state.gov/content/travel.html"),
              ]

    enlaces_ventana = CTkToplevel()
    enlaces_ventana.title("Enlaces de Información")
    for texto, url in enlaces:
        enlace = CTkLabel(enlaces_ventana, text=texto, text_color="blue", cursor="hand2")
        enlace.pack(padx=10, pady=5)
        enlace.bind("<Button-1>", lambda e, url="https://www.gob.mx/": abrir_enlace("https://www.gob.mx/"))
        enlace.bind("<Button-1>", lambda e, url="https://travel.state.gov/content/travel.html": abrir_enlace("https://travel.state.gov/content/travel.html"))
def enviar_correo(destinatario, numero_ticket):
    # Simulación del envío de correo (reemplaza esta función según tus necesidades)
    messagebox.showinfo("Correo enviado",
                        f"Se ha enviado un correo de confirmación a {destinatario} con el número de ticket {numero_ticket}")

def mostrar_ayuda():
    faqs = {
        "¿Cómo contacto al soporte técnico?": "Puedes contactarnos a través del formulario de consultas en esta pantalla.",
        "¿En donde puedo sacar mis documentos en caso de no tenerlos?": "Puedes ir a la sección 'Ayuda y Soporte' en el apartado de 'Documentos' ahí te ofrecen páginas para tus documentos faltantes"
    }

    ayuda_ventana = CTkToplevel()
    ayuda_ventana.title("Ayuda y Soporte")

    # Mostrar preguntas frecuentes
    CTkLabel(ayuda_ventana, text="Ayuda y Soporte", font=("Helvetica", 16, "bold")).pack(pady=10)
    CTkLabel(ayuda_ventana, text="Preguntas Frecuentes:", font=("Helvetica", 12, "bold")).pack(anchor='w', padx=10)
    for pregunta, respuesta in faqs.items():
        CTkLabel(ayuda_ventana, text=f"\n{pregunta}", font=("Helvetica", 10, "bold")).pack(anchor='w', padx=20)
        CTkLabel(ayuda_ventana, text=respuesta, wraplength=400).pack(anchor='w', padx=40)

    # Formulario de consultas
    CTkLabel(ayuda_ventana, text="\nFormulario de Consultas:", font=("Helvetica", 12, "bold")).pack(anchor='w', padx=10, pady=10)
    CTkLabel(ayuda_ventana, text="Nombre:").pack(anchor='w', padx=20)
    nombre_entry = CTkEntry(ayuda_ventana, width=300)
    nombre_entry.pack(anchor='w', padx=40)

    CTkLabel(ayuda_ventana, text="Correo electrónico:").pack(anchor='w', padx=20, pady=5)
    correo_entry = CTkEntry(ayuda_ventana, width=300)
    correo_entry.pack(anchor='w', padx=40)

    CTkLabel(ayuda_ventana, text="Describe tu consulta o problema:").pack(anchor='w', padx=20, pady=5)
    consulta_text = CTkTextbox(ayuda_ventana, width=300, height=100)
    consulta_text.pack(anchor='w', padx=40, pady=5)

    def enviar_consulta():
        nombre = nombre_entry.get()
        correo = correo_entry.get()
        consulta = consulta_text.get("1.0", tk.END).strip()
        if not nombre or not correo or not consulta:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return
        numero_ticket = "TICKET-" + str(hash(consulta) % 10000)
        enviar_correo(correo, numero_ticket)
        messagebox.showinfo("Consulta enviada",
                            f"Gracias {nombre}, su consulta ha sido enviada. Número de ticket: {numero_ticket}")
        ayuda_ventana.destroy()

    CTkButton(ayuda_ventana, text="Enviar Consulta", command=enviar_consulta).pack(pady=10)

def salir():
    ventana.quit()

# Crear la ventana principal
ventana = CTk()
ventana.title("Información")
ventana.geometry("600x480")
ventana.resizable(0, 0)

# Botón para mostrar información sobre documentación
btn_documentacion = CTkButton(ventana, text="Documentación", command=mostrar_informacion_documentacion)
btn_documentacion.pack(padx=10, pady=10)

# Botón para mostrar ayuda y soporte
btn_ayuda = CTkButton(ventana, text="Ayuda y Soporte", command=mostrar_ayuda)
btn_ayuda.pack(padx=10, pady=10)

# Botón para salir
btn_salir = CTkButton(ventana, text="Salir", command=salir)
btn_salir.pack(padx=10, pady=10)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
