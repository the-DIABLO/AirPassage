import smtplib
import email.mime.multipart
import email.mime.base
import os
from email.mime.text import MIMEText

def enviaCorreo(CorreoDestino, nombreArchivo):
    # Crea la conexión SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)

    correo = 'AirPassageSystem@gmail.com'
    pas = 'tbjv ycyr xcrd ecsf'
    # Inicia sesión en tu cuenta de Gmail
    server.starttls()

    server.login(correo, pas)

    # Definir el remitente y destinatario del correo electrónico
    remitente = "AirPassageSystem@gmail.com"
    destinatario = CorreoDestino

    # Crear el mensaje del correo electrónico
    mensaje = email.mime.multipart.MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = "AIR PASSAGE SYSTEM"

    # Añadir el cuerpo del mensaje
    cuerpo = "Hola,\n\nGracias por reservar tu vuelo, en este correo adjuntamos tu boleto.\n\nSaludos"
    mensaje.attach(email.mime.text.MIMEText(cuerpo, 'plain'))

    # Añadir el archivo Excel como adjunto
    ruta_archivo = nombreArchivo
    archivo = open(ruta_archivo, 'rb')
    adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
    adjunto.set_payload((archivo).read())
    email.encoders.encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo)
    mensaje.attach(adjunto)

    # Convertir el mensaje a texto plano
    texto = mensaje.as_string()

    # Enviar el correo electrónico
    server.sendmail(remitente, destinatario, texto)

    # Cerrar la conexión SMTP
    server.quit()