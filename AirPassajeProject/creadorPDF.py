import jinja2
import pdfkit
import os
import correo
"""
nombre = "Ari"
apellido = "Ceron"
numTicket = "123123123"
Clase = "223423432"
NumVuelo ="123"
Origen = "aaaa"
Destino = "ffffff"
HoraSalida ="12:23"
HoraLlegada ="23:12"
NumAsiento = "A1"
"""

def crea_pdf(ruta_template, info, rutacss=''):
    try:
        nombre_template = os.path.basename(ruta_template)
        ruta_template_dir = os.path.dirname(ruta_template)

        env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template_dir))
        template = env.get_template(nombre_template)
        html = template.render(info)

        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'utf-8',
            'enable-local-file-access': ''
        }

        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        ruta_salida = 'C:/Users/Roy/Documents/TópicosdeDesarrollodeSistemas/Python/PyCharmProyects/AirPassajeProject1)/AirPassajeProject/'+nombreA
        pdfkit.from_string(html, ruta_salida, css=rutacss, options=options, configuration=config)

    except Exception as e:
        print(f"Error: {e}")

def EnviarCorreoConPDF(nombre, apellido, numTicket, Clase, NumVuelo, Origen, Destino, HoraSalida, HoraLlegada, NumAsiento, CorreoDestino):
    ruta_template = 'C:/Users/Roy/Documents/TópicosdeDesarrollodeSistemas/Python/PyCharmProyects/AirPassajeProject1)/AirPassajeProject/AirPassajeProject/template.html'
    rutacss = 'C:/Users/Roy/Documents/TópicosdeDesarrollodeSistemas/Python/PyCharmProyects/AirPassajeProject1)/AirPassajeProject/estilos.css'
    info = {"Nombre": nombre, "Apellido": apellido, "NumTicket": numTicket, "Clase": Clase, "NumVuelo": NumVuelo,
            "Origen": Origen, "Destino": Destino, "HoraSalida": HoraSalida, "HoraLlegada": HoraLlegada,
            "NumAsiento": NumAsiento}
    global nombreA
    nombreA= nombre+" Voucher.pdf"
    crea_pdf(ruta_template, info, rutacss)
    correo.enviaCorreo(CorreoDestino, nombreA)
