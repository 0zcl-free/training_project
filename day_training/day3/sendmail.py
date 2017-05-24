

def sendmail():
    import  smtplib
    from email.mime.text import MTMEText
    from email.utils import formataddr

    msg = MIMEText('邮件内容', 'plain', 'utf-8')
    msg['From'] = formataddr(['zcl','1274828542@qq.com'])
    map['To'] = formataddr(['走人','1274828542@qq.com'])
    msg['Subject'] = '主题'

    server = smtplib.SMTP('smtp.qq.com',25)
    server.login('1274828542@qq.com','')
    server.sendmail('1274828542@qq.com',['1274828542@qq.com',],msg.as_string())
    server.quit()

sendmail()