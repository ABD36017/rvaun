#python sending mail
import smtplib

sender = 'varunr1730@gmail.com'
receivers = 'rvarun1730@gmail.com'

password = 'varun08042000'
smtpserver=smtplib.SMTP("smtp.gmail.com,587")
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login('varunr1730@gmail.com,varun08042000')
msg='subject:Demo\nthis is a demo'
smtpserver.sendmail('varunr1730@gmail.com,rvarun1730@gmail.com,hello')
print('sent')
smtpserver.close()



