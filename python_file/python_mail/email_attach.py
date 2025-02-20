import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def send_email_with_attachment():
    try:
        sender_email="secondservicenow@gmail.com"
        receiver_email="geetika.a@taashee.com"
        password="wnimrequhmtmqnzp"
        subject="Test email with attachment"
        body="This is a test email sent with an attachment from python."
        attachment_path="/home/geethika/Documents/python_file/example_new.txt"
        msg=MIMEMultipart()
        msg['From']=sender_email
        msg['To']=receiver_email
        msg['Subject']=subject
        msg.attach(MIMEText(body,'plain'))
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')
            msg.attach(part)
        with smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()
            server.login(sender_email,password)
            server.sendmail(sender_email,receiver_email,msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error:{e}")
send_email_with_attachment()
