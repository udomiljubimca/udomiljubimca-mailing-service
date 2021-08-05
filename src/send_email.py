import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
class EmailToSend():
    def __init__(self, reciver_email, message, title):
        self.title = title
        self.reciver_email = reciver_email
        self.message = message
    def send(self):
        sender_email = os.getenv('EMAIL')
        sender_password = os.getenv('PASSWORD')
        smtp_host = os.getenv('SMTP_HOST')
        smtp_port = os.getenv('SMTP_PORT')
        from_addr = sender_email
        to = self.reciver_email  

        msg = MIMEMultipart()
        msg["from_addr"] = from_addr
        msg["to"] = to 
        msg["Subject"] = self.title

        body = self.message
        msg.attach(MIMEText(body, "Plain"))

        server = smtplib.SMTP(smtp_host, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(from_addr, to, text)
        return {"email_sended": True}
