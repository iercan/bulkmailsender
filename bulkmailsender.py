import smtplib
from email.mime.text import MIMEText

with open("maillist.txt") as f:
        content = f.readlines()
maillist = [x.strip() for x in content]

with open("content.txt") as f:
    mailcontent = f.read()

msg = MIMEText(mailcontent, 'html')
me = 'mymail@mymail.com'
msg['Subject'] = 'My Subject'
msg['From'] = me

s = smtplib.SMTP('mail.mysmtpserver.com', 587)
s.login('mymail@mymail.com', 'mypassword')

for mail_addr in maillist:
    msg['To'] = mail_addr
    s.sendmail(me, [mail_addr], msg.as_string())
