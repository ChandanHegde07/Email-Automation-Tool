text
# Email Automation Tool

## Overview
The Email Automation Tool allows users to send customized bulk emails to a list of recipients stored in a CSV file. The tool uses SMTP to send emails and supports HTML email templates, attachments, and scheduled email sending. This is a simple and powerful Python-based tool for automating the process of email outreach, reminders, or notifications.

## Features
* **Bulk email sending** from a CSV file of email addresses
* **Customizable email templates** with dynamic placeholders (e.g., recipient names)
* Supports **sending attachments** with the email
* **Scheduled email sending** to automate email dispatch at specific times
* **Easy-to-use**: Modify only the configuration file and CSV data

## Requirements
* Python 3.x
* Install dependencies with:
    pip install pandas schedule


## Project Structure
email_automation/
│
├── send_email.py # Main script to send emails
├── contacts.csv # List of contacts with name and email
├── message.txt # Email message template
└── .gitignore # Git ignore file


* `send_email.py`: The script to send emails to all contacts in the contacts.csv file
* `contacts.csv`: Contains the list of recipients with their names and email addresses
* `message.txt`: Email message template with placeholders for dynamic content (like recipient's name)

## Setup

1. **Clone the repository:**
git clone https://github.com/yourusername/email-automation-tool.git
cd email-automation-tool


2. **Install required dependencies:**
pip install pandas schedule


3. **Configure Email Settings:**
In the `send_email.py` file, set your email and password.
SENDER_EMAIL = "youremail@gmail.com"
PASSWORD = "your_app_password" # Use App Password (Gmail) or SMTP password for other providers

4. **Edit the Contact List:**
Edit the `contacts.csv` file to include your recipients:
Name,Email
Alice,alice@example.com
Bob,bob@example.com
Charlie,charlie@example.com

5. **Customize the Message:**
Modify the `message.txt` file to create your email content. Use placeholders for dynamic content:
Hello {name},

This is an automated reminder from our system.
We wanted to reach out and confirm your participation in the upcoming event.

Best regards,
Smart Automation Team

