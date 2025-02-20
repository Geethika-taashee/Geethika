import smtplib
content="Hello World"
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
sender="secondservicenow@gmail.com"
password="wnimrequhmtmqnzp"
mail.login(sender,password)
recipient="geetika.a@taashee.com"
subject="Test Email"
header = f'To: {recipient}\nFrom: {sender}\nSubject: {subject}\n'
content = header + content
mail.sendmail(sender,recipient,content)
print("Email sent successfully")
mail.quit()