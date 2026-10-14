import smtplib
from email.message import EmailMessage
from pathlib import Path

from config import SMTP_EMAIL, SMTP_PASSWORD
from exceptions.smtp import SmtpError


def send_confirmation(email: str) -> None:
    msg = EmailMessage()
    msg["Subject"] = "Bem-vindo(a) à nossa comunidade - Lumen"
    msg["From"] = SMTP_EMAIL
    msg["To"] = email

    msg.set_content(
        "É um prazer ter você com a gente!\n"
        "Agradecemos por assinar nossa newsletter. 💜\n\n"
        "A partir de agora, você receberá nossas novidades, "
        "conteúdos e atualizações diretamente no seu e-mail.\n"
        "Esperamos que nossos conteúdos sejam úteis e interessantes "
        "para você!\n"
        "Obrigado por fazer parte da nossa comunidade. "
        "Juntos trilharemos seu destino! 🚀"
    )

    image_path = (
        Path(__file__).resolve().parent.parent / "assets" / "welcome_newsletter.png"
    )

    try:
        with image_path.open("rb") as image:
            msg.add_attachment(
                image.read(),
                maintype="image",
                subtype="png",
                filename="welcome_newsletter.png",
            )

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.send_message(msg)

    except (smtplib.SMTPException, OSError) as e:
        raise SmtpError() from e
