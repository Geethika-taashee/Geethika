import smtplib
li=["geetika.a@taashee.com","geethikaamadagani@gmail.com"]
for dest in li:
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("secondservicenow@gmail.com","wnimrequhmtmqnzp")
    message="""\
Subject: Python Team
Hello, welcome to python development team 
"""
    s.sendmail("secondservicenow@gmail.com",dest,message)
    print("Email sent successfully")
    s.quit()