import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sqlite3
import sys
#sys.setdefaultencoding('utf8')

conn = sqlite3.connect('StriveDB2.db')
cursor = conn.cursor()
cur2 = cursor.execute('SELECT msg, RecordID FROM Motivational ORDER BY RANDOM() LIMIT 1;')
info2 = cur2.fetchone()

#msg
j = info2[0]
#recordID
k = info2[1]

msg = MIMEMultipart()
msg['From'] = 'mkramer265@gmail.com'
msg['To'] = 'mkramer789@gmail.com'
msg['Subject'] = 'Motivational'
message = j
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('mkramer265@gmail.com', 'pw')

mailserver.sendmail('mkramer265@gmail.com','mkramer789@gmail.com',msg.as_string())

mailserver.quit()

connx = sqlite3.connect('StriveDB2.db')
cursorx = connx.cursor()
curx = cursorx.execute("INSERT INTO RIDX VALUES (?)", (k,))
connx.commit()
cursorx.close()
connx.close()
