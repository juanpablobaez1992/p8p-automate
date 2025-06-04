import smtplib
from email.message import EmailMessage


def ejecutar(entrada):
    params = entrada.get('params', {})
    smtp_server = params.get('smtp_server', 'localhost')
    smtp_port = params.get('smtp_port', 25)
    remitente = params.get('remitente')
    destinatario = params.get('destinatario')
    asunto = params.get('asunto', '')
    cuerpo = params.get('cuerpo', '')

    if not remitente or not destinatario:
        raise ValueError('Faltan direcciones de correo')

    msg = EmailMessage()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.set_content(cuerpo)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.send_message(msg)

    return {'enviado': True}
