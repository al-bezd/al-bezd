from django.db import models

# Create your models here.
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send(SUBJECT,mail_sender,password,mail_receiver,text):

    # Настройки
    #mail_sender = 'mail@gmail.com'
    #mail_receiver = 'mail@gmail.com'
    #mail_sender = 'mail@gmail.com'
    #password = '123fuckypu'
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # Формируем тело письма
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['Subject'] = Header(SUBJECT, 'utf-8')

        # Отпавляем письмо
        server.starttls()
        server.ehlo()
        server.login(mail_sender, password)
        server.sendmail(mail_sender, mail_receiver, msg.as_string())
        server.quit()
        return 'ok'
    except BaseException as err:
        return err
