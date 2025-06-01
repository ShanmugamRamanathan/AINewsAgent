
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body):
    gmail_user = os.environ.get('GMAIL_USER')
    gmail_password = os.environ.get('GMAIL_APP_PASSWORD')
    gmail_recipient = os.environ.get('GMAIL_RECIPIENT')
    recipient = gmail_recipient  # Sending to self for demo purposes

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    text = msg.as_string()
    server.sendmail(gmail_user, recipient, text)
    server.quit()
