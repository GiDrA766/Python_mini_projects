import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
FROM_EMAIL = "you email@gmail.com"  # Your Gmail email
PASSWORD = "you app password"
GMAIL_HOST = 'smtp.gmail.com'
GMAIL_PORT = 587

def concatenating(To: str, Subject: str, message: str):
    msg = mimeing(To, subject)
    msg.attach(MIMEText(message, 'plain'))
    return msg

def mimeing(To : str, Subject: str):
    msg = MIMEMultipart()
    msg['Subject'] = Subject
    msg['From'] = FROM_EMAIL
    msg['To'] = To
    return msg

def send(msg):
    try:
        smtp = smtplib.SMTP(GMAIL_HOST, GMAIL_PORT)
        smtp.starttls()
        smtp.login(FROM_EMAIL, PASSWORD)
        smtp.send_message(msg)
        smtp.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    to_email = "your@mail.ru"
    subject = "Test Email"
    message = "This is a test email sent from Python."
    
    email_msg = concatenating(to_email, subject, message)
    send(email_msg)
