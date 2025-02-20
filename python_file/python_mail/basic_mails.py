# import smtplib
# s=smtplib.SMTP("smtp.gmail.com",587)
# s.starttls()
# s.login("secondservicenow@gmail.com","wnimrequhmtmqnzp")
# message="hello,welcome to python"
# s.sendmail("secondservicenow@gmail.com","geetika.a@taashee.com",message)
# print("mail sent successfully")
# s.quit()



import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.ehlo()
s.starttls()
s.login("secondservicenow@gmail.com","wnimrequhmtmqnzp")
message = """\
Subject: Python Mail
Hello, Gd morning, Welcome to python mail 
"""
s.sendmail("secondservicenow@gmail.com","geetika.a@taashee.com",message)
print("mail sent successfully")
s.quit()