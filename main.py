import cv2
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import smtplib
import serial
import time
#ser = serial.Serial('/dev/ttyUSB0', 9600)
from_email = 'aclash2009@gmail.com'
recipients_list = ['aclash@163.com', 'czhang23@horizon.csueastbay.edu']
cc_list = []
subject = 'Intrusion Detected!!!'
message = 'Intrusion Detected! Please click on the link below for more information.'
username = 'XXX'
password = 'XXX'
smptserver = 'smtp.gmail.com:587'
serverIP = '74.207.251.237'
db_name = 'IntrusionDB'
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
    timeStamp = time.localtime()
    picName = 'Intrusion' + str(timeStamp) + '.jpg'
    cv2.imwrite(picName, frame)
    cap.release()
    cv2.destroyAllWindows()
    timeStamp = time.strftime("%Y-%m-%d %H:%M:%S", timeStamp)
    timeStamp = str(timeStamp)
    print (timeStamp)
    insertBLOB(timeStamp, picName)
    sendemail(from_email, recipients_list, cc_list, subject, message, username, password, smptserver)

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertFuck(timeStamp, photo):
    print("Inserting BLOB into intrusionDB table")
    db = mysql.connector.connect(host = serverIP, database = db_name, user = 'root', password = password)
    try:
        cursor = db.cursor(prepared = True)
        sql_insert_blob_query = """ INSERT INTO `IntrusionData` (`time`, `picture`) VALUES (%s,%s)"""
        empPicture = convertToBinaryData(photo)
        # Convert data into tuple format
        insert_blob_tuple = (timeStamp, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        db.commit()
        print ("Image inserted successfully as a BLOB into IntrusionData table", result)
    except mysql.connector.Error as error:
        db.rollback()
        print("Failed inserting BLOB data into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(db.is_connected()):
            cursor.close()
            db.close()
            print("MySQL connection is closed")

def insertBLOB(timeStamp, photo):
    print("Inserting BLOB into intrusionDB table")
    db = mysql.connector.connect(host = serverIP, database = db_name, user = 'root', password = password)
    try:
        cursor = db.cursor(prepared = True)
        sql_insert_blob_query = """ INSERT INTO `IntrusionData` (`time`, `picture`) VALUES (%s,%s)"""
        empPicture = convertToBinaryData(photo)
        # Convert data into tuple format
        insert_blob_tuple = (timeStamp, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        db.commit()
        print ("Image inserted successfully as a BLOB into IntrusionData table", result)
    except mysql.connector.Error as error:
        db.rollback()
        print("Failed inserting BLOB data into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(db.is_connected()):
            cursor.close()
            db.close()
            print("MySQL connection is closed")

takePicture()

