#coding=utf-8
import smtplib, sys
from email.mime.text import MIMEText


#from_mail = "xxxx@163.com"
#to_mail = "xxxx@qq.com"
#mail_passwd = "xxxxxx"

content = "this is the first python email"
subject = "mail test"
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = sys.argv[1]
msg['To'] = sys.argv[3]
try:
   s = smtplib.SMTP()
   s.connect('smtp.163.com')
   s.login(sys.argv[1],sys.argv[2])
   s.sendmail(sys.argv[1],sys.argv[3],msg.as_string())
   print("OK")
except Exception as e:
   print(e)
finally:
   s.close()
