import cv2
import smtplib
import time
from_email = 'aclash2009@gmail.com'
recipients_list = ['aclash@163.com']
cc_list = []
subject = 'Hello python'
message = 'This is a python test message'
username = 'xxx'
password = 'xxx'
smptserver = 'smtp.gmail.com:587'
def sendemail(from_email, recipients_list, cc_list, subject, message, username, password, smptserver):
    header = 'From: %s\n' % from_email
    header += 'To: %s\n' % ','.join(recipients_list)
    header += 'Cc: %s\n' % ','.join(cc_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
    server = smtplib.SMTP(smptserver)
    server.starttls()
    server.login(username, password)
    problems = server.sendmail(from_email, recipients_list, message)
    print("sending")
    server.quit()

def takePicture():
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    timeStamp = time.time()
    cv2.imwrite('Intrusion' + str(timeStamp) + '.jpg', frame)
    cap.release()
    cv2.destroyAllWindows()

takePicture()
#sendemail(from_email, recipients_list, cc_list, subject, message, username, password, smptserver)
