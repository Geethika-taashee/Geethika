import smtplib
def send_email():
    try:
        sender_email="secondservicenow@gmail.com"
        receiver_email="geetika.a@taashee.com"
        password="wnimrequhmtmqnzp"
        subject="Python Test mail"
        body="This is a test mail sent from python! Dear students, your are having python test on next monday the link will be send you soon"
        message=f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()
            server.login(sender_email,password)
            server.sendmail(sender_email,receiver_email,message)
        print("Email sent successfull")
    except Exception as e:
        print(f"Error:{e}")
send_email()