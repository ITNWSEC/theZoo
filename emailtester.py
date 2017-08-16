import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.Utils import formatdate

if len(sys.argv) != 6:
	print "Usage: emailtester.py [source email] [password] [SMTP server] [attachment] [destination email]"
	exit()

msg = MIMEMultipart()

mfrom = sys.argv[1]
mto = sys.argv[5]
mpassword = sys.argv[2]

msg['Subject'] = 'Test case'
msg['From'] = mfrom
msg['To'] = mto
msg['Date'] = formatdate()

# Open the file to scan in binary mode
fp = open(sys.argv[4], 'rb')
attachment = MIMEBase('application', 'octet-stream')
attachment.set_payload(fp.read())
encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', 'attachment; filename="filename"')
fp.close()
msg.attach(attachment)

# Send the email via your own SMTP server.
s = smtplib.SMTP(sys.argv[3], 587)
s.ehlo()
s.starttls()
s.login(mfrom, mpassword)
s.sendmail(mfrom, mto, msg.as_string())
s.quit()
