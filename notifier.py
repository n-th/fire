import smtplib
from email.mime.text import MIMEText


def notify(data,email):
    # servidores do google
    host = 'smtp.gmail.com'
    port = 465
    # username ou email para logar no servidor
    username = 'spaceapps.saci@gmail.com'
    password = 'curupira'

    from_addr = 'spaceapps.saci@gmail.com'
    to_addrs = [email]

    message = MIMEText('Atenção!\nIdentificamos um foco de incêndio em sua cidade na seguinte localização (%s, %s).\nPara mais informações, acesse: <link_maps>.\nDados obtidos via Nasa-FIRMS(Informações sobre incêndio para sistema de gerenciamento de recursos). \n\nEquipe Saci - Nasa Space Apps'% (data[0],data[1])) 
    message['subject'] = 'Atenção cidade de %s-%s' % (data[2],data[3])
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(host, port)
    # login servidor externo
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()
