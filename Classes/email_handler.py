from sendgrid.helpers.mail import Mail
import requests
import sys

class EmailHandler:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_email(self,recipient_email, subject, message, ):
        response = requests.post(
            "https://api.mailgun.net/v3/sandboxa6abf275944d4d81871900ed51fba9b2.mailgun.org/messages",
            auth=("api", ""),
            data={"from": "Mailgun Sandbox <postmaster@sandboxa6abf275944d4d81871900ed51fba9b2.mailgun.org>",
                "to": recipient_email,
                "subject": subject,
                "text": message})

        if response.status_code == 200:
            print('Email successfully sent!')
            sys.exit()
            #shutdown windows
            
        else:
            print(f'Failed to send email. Status code: {response.status_code}. Response: {response.text}')



