import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')

conn = sqlite3.connect('StriveDB2.db')
cursor = conn.cursor()
cur5 = cursor.execute('SELECT email FROM Sendr_Usr WHERE RadioB = "Funny"')
info5 = cur5.fetchall()


for x in info5:
	print(x)

