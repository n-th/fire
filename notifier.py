import smtplib
from email.mime.text import MIMEText


def notify(data,email):

    # conexão com os servidores do google
    host = 'smtp.gmail.com'
    port = 465
    # username ou email para logar no servidor
    username = 'spaceapps.saci@gmail.com'
    password = 'curupira'

    from_addr = 'spaceapps.saci@gmail.com'
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
