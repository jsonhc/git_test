#coding=utf-8
import smtplib
from email.mime.text import MIMEText

from_mail = "xxxx@163.com"
to_mail = "xxxx@qq.com"
mail_passwd = "xxxx"

content = "this is the first python email"
subject = "mail test"
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = from_mail
msg['To'] = to_mail
try:
   s = smtplib.SMTP()
   s.connect('smtp.163.com')
   #s.starttls()
   s.login(from_mail,mail_passwd)
   s.sendmail(from_mail,to_mail,msg.as_string())
   print("OK")
except Exception as e:
   print(e)
finally:
   s.close()
