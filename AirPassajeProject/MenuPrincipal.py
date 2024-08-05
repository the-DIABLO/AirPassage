import customtkinter as ctk
from PIL import Image
import subprocess



class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Menú Principal")
        self.geometry("698x490")

        # Configuración de CustomTkinter
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Configuración del color de fondo
        self.configure(bg="#e8eff3")

        # Frame del menú lateral
        self.menu_frame = ctk.CTkFrame(self, width=180, corner_radius=10, fg_color="#e8eff3")
        self.menu_frame.grid(row=0, column=0, sticky="nswe")

        # Frame de contenido principal
        self.content_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#f5f9fd")
        self.content_frame.grid(row=0, column=1, sticky="nswe")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Crear botones del menú en el orden especificado
        self.create_menu_button("Vuelos", self.show_search_flight)
        self.create_menu_button("Estado del Vuelo", self.show_flight_status)
        self.create_menu_button("Ayuda y Soporte", self.show_help_support)
        self.create_menu_button("Cerrar Sesión", self.exit_application)

        # Cargar imagen
        self.original_image = Image.open("LogoAirPassage.png")
        self.logo_image = ctk.CTkImage(self.original_image, size=(400, 300))

        # Mostrar imagen en el frame de contenido principal
        self.content_label = ctk.CTkLabel(self.content_frame, text="", image=self.logo_image)
        self.content_label.pack(expand=True)

        # Vincular evento de redimensionado
        self.content_frame.bind("<Configure>", self.resize_image)

    def create_menu_button(self, text, command):
        button = ctk.CTkButton(self.menu_frame, text=text, command=command, width=180, height=40, corner_radius=10)
        button.pack(pady=10, padx=10)

    def show_search_flight(self):
        try:
            result = subprocess.run(["python", "Vuelos.py"], capture_output=True, text=True)
            output = result.stdout
            self.update_content_label(output)
        except Exception as e:
            self.update_content_label(f"Error al ejecutar el script: {e}")

    def show_flight_status(self):
        self.update_content_label("Cargando Estado del Vuelo...")
        self.run_flight_status_script()

    def show_help_support(self):
        self.update_content_label("Cargando Ayuda y Soporte...")
        self.run_help_support_script()

    def show_payment_history(self):
        self.update_content_label("Cargando Historial de Pagos...")
        self.run_payment_history_script()

    def exit_application(self):
        self.destroy()
        subprocess.Popen(["python", "Login.py"])

    def update_content_label(self, text):
        self.content_label.configure(text=text, image=None)

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.original_image.resize((new_width, new_height), Image.LANCZOS)
        self.logo_image = ctk.CTkImage(resized_image, size=(new_width, new_height))
        self.content_label.configure(image=self.logo_image)

    def run_help_support_script(self):
        try:
            result = subprocess.run(["python", "AyudaSoporteDoc.py"], capture_output=True, text=True)
            output = result.stdout
            self.update_content_label(output)
        except Exception as e:
            self.update_content_label(f"Error al ejecutar el script: {e}")

    def run_payment_history_script(self):
        try:
            result = subprocess.run(["python", "HistorialP.py"], capture_output=True, text=True)
            output = result.stdout
            self.update_content_label(output)
        except Exception as e:
            self.update_content_label(f"Error al ejecutar el script: {e}")

    def run_profile_management_script(self):
        try:
            result = subprocess.run(["python", "GestionPerfil.py"], capture_output=True, text=True)
            output = result.stdout
            self.update_content_label(output)
        except Exception as e:
            self.update_content_label(f"Error al ejecutar el script: {e}")

    def run_search_flight_script(self):
        try:
            result = subprocess.run(["python", "Vuelos.py"], capture_output=True, text=True)
            output = result.stdout
            self.update_content_label(output)
        except Exception as e:
            self.update_content_label(f"Error al ejecutar el script: {e}")

    def run_check_in_script(self):
        try:
            result = subprocess.run(["python", "Checkin.py"], capture_output=True, text=True)
            output = result.stdout
            self.update_content_label(output)
        except Exception as e:
            self.update_content_label(f"Error al ejecutar el script: {e}")

    def run_flight_status_script(self):
        try:
            result = subprocess.run(["python", "EstadoVuelo.py"], capture_output=True, text=True)
            output = result.stdout
            self.update_content_label(output)
        except Exception as e:
            self.update_content_label(f"Error al ejecutar el script: {e}")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
