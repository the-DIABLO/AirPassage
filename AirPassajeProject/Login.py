from tkinter import messagebox
from customtkinter import *
from PIL import Image
import re
import csv
import os
import subprocess

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def clear_error_labels():
    email_error_label.pack_forget()
    password_error_label.pack_forget()

def login():
    clear_error_labels()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    if not email and not password:
        email_error_label.configure(text="Ingrese sus datos")
        email_error_label.pack(anchor="w", pady=(5, 0), padx=(25, 0))
    elif not email:
        email_error_label.configure(text="Ingrese correo electrónico")
        email_error_label.pack(anchor="w", pady=(5, 0), padx=(25, 0))
    elif not validate_email(email):
        email_error_label.configure(text="Correo electrónico no válido")
        email_error_label.pack(anchor="w", pady=(5, 0), padx=(25, 0))
    elif not password:
        password_error_label.configure(text="Ingrese la contraseña")
        password_error_label.pack(anchor="w", pady=(5, 0), padx=(25, 0))
    else:
        csv_path = os.path.join(os.getcwd(), 'BaseDatos/registros.csv')
        usuario_encontrado = False
        with open(csv_path, mode='r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv, None)  # Saltar la cabecera si existe
            for fila in lector_csv:
                if email == fila[3] and password == fila[4]:
                    usuario_encontrado = True
                    break
        if usuario_encontrado:
            print("Iniciar sesión")
            app.destroy()  # Cierra la ventana actual
            subprocess.run(["python", "MenuPrincipal.py"])  # Ejecuta el script del menú principal
        else:
            messagebox.showwarning("Advertencia", "Usuario no registrado")
            print("No existe")

def show_login():
    for widget in frame.winfo_children():
        widget.destroy()

    CTkLabel(master=frame, text="Bienvenido", text_color="#0485ad", anchor="w", justify="left",
             font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(master=frame, text="Ingresa a tu cuenta", text_color="#0485ad", anchor="w", justify="left",
             font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="  Correo Electrónico:", text_color="#0485ad", anchor="w", justify="left",
             font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
    global email_entry
    email_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#0485ad", border_width=1,
                           text_color="#000000")
    email_entry.pack(anchor="w", padx=(25, 0))

    global email_error_label
    email_error_label = CTkLabel(master=frame, text="", text_color="red", anchor="w", justify="left", font=("Arial Bold", 10))
    email_error_label.pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="  Contraseña:", text_color="#0485ad", anchor="w", justify="left",
             font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    global password_entry
    password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#0485ad", border_width=1,
                              text_color="#000000", show="*")
    password_entry.pack(anchor="w", padx=(25, 0))

    global password_error_label
    password_error_label = CTkLabel(master=frame, text="", text_color="red", anchor="w", justify="left", font=("Arial Bold", 10))
    password_error_label.pack(anchor="w", padx=(25, 0))

    CTkButton(master=frame, text="Entrar", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=login).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    CTkButton(master=frame, text="Registrarse", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=show_register).pack(anchor="w", pady=(20, 0), padx=(25, 0))

def registrar_usuario():
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    correo = entry_correo.get().strip()
    contrasena = entry_contrasena.get().strip()
    confirmarc = entry_confirmacion_contrasena.get().strip()

    if not (nombre and apellido and correo and contrasena and confirmarc):
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    if contrasena != confirmarc:
        messagebox.showwarning("Advertencia", "Las contraseñas no coinciden")
        return

    if not validate_email(correo):
        messagebox.showwarning("Advertencia", "Correo electrónico no válido")
        return

    csv_path = os.path.join(os.getcwd(), 'BaseDatos/registros.csv')
    next_id = 1
    if os.path.exists(csv_path):
        with open(csv_path, mode='r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv, None)  # Saltar la cabecera si existe
            ids = [int(fila[0]) for fila in lector_csv]
            if ids:
                next_id = max(ids) + 1

    with open(csv_path, mode='a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        if next_id == 1:
            escritor_csv.writerow(["ID", "Nombre", "Apellido", "Correo", "Contraseña", "Confirmación"])  # Cabecera
        escritor_csv.writerow([next_id, nombre, apellido, correo, contrasena, confirmarc])

    messagebox.showinfo("Información", "Registro guardado exitosamente")
    show_login()

def show_register():
    for widget in frame.winfo_children():
        widget.destroy()

    CTkLabel(master=frame, text="Registro", text_color="#0485ad", anchor="w", justify="left",
             font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 5), padx=(25, 0))

    global entry_nombre, entry_apellido, entry_correo, entry_contrasena, entry_confirmacion_contrasena

    CTkLabel(master=frame, text="Nombre:", text_color="#0485ad", anchor="w", justify="left",
             font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    entry_nombre = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#0485ad", border_width=1,
                            text_color="#000000")
    entry_nombre.pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="Apellido:", text_color="#0485ad", anchor="w", justify="left",
             font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    entry_apellido = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#0485ad", border_width=1,
                              text_color="#000000")
    entry_apellido.pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="Correo Electrónico:", text_color="#0485ad", anchor="w", justify="left",
             font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    entry_correo = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#0485ad", border_width=1,
                            text_color="#000000")
    entry_correo.pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="Contraseña:", text_color="#0485ad", anchor="w", justify="left",
             font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    entry_contrasena = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#0485ad", border_width=1,
                                text_color="#000000", show="*")
    entry_contrasena.pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="Confirmación de Contraseña:", text_color="#0485ad", anchor="w", justify="left",
             font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    entry_confirmacion_contrasena = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#0485ad",
                                             border_width=1, text_color="#000000", show="*")
    entry_confirmacion_contrasena.pack(anchor="w", padx=(25, 0))

    CTkButton(master=frame, text="Registrar", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=registrar_usuario).pack(anchor="w", pady=(20, 0), padx=(25, 0))
    CTkButton(master=frame, text="Volver al Login", fg_color="#0485ad", hover_color="#5b94aa", font=("Arial Bold", 12),
              text_color="#ffffff", width=225, command=show_login).pack(anchor="w", pady=(10, 0), padx=(25, 0))

app = CTk()
app.geometry("600x480")
app.resizable(0, 0)

app.title("Login")
imagen_path = "Avion.ico"
app.iconbitmap(imagen_path)  # Cambia la ruta al archivo .ico de tu icono

side_img_data = Image.open("side-img.png")
email_icon_data = Image.open("email-icon.png")
password_icon_data = Image.open("password-icon.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

show_login()
app.mainloop()
