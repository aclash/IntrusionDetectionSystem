import smtplib
from_email = 'aclash2009@gmail.com'
recipients_list = ['aclash@163.com']
cc_list = []
subject = 'Hello python'
message = 'This is a python test message'
username = 'xxxxxx'
password = 'xxxxxx'
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
    server.quit()

students = { '1': {'name': 'Bob', 'grade': 10}, '2': {'name': 'Ana', 'grade': 20}}
def averageGrade(students):
    sum = 0.0
    for key in students:
        sum = sum + students[key]['grade']
    average = sum / len(students)
    return average

avg = averageGrade(students)
print("The value is %0.2f" % (avg))

class Student:
    studentCnt = 0
    def __init__(self, name, id):
        print("constructor.")
        self.name = name
        self.id = id
        self.grades = {'math': '99'}
        Student.studentCnt = Student.studentCnt + 1

    def __del__(self):
        print("destructor")

    def getStudentCnt(self):
        return Student.studentCnt

    def addGrade(self, key, value):
        self.grades[key] = value

    def getGrade(self, key):
        return self.grades[key]

    def printGrades(self):
        for key in self.grades:
            print(key + ": " + self.grades[key])

s = Student('zhang', '99')
s.addGrade('art', '99')
s.addGrade('sport', '98')
s.printGrades()
sendemail(from_email, recipients_list, cc_list, subject, message, username, password, smptserver)
