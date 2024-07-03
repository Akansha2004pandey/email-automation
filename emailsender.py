from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
load_dotenv()
import smtplib
import os
import schedule
import time


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'abc@gmail.com'
smtp_password = os.getenv('SMTP_PASSWORD')  


from_address = 'abc@gmail.com'
to_address = 'xyz@gmail.comS'
subject = 'Application for Internship'
body = '''Dear Mam,

I am writing to apply for the internship position at your company. Please find my resume attached.

Best regards,
Akansha'''


msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
filename = 'resume.pdf'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'pdf')  
part.set_payload(attachment.read())
attachment.close()
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
msg.attach(part)
def send_email():
    try:

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(smtp_user, smtp_password)
        text = msg.as_string()  
        server.sendmail(from_address, to_address, text)
        server.quit()  
        print(f'Email sent to {to_address}')
    except Exception as e:
        print(f'Failed to send email: {e}')

def send_emails_to_all():
    send_email()


schedule.every().day.at("13:19").do(send_emails_to_all) 

while True:
    schedule.run_pending()
    time.sleep(1) 
