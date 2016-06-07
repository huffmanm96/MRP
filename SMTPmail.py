import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

def send_mail( send_from, send_to, subject, text, files=[], server="smtp.mandrillapp.com", port=587, username='MI GOP', password='iAsVYyyk9MxJr11GZLmkKw', isTls=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"r").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if isTls: smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

from datetime import datetime
now = datetime.now()

(now.month, now.day, now.year, now.hour, now.minute, now.second)
send_mail('dnormile@migop.org','berneyja@msu.edu',(('Absentee Distribution List %s/%s/%s %s:%s:%s') % (now.month, now.day, now.year, now.hour, now.minute, now.second))," ",['/Users/maddiehuffman/Desktop/broken/MD/MRPmailNEW.csv'])