#!/usr/bin/python
import smtplib
import email.mime.text
import sys

## python bulkMailer.py <name_Of_File_With_Receiver's_EmailID_List><name_Of_File_With_Actual_Message_of_Email><Subject_Of_Email>
# allow less secure Apps to access your Gmail Account
# Gmail -> My Account -> Sign-in & Security -> Allow less secure Apps: ON
sender = 'username' # provide Gmail ID
password = 'password' # provide  Gmail password

receipientList = sys.argv[1]
actualMessageFile = sys.argv[2]
subjectOfMail = sys.argv[3]

with open(receipientList, 'r') as fp:
	receivers = fp.read().split()

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

with open(actualMessageFile, 'r') as fp:
	message = email.mime.text.MIMEText(fp.read())
	message['subjectOfMail'] = subjectOfMail

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.set_debuglevel(True)

server.ehlo()
if server.has_extn('STARTTLS'):
	server.starttls()
	server.ehlo()

server.login(sender, password)

for receiver in receivers:
	server.sendmail(sender, receiver, message.as_string())

server.quit()
