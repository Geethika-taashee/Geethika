import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender_email = "secondservicenow@gmail.com"
receiver_email = "geetika.a@taashee.com"
password = "wnimrequhmtmqnzp"
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "test Email from python"
body = "This is a test email sent using python."
msg.attach(MIMEText(body,'plain'))
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
server.sendmail(sender_email,receiver_email,msg.as_string())
server.quit()
print("Email sent successfully")