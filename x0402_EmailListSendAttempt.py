import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sqlite3
import sys
#sys.setdefaultencoding('utf8')

conn = sqlite3.connect('StriveDB2.db')
cursor = conn.cursor()
cur5 = cursor.execute('SELECT email FROM Sendr_Usr WHERE RadioB = "Funny"')
info5 = cur5.fetchall()

msg = MIMEMultipart()
msg['From'] = 'mkramer265@gmail.com'
msg['To'] = ', '.join(info5)
msg['Subject'] = 'Motivational'
message = 'test message'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('mkramer265@gmail.com', 'Celtics123')

mailserver.sendmail('mkramer265@gmail.com',info5,msg.as_string())

mailserver.quit()

connx = sqlite3.connect('StriveDB2.db')
cursorx = connx.cursor()
curx = cursorx.execute("INSERT INTO RIDX VALUES (?)", (k,))
connx.commit()
cursorx.close()
connx.close()


print(info5)

