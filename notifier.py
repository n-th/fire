import smtplib
from email.mime.text import MIMEText

import credentials

consumer_secret = credentials.login['consumer_secret']

def notify(data,email):

    # conexão com os servidores do google
    host = 'smtp.gmail.com'
    port = 465
    # username ou email para logar no servidor
    username = consumer_secret['username']
    password = consumer_secret['password']

    from_addr = username
    to_addrs = [email]

    message = MIMEText('Hello World')
    message['subject'] = 'Hello'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(host, port)
    # para interagir com um servidor externo precisaremos
    # fazer login nele
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()
