from fastapi import APIRouter

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

router = APIRouter()


@router.post("/reset-password/")
def reset_password(email: str, email_sender: str, email_password: str):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Destinatário do email
    email_receiver = email

    # Construindo o email
    subject = "Recuperação de senha"
    body = "Infelizmente"

    msg = MIMEMultipart()
    msg["From"] = email_sender
    msg["To"] = email_receiver
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    # Conexão com o servidor SMTP
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_sender, email_password)
        text = msg.as_string()
        server.sendmail(email_sender, email_receiver, text)
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o email: {e}")

    # Fechar conexão com o servidor SMTP
    server.quit()

    return {"message": "reseted sucesfully"}
