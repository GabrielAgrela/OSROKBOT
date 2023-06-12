from Actions.action import Action
from email_handler import EmailHandler

class EmailAction(Action):
    def __init__(self, email_handler: EmailHandler, recipient_email: str, subject: str, message: str):
        self.email_handler = email_handler
        self.recipient_email = recipient_email
        self.subject = subject
        self.message = message

    def execute(self):
        try:
            self.email_handler.send_email(self.recipient_email, self.subject, self.message)
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
