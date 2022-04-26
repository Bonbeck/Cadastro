import smtplib, ssl, json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSenha():
  def __init__(self, destinatario):
    with open("token.json", "r") as token:
      self.TOKEN = json.load(token)

    self.sender_email = "matheus.aulas.python@gmail.com"
    self.receiver_email = destinatario
    self.password = self.TOKEN["email"]

  def envia(self, codigo):
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = self.sender_email
    message["To"] = self.receiver_email

    # Create the plain-text and HTML version of your message
    text = f"""\
    ola,
    sua conta excedeu o limite de tentativas de login, para utiliza-la copie o codigo abaixo:
    {codigo}"""
    html = f"""\
    <html>
      <body>
        <p>ola,<br>
          sua conta excedeu o limite de tentativas de login, para utiliza-la copie o codigo abaixo:<br>
          {codigo}
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(self.sender_email, self.password)
        server.sendmail(
            self.sender_email, self.receiver_email, message.as_string()
        )
    return print("o e-mail foi enviado com o codigo para sua conta")