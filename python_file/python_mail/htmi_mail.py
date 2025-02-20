import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender_email = "secondservicenow@gmail.com"
receiver_email = "geetika.a@taashee.com"
password = "wnimrequhmtmqnzp"
smtp_server="smtp.gmail.com"
smtp_port=587
message=MIMEMultipart()
message['From']=sender_email
message['To']=receiver_email
message['Subject']="Test HTML Email"
html_content="""
<html>
  <body>
    <h1>This is a test email</h1>
    <p style="color:blue;">Hello, this is an <b>HTML</b> email sent from Python!</p>
  </body>
</html>
"""
message.attach(MIMEText(html_content,'html'))
try:
    server=smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string())
    print("Email sent successfully")
except Exception as e:
    print(f"Error : {e}")
finally:
    server.quit()