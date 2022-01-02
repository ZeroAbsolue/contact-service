import smtplib
import ssl

from decouple import config

SMTP_HOST = config('SMTP_HOST')
SMTP_PORT = config('SMTP_PORT')
SMTP_USER = config('SMTP_USER')
SMTP_PASSWORD = config('SMTP_PASSWORD')


class Messenger:
    def __init__(self, sender, receiver, subject, message):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.message = message

    def __str__(self):
        return "from %s to %s subject %s message %s" % (self.sender, self.receiver, self.subject, self.message)

    def send_mail(self):
        msg = 'To: %s\nFrom: %s\nSubject: %s\n\nSender: %s\n\n%s' % (
            self.receiver, self.sender, self.subject, self.sender, self.message)
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(self.sender, [self.receiver], msg)
        server.quit()
