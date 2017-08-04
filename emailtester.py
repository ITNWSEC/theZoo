import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.Utils import formatdate

if len(sys.argv) != 3:
	print "Usage: emailtester.py [source email] [password] [attachment] [destination email]"
	exit()

msg = MIMEMultipart()

mfrom = sys.argv[1]
mto = sys.argv[4]
mpassword = sys.argv[2]

msg['Subject'] = 'Test case'
msg['From'] = mfrom
msg['To'] = mto
msg['Date'] = formatdate()

# Open the file to scan in binary mode
fp = open(sys.argv[3], 'rb')
attachment = MIMEBase('application', 'octet-stream')
attachment.set_payload(fp.read())
encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', 'attachment; filename="filename"')
fp.close()
msg.attach(attachment)

# Send the email via your own SMTP server.
s = smtplib.SMTP('smtp.outlook.com', 587)
s.ehlo()
s.starttls()
s.login(mfrom, mpassword)
s.sendmail(mfrom, mto, msg.as_string())
s.quit()
