from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email="dev.singh@live.com"
    from_password="d5twosix"
    to_email=email

    subject="Height data"
    message="Hi, your height is <strong>%s</strong>. Average height of all users is <strong>%s</strong> and that is calculated out of <strong>%s</strong> users." %(height,average_height, count)

    msg=MIMEText(message, 'html')

    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    live=smtplib.SMTP('smtp-mail.outlook.com', 587)
    live.ehlo()
    live.starttls()
    live.login(from_email, from_password)
    live.send_message(msg)
