from Actions.action import Action
from email_handler import EmailHandler
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Actions.action import Action
import time
from dotenv import load_dotenv
import os

class SendEmailAction(Action):
    def __init__(self,delay=0.1, subject="Captcha detected", body=" ", to_email="", from_email="rokemailsendertest@gmail.com", from_password="prtnezkgfevwihok", smtp_server='smtp.gmail.com', smtp_port=587):
        self.subject = subject
        self.body = body
        self.to_email = to_email
        self.from_email = from_email
        self.from_password = from_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.delay = delay

    def execute(self):
        load_dotenv()
        time.sleep(self.delay)
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = os.getenv('EMAIL')
        msg['Subject'] = self.subject + " " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        msg.attach(MIMEText(self.body, 'plain'))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.from_email, self.from_password)
        text = msg.as_string()
        server.sendmail(self.from_email, self.to_email, text)
        server.quit()
        return True
