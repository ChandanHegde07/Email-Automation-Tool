import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import schedule
import time

# CONFIGURATION
SENDER_EMAIL = "youremail@gmail.com"
PASSWORD = "your password"   # Use App Password from Google Account
SUBJECT = "Event Reminder"


# FUNCTION: Send Email
def send_email(name, receiver_email):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = SUBJECT

    with open("message.txt", "r") as f:
        body = f.read().format(name=name)

    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {name} ({receiver_email})")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")


# FUNCTION: Send to all
def send_bulk_emails():
    contacts = pd.read_csv("contacts.csv")
    for _, row in contacts.iterrows():
        send_email(row['Name'], row['Email'])

# OPTIONAL: Schedule emails
# Send emails every day at 9 AM
# schedule.every().day.at("09:00").do(send_bulk_emails)

if __name__ == "__main__":
    send_bulk_emails()
