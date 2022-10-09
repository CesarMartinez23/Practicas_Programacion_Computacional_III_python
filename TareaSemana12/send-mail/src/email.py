from smtplib import SMTP
from os import getenv
from typing import List, Optional
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create a class to send emails


class Email():

    # Create construction function
    def __init__(self):
        self.server = SMTP(
            host=getenv('SMTP_HOSTNAME'),
            port=getenv('SMTP_TSL_PORT'),
        )

    # Create a function to connect to the server of gmail with the credentials of the .env file
    def connectServer(self):
        self.server.starttls()
        self.server.login(
            user=getenv('SMTP_EMAILUSER'),
            password=getenv('SMTP_PASSWORD'),
        )

# Create a function to send email with the data from the GUI form Tkinter.
    def sendEmail(self, emails: List[str], subject: Optional[str], **kwargs):
        self.connectServer()
        print('Sending email...')
        for email in emails:
            mime = MIMEMultipart()
            mime['From'] = getenv('SMTP_EMAILUSER')
            mime['To'] = email
            mime['Subject'] = subject
            emailBody = MIMEText(kwargs['message_format'], kwargs['format'])
            mime.attach(emailBody)
            try:
                self.server.sendmail(
                    getenv('SMTP_EMAILUSER'),
                    email,
                    mime.as_string()
                )
            except Exception as e:
                raise e
            finally:
                print('Finished sending email.')
                self.disconectServer()

    # El metodo disconectServer() se encarga de desconectarse del servidor de correo de gmail.
    def disconectServer(self):
        self.server.quit()
        self.server.close()
